Student = [
     {
        "Name": "Harsh",
        "Email":"Harsh@gmail.com",
         "Uid":"Harsh-chauhan630"
     },
     {
         "Name": "Riddhi",
        "Email":"riddhi@gmail.com",
         "Uid":"riddhi-sharma930",
     },
     {
         "Name": "Akshay",
         "Email":"akshay@gmail.com",
         "Uid":"akshay-sharma830"
     },

    {
        "Name" :"Riddhi",
        "Email": "riddhi@gmail.com",
        "Uid" :"riddhi-sharma850",
    }

]


search = list(map(lambda x: x["Name"],Student))
search_riddhi =  list(filter(lambda x: x["Name"]=="Riddhi",Student))
uid = list(map(lambda x: x["Uid"],filter(lambda x: x["Name"]=="Riddhi",Student)))
first_riddhi_uid =  next(filter(lambda x: x["Name"]=="Riddhi",Student))["Uid"] 

riddhi_student = list(filter(lambda x: x["Name"]=="Riddhi",Student))
second_riddhi = riddhi_student[1]["Uid"]

print(search)
print(search_riddhi)
print(uid)
print(first_riddhi_uid)
print(second_riddhi)