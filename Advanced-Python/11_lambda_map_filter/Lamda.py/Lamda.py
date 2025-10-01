# Lambda in Python is basically a way to create small, anonymous functions (functions without a name) in a single line.

# lambda → keyword

# arguments → input parameters (like in normal functions)

# expression → a single expression whose result will be returned

# lambda arguments: expression


add =  lambda x,y:x+y

print(add(5,4))


nums = [3,2,4,5,6,1]

sortes_nums = sorted(nums)
print(sortes_nums)

# Used with map(),fillter(),reduce()

num = [1,2,3,4,5,6]
s= list(map(lambda x: x**2,num))
print(s)

evens = list(filter(lambda x: x%2==0,num))
print(evens)
