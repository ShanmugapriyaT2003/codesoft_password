import random
num=int(input("enter the number"))
v="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%"
password=''.join(random.sample(v,num))
print(password)
