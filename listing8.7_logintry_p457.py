#this program takes password from the user and then check it
import login

def main():
    password = input('Enter password')

    while not login.valid_password(password):
        print('Pasword is not correct')
        password = input('Enter password.')
    print('Password is correct.')
def valid_password(password):
    correct_length = False
    has_uppercase = False
    has_lowercase = False
    has_digit = False
    if len(password) >= 7:
        correct_length = True
        for ch in password:
            if ch.isupper():
                has_uppercase = True
            if ch.islower():
                has_lowercase = True
            if ch.isdigit():
                has_digit = True
    if correct_length and has_uppercase and \
        has_lowercase and has_digit:
        is_valid = True
    else:
        is_valid = False
    return is_valid

main()