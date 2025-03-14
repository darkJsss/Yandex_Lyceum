from flask import Flask, render_template_string

app = Flask(__name__)
professions = ['инженер-исследователь', 'пилот', 'строитель', 'экзобиолог', 'врач', 'инженер по терраформированию',
               'климатолог', 'специалист по радиационной защите', 'астрогеолог', 'гляциолог',
               'инженер жизниобеспечения', 'метеоролог', 'оператор марсохода', 'киберинженер', 'штурман', 'пилот дронов']

html = '''
<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <title>Профессии для миссии на Марсе</title>
</head>
<body>
    <h2>Список профессий, требуемых для успешной работы миссии на Марсе:</h2>

    {% if list_type == 'ol' %}
        <ol>
            {% for i in professions %}
                <li>{{ i }}</li>
            {% endfor %}
        </ol>
    {% elif list_type == 'ul' %}
        <ul>
            {% for i in professions %}
                <li>{{ i }}</li>
            {% endfor %}
        </ul>
    {% else %}
        <p>Неверный тип списка.</p>
    {% endif %}
</body>
</html>
'''


@app.route('/list_prof/<string:list_type>')
def list_prof(list_type):
    return render_template_string(html, list_type=list_type, professions=professions)


if __name__ == '__main__':
    app.run(debug=True)
