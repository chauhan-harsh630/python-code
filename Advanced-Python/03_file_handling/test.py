# X = [10 , 20 , 30]
# Y=X
# print(Y[0])

# Y[2] = 10
# for i in X:
    # print([i])
# 
import sys
A = 10
B = 20
print(hex(id(A)))
print("Size of A is ", sys.getsizeof(A) , "bytes")
print(hex(id(B)))

l1= [1,2,3]  
l2 = l1
l1[0] = 33
l2 = [10,20,30] # becuse list is mutable
# that is why it is changing
print(l1)
print(l2)


# with open("./hello.txt","w") as file:
    #   file.write("Hello my name is Harsh ")
    #   file.write("What about you")



# with open("E:/python-code-1/Advanced Python/03_file_handling/hello.txt","r") as file:
#      content =  file.read()
#      print(content)



