import random
ch ="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_+}{"
le = int(input("Enter password length "))
password=""
for i in range(le+1):
    password += random.choice(ch)
print(password)
