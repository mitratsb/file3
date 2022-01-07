# cinema age range and tickets cost

print("how old are you?")

age= int(input())

if 2<age  and age<8:
    print("please pay 2 dollars")
elif age>=65 :
    print("please pay 5 dollars")

else:
    print("please pay 10 dollars")

print("---------------")

#روش دوم

if (0<=age and age<=2) or (8<=age and age<65):
    print ("10 dollars")
elif age>2 and age<8 :
    print ("2 dollars")
else:
    print ("5 dollars")
