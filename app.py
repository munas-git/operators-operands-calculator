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
        operators = operators_count(clean_code)
        operands = operands_count(clean_code)
        unique_operands_amount = operands[1]
        unique_operators_amount = operators[3]
        length_volume = code_length_volume(unique_operators_amount, unique_operands_amount) 
        length = '{0:.2f}'.format(length_volume[0])
        volume = '{0:.2f}'.format(length_volume[1])
        return render_template('result.html', num_operators = operators[2], num_operands = operands[0], original_code = original_code, clean_code = clean_code, length = length, volume = volume, unique_operands_amount= unique_operands_amount, unique_operators_amount = unique_operators_amount)



if __name__ == '__main__':
    app.run()