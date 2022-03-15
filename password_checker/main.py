import string

password = input("Enter your password: ")

upper_case = any([1 if c in string.ascii_uppercase else 0 for c in password])
lower_case = any([1 if c in string.ascii_lowercase else 0 for c in password])
special = any([1 if c in string.punctuation else 0 for c in password])
digits = any([1 if c in string.digits else 0 for c in password])

characters = [upper_case, lower_case, special, digits]

password_length = len(password)

score = 0

with open('common_password.txt', 'r') as f:
    common = f.read().splitlines()

if password in common:
    print("Password compromise!")
    exit()

if password_length > 8:
    score += 1
if password_length > 16:
    score += 1
if password_length > 24:
    score += 1

print(f"Password length is {str(password_length)}")

if sum(characters) > 1:
    score += 1
if sum(characters) > 2:
    score += 1
if sum(characters) > 3:
    score += 1

print(f"Password has {str(sum(characters))} different character types")

if score < 4:
    print("Boo, your password is weak!")
elif score == 4:
    print("Your password is so-so")
elif 4 < score < 6:
    print("Your password is decent enough!")
elif score > 6:
    print("Your password is strong!")
