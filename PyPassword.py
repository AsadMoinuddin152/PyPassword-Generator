#Password Generator Project
import random
#variable sections
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

#Input section
print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#creating the password from the given the data
passowrd_list = []
for num in range (1, nr_letters+1):
  passowrd_list += random.choice(letters)

for num in range (1, nr_symbols+1):
  passowrd_list += random.choice(symbols)

for num in range (1, nr_numbers+1):
  passowrd_list += random.choice(numbers)

#shuffling the the password list to create a strong passowrd
random.shuffle(passowrd_list)

#concatenate the password
password = ""
for char in passowrd_list:
  password += char

#printing the Final password
print(f"Your New password is {password}.\nThank you for using the PyPassword Generator.")
