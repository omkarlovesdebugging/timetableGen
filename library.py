import random 
list = [ "omkar","Sudhir","gholap","Chotu"]

for i in list :
    random.shuffle(list)
    if i=="gholap":
        i="omkar"
    print(i)
