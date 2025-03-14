from flask import Flask, render_template_string

app = Flask(__name__)

html = """
<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <title>Подготовка к полету на Марс</title>
</head>
<body>
    {% if specialty == 'инженер' or specialty == 'строитель' %}
        <h2>Инженерные тренажеры</h2>
        <img src="/static/t1.jpg" alt="Схема расположения инженерных тренажеров">
    {% else %}
        <h2>Научные симуляторы</h2>
        <img src="/static/t2.jpeg" alt="Схема расположения научных симуляторов">
    {% endif %}
</body>
</html>
"""


@app.route('/training/<string:prof>')
def training(prof):
    return render_template_string(html, specialty=prof)


if __name__ == "__main__":
    app.run(debug=True)