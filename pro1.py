import string
import random
a=list(string.ascii_lowercase)
b=list(string.ascii_uppercase)
c=list(string.digits)
d=list(string.punctuation)
user=input("Total characters in the password:")
while True:
    try:
        num=int(user)
        if num < 8:
            print("your password should be atleast 8.")
            user=input("Please,Enter your number again:")
        else:
            break
    except:
        print ("Please,Enter numbers only.")
        user=input("How many characters do you want in your password?")
random.shuffle(a)
random.shuffle(b)
random.shuffle(c)
random.shuffle(d)
x=round(num *(30/100))
y=round(num*(20/100))
result=[]
for i in range(x):
    result.append(a[i])
    result.append(b[i])
for i in range(y):
    result.append(c[i])
    result.append(d[i])
random.shuffle(result)
password="".join(result)
print("strong Password:",password)
