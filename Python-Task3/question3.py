#Printing numbers from 1 to 0 except 7 and 3 using for and while loop

#using for loop

#defining function using for loop to the numbers
def usingForloop():
    for index in range(1,11):
        if(index == 3 or index == 7):
            continue
        else:
            print(index )
    
#using while loop

#defining function using for while to the numbers
def usingWhileloop() :    
    number=1
    while(number != 11):
        if(number == 3 or number == 7):
            number += 1
        else:
            print(number )
            number += 1

print("Printing numbers from 1 to 0 except 7 and 3")
print("Using For Loop: ")
usingForloop()
print("Using While Loop: ")
usingWhileloop()
