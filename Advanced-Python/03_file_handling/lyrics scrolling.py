import time

with open("E:/python-code-1/Advanced-Python/03_file_handling/song.txt","r",encoding="utf-8") as file:
     for line in file:
        for char in line.strip(): 
            print(char, end="", flush=True)
            time.sleep(0.05)  
        print() 
        time.sleep(0.5)  
