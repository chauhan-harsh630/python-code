f =open("E:\\python-code-1\\Advanced-Python\\12_context_managers\\data.txt","r")
try:   
 content = f.read()
finally:
  f.close()


with open("E:\\python-code-1\\Advanced-Python\\12_context_managers\\data.txt", "r") as f:
    content = f.read()
    print(content)
