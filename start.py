import random
n=10
a=0
forCount=1
for i in range(1,n):
    forCount+=1
    a+=1
print("A:{}\nForCount={}".format(a,forCount))

list = [i**2 for i in range(0, 6)]
print(list)
random_list = [random.randint(0,10) for i in range(0,10)]
print(random_list)