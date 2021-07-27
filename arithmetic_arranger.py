def arithmetic_arranger(problems, need_result=False):

    if len(problems) > 5:
        return "Error: Too many problems."

    operators = ['+', '-']

    row_1 = ''
    row_2 = ''
    row_3 = ''
    row_4 = ''

    for e, problem in enumerate(problems):

        num1, operator, num2 = problem.split()
        num1_len = len(num1)
        num2_len = len(num2)

        # handling 3 ERRORS
        # 1. checking operators
        if operator not in operators:
            return "Error: Operator must be '+' or '-'."

        # 2. checking digits
        if num1.isdigit() == False or num2.isdigit() == False:
            return 'Error: Numbers must only contain digits.'

        # 3. checking digits lenght (>4)
        if num1_len > 4 or num2_len > 4:
            return 'Error: Numbers cannot be more than four digits.'

        # calculations
        if operator == '+':
            result = int(num1) + int(num2)
        else:
            result = int(num1) - int(num2)

        # space
        space = max(num1_len,num2_len) + 2

        extra_space = '    '

        row_1 += num1.rjust(space)
        row_2 += operator + num2.rjust(space-1)
        row_3 += '-' * space
        row_4 += str(result).rjust(space)

        if e < len(problems) - 1:
            row_1 += extra_space
            row_2 += extra_space
            row_3 += extra_space
            row_4 += extra_space  

    if need_result:
        solution = row_1 + '\n' + row_2 + '\n' + row_3 + '\n' + row_4
    else:
        solution = row_1 + '\n' + row_2 + '\n' + row_3

    return solution
