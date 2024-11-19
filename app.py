from flask import Flask, render_template, request

app = Flask(__name__)

class User:
    def __init__(self, name, city, hobby, age):
        self.name = name
        self.city = city
        self.hobby = hobby
        self.age = age

@app.route('/')
def home():
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        city = request.form['city']
        hobby = request.form['hobby']
        age = request.form['age']

        user = User(name, city, hobby, age)
        return render_template('form.html', user=user)

if __name__ == '__main__':
    app.run(debug=True)


# from flask import Flask, render_template, request
#
# app = Flask(__name__)
#
# @app.route("/", methods=["GET", "POST"])
# def user_form():
#     user_data = None  # Переменная для хранения данных пользователя
#
#     if request.method == "POST":
#         # Извлекаем данные из формы
#         name = request.form.get("name")
#         city = request.form.get("city")
#         hobby = request.form.get("hobby")
#         age = request.form.get("age")
#
#         # Сохраняем данные в словарь
#         user_data = {
#             "name": name,
#             "city": city,
#             "hobby": hobby,
#             "age": age
#         }
#
#     # Передаём данные в шаблон
#     return render_template("form.html", user_data=user_data)
#
# if __name__ == "__main__":
#     app.run(debug=True)
