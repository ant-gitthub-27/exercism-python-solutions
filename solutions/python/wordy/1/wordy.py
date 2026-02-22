def answer(question):
    
    numbers = []
    operations = []

        
    if not question.startswith('What is ') or not question.endswith('?'):
        raise ValueError("syntax error")

    question_list = question[:-1].split()

    for index, string in enumerate(question_list[2:]):
        if string in ['multiplied', 'divided', 'plus', 'minus']:
            operations.append(string)
        elif string.isnumeric():
            numbers.append(string)
        elif string[0] == '-':
            numbers.append(string)
        elif string != 'by':
            raise ValueError("unknown operation")

    if question_list[-1] in operations:
        raise ValueError("syntax error")
    
    
    if len(numbers) - len(operations) != 1:
        raise ValueError("syntax error")


    for index, string in enumerate(question_list):
        if string in ['plus', 'minus', 'multiplied', 'divided'] and question_list[index - 1] not in numbers:
            raise ValueError("syntax error")
        elif string in ['plus', 'minus', 'by'] and question_list[index + 1] not in numbers:
            raise ValueError("syntax error")

    temp = 0
    i = 0
    
    while i < len(operations):
        if operations[i] in ['multiplied', 'divided']:
            op = operations.pop(i)
            num1 = int(numbers.pop(i))
            num2 = int(numbers.pop(i))

            if op == 'multiplied':
                temp = num1 * num2
            else:
                temp = num1 / num2

            numbers.insert(i, temp)
        elif operations[i] in ['plus', 'minus']:
            op = operations.pop(i)
            num1 = int(numbers.pop(i))
            num2 = int(numbers.pop(i))

            if op == 'plus':
                temp = num1 + num2
            else:
                temp = num1 - num2

            numbers.insert(i, temp)
        else: 
            i += 1

    return int(numbers[0])