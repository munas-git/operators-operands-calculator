from operands_operators import *
from flask import Flask, render_template, request


app = Flask(__name__)


@app.route('/home/', methods=['POST', 'GET'])
def home():
    if request.method == 'GET':
        return render_template('home.html')

    elif request.method == 'POST':
        original_code = request.form.get('code_input')
        clean_code = original_code.replace('\n', ' ').replace('\t', ' ')
        num_operators = operators_count(clean_code)
        num_operands = operands_count(clean_code)
        return render_template('result.html', num_operators = num_operators[2], num_operands = num_operands, original_code = original_code, clean_code = clean_code)



if __name__ == '__main__':
    app.run()