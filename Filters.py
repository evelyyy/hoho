def censur(text):

    result = ""

    for letter in text:

        if letter == " ":

            result += " "

        else:

            result += "*"

    return result
def heart(text):
    result = 'heart'.join(text.split())

    return result
def smile(text):
    result = 'smile'.join(text.split())

    return result
def loud(text):
    result = text.upper()

    return result
def aestetic(text):
    result = text.lower()

    return result

