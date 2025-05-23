def phone_number(text):
    if len(text) == 10:
        digits = "(" + text[0:3] + ")" + "-" + text[3:6] + "-" + text[6:]
    return digits
