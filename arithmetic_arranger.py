def arithmetic_arranger(given, solve=False):
    for expression in given:
        if len(given) > 5:
            return "Error: Too many problems."

        first_number = expression.split()[0]
        second_number = expression.split()[2]
        operator = expression.split()[1]
        if len(first_number) > 4 or len(second_number) > 4:
            return "Error: Numbers cannot be more than four digits."
        if operator == '*' or operator == '/':
            return "Error: Operator must be '+' or '-'."

        sum = ''
        if operator == '+':
            sum = str(int(first_number) + int(second_number))
        else:
            sum = str(int(first_number) - int(second_number))

        max_length = max(len(first_number), len(second_number))

        first_line = str(first_number).rjust(max_length)
        second_line = operator + str(second_number).rjust(max_length-1)


        line = ''
        for i in range(max_length):
            line += ('-')

        answer = str(sum).rjust(max_length)

        first_printed = ''
        second_printed = ''
        printed_answer = ''

        if expression[0] != expression[2]:
            first_printed += first_line + ' '
            second_printed += second_line + ' '
            printed_answer += answer + ' '
        else:
            first_printed += first_line
            second_printed += second_line
            printed_answer += answer

    if solve:
        result = first_printed + '\n' + second_printed + '\n' + line + '\n' + printed_answer
    else:
        result = result = first_printed + '\n' + second_printed
    return result
