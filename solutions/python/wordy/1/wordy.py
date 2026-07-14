def answer(question):

    if not question.startswith("What is ") or not question.endswith("?"):
        raise ValueError("syntax error") 
    
    question = question[8:-1]
    if not question:
        raise ValueError("syntax error")
    
    question = question.replace("plus", "+").replace("minus", "-").replace("multiplied by", "*").replace("divided by", "/")

    tokens = question.split()

    if tokens[-1] == "cubed":
        raise ValueError("unknown operation")
    if len(tokens) % 2 == 0:
        raise ValueError("syntax error")

    for n, token in enumerate(tokens):
        if n % 2 == 0:
            fixed_token = token[1:] if token.startswith("-") else token
            if not fixed_token.isdigit():
                raise ValueError("unknown operation" if token.isalpha() else "syntax error")
        else:
            if token not in ["+", "-", "*", "/"]:
                raise ValueError("unknown operation" if token.isalpha() else "syntax error")

    result = int(tokens[0])

    for i in range(1, len(tokens), 2):
        operator = tokens[i]
        next_number = int(tokens[i+1])

        if operator == "+":
            result += next_number
        elif operator == "-":
            result -= next_number
        elif operator == "*":
            result *= next_number
        elif operator == "/":
            result = int(result / next_number)
    return result