# with open("sample.txt","w") as file:
    # file.write("Hello, World!\n")
    # file.write("This is a smaple file. SO what do you want to do with it?\n")


# with open("sample.txt","r") as file:
    # contant = file.read()
    # print(contant + " Now you know how to read and write files in Python!")    

# with open("E:/python-code-1/Advanced Python/03_file_handling/hello.txt", "r") as f:
    # print("\n🔹 Reading line by line:")
    # for line in f:
        # print(line.strip())


# from greet import hello_fun,add

# contant = hello_fun()
# print(contant)

# from greet import add

# 


# 


import json

data = {"username": "Karan", "email": "Karan@gmail.com","student":True}

with open("json_file","w") as file:
    json.dump(data,file,indent=4)


with open("json_file","r") as f:
    user = json.load(f)
    print(user["username"])