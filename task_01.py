import string

def is_palindrome(name):
    translator = str.maketrans('', '', string.punctuation)
    clean_text = str(name).translate(translator)
    clean_text = clean_text.replace(" ", "")
    clean_text = clean_text.lower()
    if ''.join(reversed(clean_text)) == clean_text:
        print("True")
        return True
    else:
        print("False")
        return False

is_palindrome("A man, a plan, a canal -- Panama")
is_palindrome("Madam, I'm Adam!")
is_palindrome(333)
is_palindrome(None)
is_palindrome("Abracadabra")
