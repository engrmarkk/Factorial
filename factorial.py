from flask import Flask, render_template, request
app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def index():
    num1 = ''
    result = ''
    if request.method == 'POST' and "digit" in request.form:
        num1 = int(request.form.get('digit'))
        num2 = num1 + 1
        result = 1
        for i in range(1, num2):
            result *= i

    output = result
    return render_template('factorial.html', output=output, num1=num1)


if __name__ == '__main__':
    app.run(debug=True)
