import random
small=int(input("Enter smaller number:"))
large=int(input("Enter larger number:"))
myNumber=random.randint(small,large)
count=0
while True:
    count+=1
    userNumber=int(input("Enter guess:"))
    if userNumber<myNumber:
        print("Too small! Try again")
    elif userNumber>myNumber:
        print("Too large! Try again")
    else:
        print("Congratulations! You've guessed it in",count,"attempts")
        break
    

        