def response(hey_bob):


    hey_bob = "".join(hey_bob.split())    

    if(hey_bob == ""):
        return('Fine. Be that way!')
    elif(hey_bob[-1] == '?'):
        if(hey_bob.isupper()):
            return("Calm down, I know what I'm doing!")
        else:
            return('Sure.')
    elif(hey_bob.isupper()):
        return('Whoa, chill out!')
    elif(hey_bob.isspace()):
        return('Fine. Be that way!')
    else:
        return('Whatever.') 
