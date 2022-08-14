from math import *

operators = [
        '+', '-', '*', '/', '%', '**', '//', '=', '+=', '-=', '*=', '/=', '%=', '//=', '**=', '&=', '|=', '^=',
        '>>=', '<<=','==', '!=','>', '<', '>=', '<=', 'and', 'or', 'not', 'is', 'is not', 'in', 'not in', '&',
        '|', '^', '~', '<<', '>>', 'return', 'def']
non_operators = [
    ':', ';', '.', "'", '"', '(', ')', '[', ']', '{', '}', '_', 
]


def operators_count(code):
    """
    This function calculates the number of operators and operands in a string of code (python)

    Parameter:
     code: code string

    return:
     (operators_dict, operators_list, operators amount, unique_operators_amount): Tuple containing operators and their occurence count, list containing operators and integer number of operators, integer number of unique operators.
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
    unique_operators_amount = [x for x in operators_dict.keys()]
    unique_operators_amount = len(unique_operators_amount)
    return(operators_dict, operators_list, operators_amount, unique_operators_amount)


def operands_count(code):
    """
    This function extracts the operands in a code and puts them in a code by isolating the operators and returning returnig what is left

    paratemer:
     code: code string

    return:
     (operands_amount, unique_operands_amount): integer number of operands and integer number of unique operands.
    """
    operands_dict = {}
    operands_list = []

    for char in code.split():
        if char not in operators and char not in non_operators:
            operands_list.append(char)
            if char not in operands_dict.keys():
                operands_dict[char] = 1
            else:
                operands_dict[char] +=1
    operands_amount = len(operands_list)
    unique_operands_amount = [x for x in operands_dict.keys()]
    unique_operands_amount = len(unique_operands_amount)
    return (operands_amount, unique_operands_amount)


def code_length_volume(unique_operators_amount, unique_operands_amount):
    """
    This function takes number of unique operators, number of unique operands and returns the codes estimate length and volumn.

    parameters:
     code: code string

    return:
     (length, volume) float values of code estimated length and volumn
    """

    n1, n2 = unique_operators_amount, unique_operands_amount
    n = n1 + n2
    length = (n1 * log2(n1) + n2 * log2(n2))
    volume = length * log2(n)
    return(length, volume)