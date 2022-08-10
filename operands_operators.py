operators = [
        '+', '-', '*', '/', '%', '**', '//', '=', '+=', '-=', '*=', '/=', '%=', '//=', '**=', '&=', '|=', '^=',
        '>>=', '<<=','==', '!=','>', '<', '>=', '<=', 'and', 'or', 'not', 'is', 'is not', 'in', 'not in', '&',
        '|', '^', '~', '<<', '>>', 'return', 'def']
non_operators = [
    ':', ';', '.', "'", '"', '(', ')', '[', ']', '{', '}', 
]


def operators_count(code):
    """
    This function calculates the number of operators and operands in a string of code (python)

    Parameter:
    code: code string

    return:
    (operators_dict, operators_list, operators amount): Tuple containing operators and their occurence count, list containing operators and integer sum of operators.
    """
    operators_dict = {}
    operators_list = []
    
    for char in code.split():
        if char in operators:
            operators_list.append(char)
            if char not in operators_dict.keys():
                operators_dict[char] = 1
            else:
                operators_dict[char] +=1
    operators_amount = len(operators_list)
    return(operators_dict, operators_list, operators_amount)


def operands_count(code):
    """
    This function extracts the operands in a code and puts them in a code by isolating the operators and returning returnig what is left

    paratemer:
    code: code string

    return:
    operands_list: integer sum of operands.
    """
    operands_list = []

    for char in code.split():
        if char not in operators and char not in non_operators:
            operands_list.append(char)
    operands_amount = len(operands_list)
    return operands_amount