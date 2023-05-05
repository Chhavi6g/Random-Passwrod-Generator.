#Project: Password Generator 

import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

password = ""
for number_of_char in range(1,nr_letters+1):
    random_char=random.choice(letters)
    password += random_char

for number_of_symb in range(1,nr_symbols+1):
    random_symb=random.choice(symbols)
    password += random_symb

for number_of_num in range(1,nr_numbers+1):
    random_num=random.choice(numbers)
    password += random_num
print(password)

#Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

'''password = ""
for number_of_char in range(1,nr_letters+1):
    random_char=random.choice(letters)
    password += random_char

for number_of_symb in range(1,nr_symbols+1):
    random_symb=random.choice(symbols)
    password += random_symb

for number_of_num in range(1,nr_numbers+1):
    random_num=random.choice(numbers)
    password += random_num
print(password)'''

# To generate pwd in random order we can use this

password_list = []
for number_of_char in range(1,nr_letters+1):
    password_list.append(random.choice(letters))

for number_of_symb in range(1,nr_symbols+1):
    password_list+=random.choice(symbols)

for number_of_num in range(1,nr_numbers+1):
    password_list+=random.choice(numbers)

random.shuffle(password_list)


password = ""
for char in password_list:
    password += char
print(f"Your password is: {password}")


