"""response=input("Do you like it?")
likes=response.lower()=="yes"
print(f"like/not: {likes}")
while True:
    try:
        age=int(input("Enter your age: "))
        if age>0:
            break
        else:
            print("age cannot be negative")
    except ValueError:
        print("Enter an integer please!")
print(f"Your age is {age}")
data=input("Enter your name,age (comma seperated): ")
name,age=data.split(",")
age=int(age.strip())
name=name.strip()
print(f"Your namne is {name} & your age is {age}")
fruits=["mango","orange"]
for data in fruits:
    print(data,end=" ")
for i in range (1,11):
    print(i, end=" ")
fruits=["mango","orange","banana"]
for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")
def tname(pname):
    print(f"Hellow {pname}")
    return pname
iname=input("Type your name here: ")
name=tname(iname)
print(name)"""
 


