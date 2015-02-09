__author__ = 'Pedram'
from Crypto.Hash import SHA256

print("Provide username and password pairs for input")
user = input()
password = input()
dict = {}


while (user != "" and password != ""):
    dict[user] = SHA256.new(str.encode(password)).hexdigest()
    user = input()
    password = input()

print("Provide username and password pairs for checking")
user = input()
password = input()
while (user != "" and password != ""):
    if user not in dict: print("user not found")
    elif dict[user] == SHA256.new(str.encode(password)).hexdigest(): print("login succeeds")
    else: print ("login fails")
    user = input()
    password = input()



