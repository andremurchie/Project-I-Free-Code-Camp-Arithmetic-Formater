def arithmetic_arranger(problems, *args):
    if len(problems) > 5:
        return 'Error: Too many problems.'  # maximun of 5 equations

    arranged_problems = []

    for i in problems:
        if '*' in i or '/' in i or '**' in i or '%' in i:
            return "Error: Operator must be '+' or '-'."  #only addition or subtraction
        equation = i.split(' ')  # ["10", "+", "5"]            try:
        try:
            term_1 = int(equation[0])
            term_2 = int(equation[2])
        except:
            return 'Error: Numbers must only contain digits.'  # only digits
        if len(equation[0]) > 4 or len(equation[2]) > 4:
            return 'Error: Numbers cannot be more than four digits.'  # max of 4 digits

        long_term = max(len(equation[0]), len(equation[2]))
        width = long_term + 1

        #line up the numbers
        line_1 = f"{equation[0]:>{width + 1}}"
        line_2 = equation[1] + f"{equation[2]:>{width}}"
        dash = "-" * (width + 1)

        if equation[1] == "+":
            result = int(equation[0]) + int(equation[2])
            result = f"{str(result):>{width + 1}}"

        if equation[1] == "-":
            result = int(equation[0]) - int(equation[2])
            result = f"{str(result):>{width + 1}}"

        try:
            arranged_problems[0] += ('    ') + line_1
        except:
            arranged_problems.append(line_1)
        try:
            arranged_problems[1] += ('    ') + line_2
        except:
            arranged_problems.append(line_2)
        try:
            arranged_problems[2] += ('    ') + dash
        except:
            arranged_problems.append(dash)

        if args:
            try:
                arranged_problems[3] += ('    ') + result
            except:
                arranged_problems.append(result)

    n_args = (
        f"{arranged_problems[0]}\n{arranged_problems[1]}\n{arranged_problems[2]}"
    )

    if args:
        y_args = n_args + f"\n{arranged_problems[3]}"
        return y_args
    else:
        return n_args


print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]))
