from flask import Flask, render_template, request, redirect, url_for, session
from LMS.common import Session
from LMS.domain import Board, Score

app = Flask(__name__)
app.secret_key = "fffffff"


@app.route('/') # url 생성용 코드 http://localhost:5000/ or http://192.168.0.???:5000
def index():
    return render_template('main.html')
    # render_template 웹브라우저로 보낼 파일명
    # templates 라는 폴더에서 main.html을 찾아 보냄


@app.route('/login', methods=['GET', 'POST'])
def login():                                              # 로그인
    if request.method == 'GET':
        # 지금들어온 요청이 페이지 요청이니?
        return render_template('login.html')
        #  요청이 맞으면 login.html 여기로 보내라~
    uid = request.form.get('uid')  # post로 넘어온 form데이터를 request.form 안에 딕셔너리타입으로 넣어준다
    upw = request.form.get('upw')
    conn = Session.get_connection() # 디비에 접속
    try:
        print(request.form)
        with conn.cursor() as cursor: #디비에 전화를 건다
            sql = "SELECT id, name, uid, role \
            from members where uid = %s and password = %s"
        # 멤버스테이블에서 uid,password 가 일치하는 사람의 id, 이름, 권한을 가져와~
            cursor.execute(sql, (uid, upw)) # 상담원이 uid,upw를 디비에 적용한다
            user = cursor.fetchone() # 조회된 결과의 회원정보를 한줄로 만들어 놓아바~~

        if user: # 회원정보가 있으면 브라우져의 세션영역에 보관한다~!
            session['user_id'] = user['id']
            session['user_name'] = user['name']
            session['user_uid'] = user['uid']
            session['user_role'] = user['role']  #브라우져 f12/애플리케이션/쿠키에 가면 세션정보가 보임(쿠키삭제하면 로그아웃됨)
            return redirect(url_for('index'))  # 로그인이 끝났으니 메인페이지 인덱스로 가라~

        else:
            return "<script>alert('아이디나 비번이 틀렸습니다.');history.back();</script>"
                  #자바스크립트영역  alert(경고창)               뒤로가기         스크립트닫기
    finally:
        conn.close() # 연결종료

@app.route('/logout')                                   # 로그아웃
def logout():
    session.clear() # 세션 비우기
    return redirect(url_for('login')) # 로긴화면으로 가기

@app.route('/join', methods=['GET', 'POST'])
def join():                                             # 조인은 회원가입용 필수 코드다~
    if request.method == 'GET': # 지금 들어온코드가 회원가입화면을 보여달라는건지 확인한다
        return render_template('join.html') # 회원가입화면을 보여준다~!!
    uid = request.form.get('uid')   #회원가입 폼에서 사용자가 입력한 아이디를 꺼낸다
    password = request.form.get('password') #회원가입 폼에서 사용자가 입력한 패스워드를 꺼낸다
    name = request.form.get('name') # 회원가입폼에서 사용자가 입력한 이름을 꺼낸다.

    conn = Session.get_connection() # 디비에 연결해서 회원정보를 저장할 준비를 한다
    try:
        with conn.cursor() as cursor:
            cursor.execute("select id from members where uid =%s", (uid,)) # 입력한 아이디가 디비에 있니??
            if cursor.fetchone(): # 조회결과가 하나라도 있으면
                return "<script>alert('이미 존재하는아이디입니다.');history.back();</script>" #경고창 띄우기
            sql = "INSERT INTO members (uid, password, name) VALUES (%s, %s, %s);"
            # 멤버스테이블에 입력한 값을 새회원을 저장하는 sql변수에 넣어놔~
            cursor.execute(sql, (uid, password, name)) # sql을 아이디 비번 이름을 디비에 넣어~!
            conn.commit() # 저장 해라 (이줄이 없으면 저장안된다~!!)
            return "<script>alert('회원가입이 완료되었습니다.');location.href='/login;</script>"
                   # 자바스크립트  알림창            (현재주소를 바꾸는 자바스크립트코드) 로그인 주소로이동

    except Exception as e:  # 예외발생시 실행문
        print(f"회원가입 에러: {e}")
        return "가입 중 오류가 발생했습니다. /n join()메서드를 확인하세요!!!"
    finally:  # 항상 실행문
        conn.close()

@app.route('/member/edit', methods=['GET', 'POST'])
def member_edit():                                      # 회원정보 수정하기
    if 'user_id' not in session:    # 로그인이 안되어있으면
        return redirect(url_for('login')) # 로긴화면으로 가
    conn = Session.get_connection() # 있으면 디비연결
    try:
        with conn.cursor() as cursor: #디비를열어
            if request.method == 'GET': #겟 페이지 요청
                cursor.execute("SELECT * FROM members WHERE id = %s", (session['user_id'],)) #세션에로긴한사람을 조회
                user_info = cursor.fetchone() #조회되면 한줄로 나열
                return render_template('member_edit.html', user=user_info)
                #      템플릿파일로 넘어가                   회원수정화면띄우기   조회된내용 화면에 띄우기
            new_name = request.form.get('name') #새이름 폼에서 가져와
            new_pw = request.form.get('password') #새비밀번호 폼에서 가져와

            if new_pw: #새비밀번호가 입력이 되었니?
                sql = "UPDATE members SET name = %s, password = %s WHERE id = %s"
                # 이름과 비밀번호를 업데이트를 하는 sql변수를 만든다
                cursor.execute(sql, (new_name, new_pw, session['user_id']))
                # 디비에 sql변수에 저장한 새이름 비번을 세션아이디에 넣어라~~~
            else: # 새비번이 입력안되구 나머지이름만 수정되었니??
                sql = "UPDATE members SET name = %s WHERE id = %s"
                # 변경된 이름을 sql변수에 넣어놔
                cursor.execute(sql, (new_name, session['user_id']))
                # 디비에 sql변수에 있는 새이름 넣어~

            conn.commit() # 저장해라
            session['user_name'] = new_name  # 이름이 변경되었으니 세션에 이름도 변경해주쟈~!!!업데이트
            return "<script>alert('정보가 수정되었습니다.'); location.href='/mypage';</script>"
            #                                               이동해        마이페이지로
    except Exception as e:# 예외발생시 실행문
        print(f"회원수정 에러: {e}")
        return "수정 중 오류가 발생했습니다. \n member_edit()메서드를 확인하세요!!!"

    finally:  # 항상 실행문
        conn.close()


@app.route('/mypage')
def mypage():
    if 'user_id' not in session:  # 로그인이 안되어있으면
        return redirect(url_for('login'))  # 로긴화면으로 가
    conn = Session.get_connection()  # 있으면 디비연결
    try:
        with conn.cursor() as cursor:
            cursor.execute("select * from members where id = %s", (session['user_id'],)) #세션에 로긴한사람 조회
            user_info = cursor.fetchone() # 한줄로 나열
            # 게시글 개수 조회 (보드테이블활용)
            cursor.execute("SELECT COUNT(*) as board_count FROM boards WHERE member_id = %s", (session['user_id'],))
            # 디비에서            3. 갯수센다 4. 보드카운트에담아    2.보드에 작성한아이디          1. 세션에 아이디가
            board_count = cursor.fetchone()['board_count'] # 방금조회한걸 한줄로 가져와 보드카운트 값을 꺼내와
            return render_template('mypage.html', user=user_info, board_count=board_count)
            #    템플릿트 파일로 이동해                  마이페이지로가      회원정보랑           보드카운트 화면에 띄우기
    finally:
        conn.close()

    #################################### 회원 CRUD END #################################################################

    #################################### 게시판 CRUD ##################################################################
@app.route('/board/write', methods=['GET', 'POST'])
def board_write():      # 글쓰기
    if request.method == 'GET': # 글쓰기 버튼을 눌렀을때
        if 'user_id' not in session:
            return '<script>alert("로그인 후 이용 가능합니다."); location.href="/login";</script>'
        return render_template('board_write.html')

    elif request.method == 'POST': # 등록하기 버튼을 눌렀을때
        title = request.form.get('title') # 폼에서 타이틀 꺼내와
        content = request.form.get('content') # 폼에서 컨텐츠 꺼내와
        member_id = session.get('user_id') # 세션에 로그인한 아이디 꺼내와

        conn = Session.get_connection() #디비 연결시작
        try:
            with conn.cursor() as cursor: # 디비 상담원 연결
                sql = "INSERT INTO boards (member_id, title, content) VALUES (%s, %s, %s)"
                # 보드스에 테이블에 글을 저장하기 위한 sql문 작성
                cursor.execute(sql, (member_id, title, content))
                # 디비에 변수를 넣어
                conn.commit() # 저장해
            return redirect(url_for('board_list'))  # 저장 후 목록으로 이동
        except Exception as e:
            print(f"글쓰기 에러: {e}")
            return "저장 중 에러가 발생했습니다."
        finally:
            conn.close()

@app.route('/board')
def board_list():   # 게시판 목록
    conn = Session.get_connection() # 디비 연결
    try:
        with conn.cursor() as cursor:
            sql = """
                SELECT b.*, m.name as writer_name
                FROM boards b
                JOIN members m ON b.member_id = m.id
                ORDER BY b.id DESC
            """
            # 보드테이블 전체, 멤버스테이블의 네임을 writer_name 이걸로해
            # 보드테이블은 b라고 할꺼야
            # boards의 member_id(작성자 번호)와 members의 id(회원 번호)가 같은 것끼리 연결한다 (JOIN)
            # 보드아이디를 최신 글이 위로 오도록 id 기준 내림차순 정렬
            cursor.execute(sql) # 위에서 작성한 sql을 연결한다
            rows = cursor.fetchall() # 조횐된 모든것을 rows에 넣어~
            boards = [Board.from_db(row)for row in rows]
            # rows 안에 있는 row를 하나씩 꺼내서 Board.from_db()에 넣고 Board 객체로 만든 다음 리스트에 담는다
            return render_template('board_list.html', boards=boards)
    finally:
        conn.close()

@app.route('/board/view/<int:board_id>')
def board_view(board_id):   # 게시판 자세히 보기
    conn = Session.get_connection()  # 디비연결
    try:
        with conn.cursor() as cursor:
            sql = """
                SELECT b.*, m.name as writer_name, m.uid as writer_uid
                FROM boards b JOIN members m 
                ON b.member_id = m.id
                WHERE b.id = %s
            """
            # 보드테이블 전체. 멤버네임을 writer_name, 멤버유아이디를 writer_uid 라고 할꺼야
            # 보드테이블을 b라고 함
            # 멤버스테이블을 m이라고 함 b.member_id = m.id 같은것끼리 연결
            # 게시글 id가 특정 값인 것만 가져온다
            # 👉 즉, 게시글 하나만 조회

            cursor.execute(sql, (board_id,)) # sql문을 실행해서 보드아이디에 해당하는 게시글을 디비에서 찾아
            row = cursor.fetchone() # 한줄로 꺼내와~
            if not row: # 없으면
                return "<scrip>alert('존재하지 않는 게시글입니다.');history.back();</script>"

            board = Board.from_db(row) # 있으면 한줄을 보드 객체화를 시켜
            return render_template('board_view.html', board=board)
            #       이동해                               보드자세히보기로   보드 객체를 넘겨준다
    finally:
        conn.close()

@app.route('/board/edit/<int:board_id>', methods=['GET', 'POST'])
def board_edit(board_id):    # 게시판 수정 관리하기
    conn = Session.get_connection() # 디비 접속
    try:
        with conn.cursor() as cursor: # 디비 상담원 연결
            if request.method == 'GET': # 수정하기 버튼 눌렀을때
                sql = "SELECT * FROM boards WHERE id = %s" # 게시글 작성자 아이디 글을 디비에 찾아 SQL에 담아
                cursor.execute(sql, (board_id,)) # 보드아이디에 SQL문을 넣어~
                row = cursor.fetchone() # 조회된걸 한줄로 가져와

                if not row: # 게시글이 없으면
                    return "<script>alert('존재하지 않는 게시글입니다.');history.back();</script>"
                if row['member_id'] != session.get('user_id'): # 게시글 작성자와 로그인한 사용자가 다르면
                    return "<script>alert('수정 권한이 없습니다.');history.back();</script>"
                print(row)
                board = Board.from_db(row) # 디비에 한줄데이터를 보드 객체로 변환해
                return render_template('board_edit.html', board=board)
                #        이동해                   보드 수정화면으로      기존글 화면에 보여줘

            elif request.method == 'POST': # 이제 수정하자~
                title = request.form.get('title') # 타이들입력값 가져와
                content = request.form.get('content') # 컨텐츠 입력값 가져와

                sql = "UPDATE boards SET title = %s, content = %s WHERE id = %s"
                # 업데이트 수정할꺼야~ 보드테이블에서 아이디값을 가져와서 제목과 컨텐츠를 새값으로 입력해~
                cursor.execute(sql, (title, content, board_id)) # 디비에 sql문실행해서 해당 객체를 찾아~
                conn.commit() # 저장해
                return redirect(url_for('board_view', board_id=board_id))
                #      이동해 다른파일로간다~                    게시글보기    아이디글을 보여줘~
    finally:
        conn.close()
@app.route('/board/delete/<int:board_id>')
def board_delete(board_id):
    conn = Session.get_connection()
    try:
        with conn.cursor() as cursor:
            sql = "DELETE FROM boards WHERE id = %s"
            # 디비 보드스테이블에서 특정값 아이디를 삭제할꺼야
            cursor.execute(sql, (board_id,)) # 디비에 sql문을 실행 특정값 아이디 삭제
            conn.commit() # 저장해
            if cursor.rowcount > 0: # 실제 삭제된 행이 있는지 확인 rowcount는 영향을 받은행 갯수야
                print(f"게시글 {board_id}번 삭제 성공")
            else:
                return redirect(url_for('board_list')) # 삭제된것이 없으면 게시글 리스트로가~
        return redirect(url_for('board_list')) # 삭제 성공해도 리스트로가~
    except Exception as e:
        print(f"삭제 에러: {e}")
        return "삭제 중 오류가 발생했습니다."
    finally:
        conn.close()

    #################################### 게시판 CRUD END ###############################################################
    #################################### 성적 CRUD 시작 ################################################################
@app.route('/score/add') # 성적 조회
def score_add():
    if session.get('user_role') not in ('admin', 'manager'): # 권한 설정 사용자의역활이 어드민 매니저가 아니면
        return "<script>alert('권한이 없습니다.'); history.back();</script>"
    target_uid = request.args.get('uid') #권한이있으면 url에서 uid값 가져와 (args는 url주소로 입력됨)
    target_name = request.args.get('name') # 이름 가져와~       (add?uid=test1&name=홍길동 이런식이야)
    conn = Session.get_connection() # 디비연결해
    try:
        with conn.cursor() as cursor: # 디비 상담원이
            cursor.execute("SELECT id FROM members WHERE uid = %s", (target_uid,))
            #                              멤버스테이블에서  uid를 찾아
            student = cursor.fetchone() # 한줄로 아이디정보를 가져와~

            existing_score = None # 기존 성적이 있는지 조회하는 변수~~밑에 써먹을꺼야~!!
            if student: #학생이 있으면
                cursor.execute("SELECT * FROM scores WHERE member_id = %s", (student['id'],))
                #                             스코어테이블에서 멤버아이디      한줄로만든 객체를 아이디에 넣어
                row = cursor.fetchone() # 성적 1줄 가져와
                print(row)
                if row: # 성적이 있다면
                    existing_score = Score.from_db(row) # 스코어 디비한줄을 스코어 객체로 변환해
            return render_template('score_form.html',
                                   target_uid=target_uid,
                                   target_name=target_name,
                                   score=existing_score)
            #  스코어 폼으로 이동해 , 아이디 이름 성적을 내가만든 변수에 담은 것을 전송해, 없으면 새로 입력화면, 있으면 수정화면
    finally:
        conn.close()


@app.route('/score/save', methods=['POST'])
def score_save():
    if session.get('user_role') not in ('admin', 'manager'):
        return "권한 오류", 403
    target_uid = request.form.get('target_uid') # 성적이 있으면 폼에서 아이디 꺼내와
    kor = int(request.form.get('korean', 0)) # 국어점수,정수형으로 꺼내와, 값이 없으면 0처리
    eng = int(request.form.get('english', 0)) # 영어점수,숫자형으로 꺼내와, 값이 없으면 0처리
    math = int(request.form.get('math', 0)) # 수학점수, 정수형으로 꺼내와, 값이 없으면 0처리

    conn = Session.get_connection() # 디비 연결하자
    try:
        with conn.cursor() as cursor: # 디비 상담원 연결
            cursor.execute("SELECT id FROM members WHERE uid = %s", (target_uid,))
            #                             멤버스테이블에서 아이디를 찾아와 (타겟 아이디를)
            student = cursor.fetchone() # 학생 한명을 조회해  (row)한줄이아니야~!!
            print(student) # 이게 뭔지 출력해바
            if not student: # 학생이 없으면
                return "<script>alert('존재하지 않는 학생입니다.'); history.back();</script>"

            temp_score = Score(member_id=student['id'], kor=kor, eng=eng, math=math) # 변수만들어 Score.py의 객체가져와
            cursor.execute("SELECT id FROM scores WHERE member_id = %s", (student['id'],))
            #                              스코어테이블에서  멤버아이디 특정값이  변수아이디인걸 찾아
            is_exist = cursor.fetchone() #한줄로 가져와 변수에 저장한다 is_exist 변수명
            if is_exist: # 있으면 업데이트 수정해~
                sql = """
                    UPDATE scores SET korean = %s, english = %s, math = %s,
                                        total = %s, avgrage = %s, grade = %s
                    WHERE member_id = %s
                """
                cursor.execute(sql,(temp_score.kor, temp_score.eng, temp_score.math,
                                    temp_score.total, temp_score.avg, temp_score.grade,
                                    student['id']))
            else: # 없으면 새로 저장해~
                sql = """
                    INSERT INTO scores (member_id, korean, english, math, total, avgrage, grade)
                    VALUES (%s, %s, %s, %s, %s, %s, %s)
                """
                cursor.execute(sql,(student['id'], temp_score.kor, temp_score.eng, temp_score.math,
                                    temp_score.total, temp_score.avg, temp_score.grade,))
            conn.commit()
            return f"<script>alert('{target_uid} 학생 성적 저장 완료!'); location.href='/score/list';</script>"
    finally:
        conn.close()

@app.route('/score/list')
def score_list():  # 성적 리스트
    if session.get('user_role') not in ('admin', 'manager'): # 권한설정
        return "<script>alert('권한이 없습니다.'); history.back();</script>"
    conn = Session.get_connection() # 디비열어
    try:
        with conn.cursor() as cursor:
            sql = """
                SELECT m.name, m.uid, s.* FROM scores s
                JOIN members m 
                ON s.member_id = m.id
                ORDER BY s.total DESC
            """
            # 멤버 네임,uid 가져와
            # 스코어테이블 모든것을
            # 스코어 테이블은 s, 멤버테이블은 m
            # s.member_id = m.id 같은걸 끼리 연결해~
            # 점수 높은순으로 정렬 (DESC)내림차순

            cursor.execute(sql) # sql문 디비에 실행해~
            datas = cursor.fetchall() # 결과를 전체 가져와 datas 변수 만들었어~
            print(f"sql 결과테스트 {datas}") # 가져온값 확인 프린트

            score_objects = [] # 성적 객체들을 담을 빈 리스트 생성

            for data in datas: # 데이타 안에있는 한줄씩 꺼내~
                s = Score.from_db(data) # 데이타 한줄을 Score.py에 있는 객체로 변환하는거야 (성적이 국어,영어,수학,총점등등..)
                s.name = data['name'] # 조인한 테이블에서 이름도 가져와 (Score.py엔 이름이없어)
                s.uid = data['uid'] # 조인한 테이블에서 아이디도 가져와 (Score.py엔 아이디없어)
                score_objects.append(s) # 완성된걸 score_objects에 담아~~~
            return render_template('score_list.html', scores=score_objects)
            #         이동해                          스코어 리스트로~       화면에 변수를 출력해~~
    finally:
        conn.close()

@app.route('/score/members')
def score_members():
    if session.get('user_role') not in ('admin', 'manager'): #권한 설정
        return "<script>alert('권한이 없습니다.'); history.back();</script>"

    conn = Session.get_connection() # 디비열어
    try:
        with conn.cursor() as cursor:
            sql = """
                SELECT m.id, m.uid, m.name, s.id AS score_id
                FROM members m
                LEFT JOIN scores s ON m.id = s.member_id
                WHERE m.role = 'user'
                ORDER BY m.name ASC
            """
            # 멤버 네임,uid 가져와
            # 스코어테이블에서 성적이 있으면 가져와 이름을 score_id 이걸로 바꿔
            # 멤버스는 m, 스코어스는 s 왼쪽기준으로 정리해
            # members 기준으로
            # 👉 scores를 왼쪽 조인
            # 의미는 👇
            # 성적이 있는 학생 → score_id 있음
            # 성적이 없는 학생 → score_id = None
            # 학생만 조회해~
            # 이름 오름차순으로 정리해
            cursor.execute(sql) #sql문 디비에 실행해~
            members = cursor.fetchall() # 모든결과 가져와~
            return render_template('score_member_list.html', members=members)
            #          이동해                               리스트로             결과 출력해~
    finally:
        conn.close()

@app.route('/score/my')  # http://localhost:5000/score/my -> get
def score_my():
    if 'user_id' not in session: # 로그인 안했으면 돌아가 로그인창으로
        return redirect(url_for('login'))

    conn = Session.get_connection() # 디비연결
    try:
        with conn.cursor() as cursor:

            sql = "SELECT * FROM scores WHERE member_id = %s;" # 스코어스테이블에서 멤버아이디를 가져와
            cursor.execute(sql, (session['user_id'],)) # sql실행 멤버아이디를 세션아이디에 전달
            row = cursor.fetchone() # 한줄로 정리해
            print(row)  # 딕셔너리타입으로 결과물 들어옴
            score = Score.from_db(row) if row else None # 한줄정리한걸 객체화 시켜 없으면 논처리
            return render_template('score_my.html', score=score)
            #       이동해                             이파일로           값을 출력해
    finally:
        conn.close()

    #  ============================= 실행 ====================================


if __name__ == '__main__':

    app.run(host='0.0.0.0', port=5000, debug=True)
