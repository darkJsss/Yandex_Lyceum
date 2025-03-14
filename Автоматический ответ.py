from flask import Flask, render_template, request

app = Flask(__name__, template_folder='templates', static_folder='static')

@app.route('/answer', methods=['POST'])
def answer():
    data = {
        'title': request.form.get('title'),
        'surname': request.form.get('surname'),
        'name': request.form.get('name'),
        'education': request.form.get('education'),
        'profession': request.form.get('profession'),
        'sex': request.form.get('sex'),
        'motivation': request.form.get('motivation'),
        'ready': request.form.get('ready')
    }
    return render_template('auto_answer.html', **data)

if __name__ == '__main__':
    app.run(debug=True)