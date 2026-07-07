
# LMS/service/BoardService.py

from LMS.common import Session
import math

class BoardService:

    @staticmethod
    def list_paged(board_type="notice", keyword="", page=1, size=10):  # 페이징 처리
        import math

        # page 최소 1 보정
        if page < 1:
            page = 1

        # size 최소/최대 보정(너무 크게 못가게)
        if size < 1:
            size = 10
        if size > 50:
            size = 50

        offset = (page - 1) * size

        conn = Session.get_connection()
        try:
            with conn.cursor() as cursor:
                where = "WHERE 1=1"
                params = []

                # ⭐ all이 아닐 때만 타입 필터 적용
                if board_type != "all":
                    where += " AND b.board_type = %s"
                    params.append(board_type)

                # 검색어가 있으면 title/content 검색
                if keyword:
                    where += " AND (b.title LIKE %s OR b.content LIKE %s)"
                    like = f"%{keyword}%"
                    params.extend([like, like])

                # ✅ 전체 개수(페이징용)
                sql_count = f"SELECT COUNT(*) AS cnt FROM boards b {where}"
                cursor.execute(sql_count, tuple(params))
                total = cursor.fetchone()["cnt"]

                pages = max(1, math.ceil(total / size))

                # page가 총 페이지보다 크면 마지막 페이지로 보정
                if page > pages:
                    page = pages
                    offset = (page - 1) * size

                # ✅ 실제 목록 조회
                # - 상단고정 먼저
                # - display_date가 있으면 그 날짜 우선, 없으면 created_at
                # - 같은 시간대 정렬 흔들림 방지로 id DESC 추가
                sql_list = f"""
                    SELECT
                        b.*,
                        m.name AS writer_name,
                        m.uid AS writer_uid,

                        /* 좋아요 개수 */
                        (SELECT COUNT(*) FROM board_likes bl WHERE bl.board_id = b.id) AS like_count,

                        /* 댓글 개수 (대댓글 포함) */
                        (SELECT COUNT(*) FROM board_comments bc WHERE bc.board_id = b.id) AS comment_count

                    FROM boards b
                    JOIN members m ON b.member_id = m.id
                    {where}

                    ORDER BY
                        b.is_pinned DESC,
                        COALESCE(b.display_date, b.created_at) DESC,
                        b.id DESC

                    LIMIT %s OFFSET %s
                """
                cursor.execute(sql_list, tuple(params + [size, offset]))
                items = cursor.fetchall()

                return {
                    "items": items,
                    "page": page,
                    "size": size,
                    "total": total,
                    "pages": pages,
                }
        finally:
            conn.close()

    @staticmethod
    def list(board_type="notice", keyword=""):
        conn = Session.get_connection()
        try:
            with conn.cursor() as cursor:

                sql = """
                    SELECT
                      b.id,
                      b.title,
                      b.board_type,
                      b.is_pinned,
                      b.display_date,
                      b.created_at,
                      b.view_count,

                      m.name AS writer_name,
                      m.uid  AS writer_uid,

                      (SELECT COUNT(*) FROM board_likes bl WHERE bl.board_id = b.id) AS like_count,
                      (SELECT COUNT(*) FROM board_comments bc WHERE bc.board_id = b.id) AS comment_count

                    FROM boards b
                    JOIN members m ON b.member_id = m.id
                    WHERE b.board_type = %s
                """

                params = [board_type]

                if keyword:
                    sql += " AND (b.title LIKE %s OR b.content LIKE %s) "
                    like = f"%{keyword}%"
                    params.extend([like, like])

                sql += """
                    ORDER BY
                      b.is_pinned DESC,
                      COALESCE(b.display_date, DATE(b.created_at)) DESC,
                      b.id DESC
                """

                cursor.execute(sql, params)
                return cursor.fetchall()

        finally:
            conn.close()

    @staticmethod
    def notice_preview(limit=5):    # 공지사항 미리보기
        conn = Session.get_connection()
        try:
            with conn.cursor() as cursor:
                sql = """
                        SELECT b.*, m.name AS writer_name, m.uid AS writer_uid
                        FROM boards b
                        JOIN members m ON b.member_id = m.id
                        WHERE b.board_type = 'notice'
                        ORDER BY b.is_pinned DESC, b.created_at DESC
                        LIMIT %s
                    """
                cursor.execute(sql, (limit,))
                return cursor.fetchall()
        finally:
            conn.close()

    @staticmethod
    def update(board_id, title, content):
        conn = Session.get_connection()
        try:
            with conn.cursor() as cursor:
                sql = """
                    UPDATE boards
                    SET title=%s, content=%s
                    WHERE id=%s
                """
                cursor.execute(sql, (title, content, board_id))
            conn.commit()
        finally:
            conn.close()

    @staticmethod
    def delete(board_id):
        conn = Session.get_connection()
        try:
            with conn.cursor() as cursor:
                # (댓글 테이블이 board_id FK면 먼저 댓글 삭제 권장)
                cursor.execute("DELETE FROM board_comments WHERE board_id=%s", (board_id,))
                cursor.execute("DELETE FROM boards WHERE id=%s", (board_id,))
            conn.commit()
        finally:
            conn.close()