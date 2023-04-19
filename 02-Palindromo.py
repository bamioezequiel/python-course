def reverse(text):
    reverse_text = ""
    for letter in text:
        reverse_text = letter + reverse_text
    return reverse_text

def is_palindromo(text):
    formatted_text = text.lower().replace(" ", "")
    #reverse_text = formatted_text[::-1]
    reverse_text = reverse(formatted_text)

    return formatted_text == reverse_text


print("Abba", is_palindromo("Abba")) #True
print("Reconocer", is_palindromo("Reconocer")) #True
print("Amo la paloma", is_palindromo("Amo la paloma")) #True
print("Hola Mundo", is_palindromo("Hola Mundo")) #False
