name=input("Enter your name here: ")
myfile=open ("name.txt", "w")
myfile.write(name)
myfile.close()