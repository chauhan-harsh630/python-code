class File:

    def __init__(self,filename,methode):
        self.filename = filename
        self.methode = methode

    def __enter__(self):
        print("Enter..")
        self.file  = open(self.filename,self.methode)
        return self.file
    
    def __exit__(self,type,value,traceback):
        print("Exit")
        self.file.close()
        if "r"  in self.methode or "+" in self.methode:
            with open(self.filename,'r') as f:
                print("Final content: ",f.read())



with File("file.txt",'w+') as f:
    f.write("Good evening!")
    f.seek(0)
    data =f.read()
    print("Inside block: ",data)
