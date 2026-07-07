from  flask import  Flask, render_template
app = Flask(__name__)
@app.route('/')
def home():
    posts = [
        {
            "title": "HTML5 시맨틱 태그 완전 정복",
            "date": "2024년 1월 15일",
            "views": 1234,
            "desc": "HTML5 시맨틱 태그의 모든 것을 알아봅니다."
        },
        {
            "title": "CSS Grid vs Flexbox, 언제 무엇을 써야 할까?",
            "date": "2024년 1월 10일",
            "views": 856,
            "desc": "Grid와 Flexbox의 차이와 사용 시기"
        }
    ]

    return render_template("index.html", posts=posts)
if __name__ == '__main__':
    app.run(debug=True)