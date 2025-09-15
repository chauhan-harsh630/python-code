with open("sample.txt","w") as file:
    file.write("Hello, World!\n")
    file.write("This is a smaple file. SO what do you want to do with it?\n")


# with open("sample.txt","r") as file:
    # contant = file.read()
    # print(contant + " Now you know how to read and write files in Python!")    

with open("sample.txt", "r") as f:
    print("\n🔹 Reading line by line:")
    for line in f:
        print(line.strip())