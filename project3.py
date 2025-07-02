import random
password=""
letters=["a","b","c","d","e","f","g","h","i","j","k","l","m",
         "n","o","p","q","r","s","t","u","v","w","x","y","z"]
symbols=["!","@","#","$","%","^","&","*","(",")","-","_",
         "+","=","{","}","[","]","|",":",";","'",'"',"<",">","?"]
numbers=["0","1","2","3","4","5","6","7","8","9"]
selection_of_letters=int(input("How many letters would you like in your password? "))
selection_of_symbols=int(input("How many symbols would you like in your password? "))
selection_of_numbers=int(input("How many numbers would you like in your password? "))
for i in range(0,selection_of_letters):
    password+=random.choice(letters)
for j in range(0,selection_of_symbols):
    password+=random.choice(symbols)
for k in range(0,selection_of_numbers):
    password+=random.choice(numbers)

user=input("Do you want to make it a strong password? (yes/no): ").lower()
if (user == "yes"):
    strong_password=list(password)
    random.shuffle(strong_password)
    strong_password="".join(strong_password)
    print("Strong password is: ",strong_password)
else:
    print("Simple password is: ",password)
# Note: The code above generates a simple password based on user input for letters, symbols, and numbers,