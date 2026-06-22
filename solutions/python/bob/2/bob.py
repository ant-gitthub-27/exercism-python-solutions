def response(hey_bob):
    cleaned = hey_bob.strip()
    if not cleaned:
        return "Fine. Be that way!"
    if cleaned.endswith("?"):
        if cleaned.isupper():
            return "Calm down, I know what I'm doing!" 
        else:
            return "Sure."
    else:
        if cleaned.isupper():
            return "Whoa, chill out!"
        else:
            return "Whatever."