prime = int(input("The the number "))
for num in range (2,prime+1):
    for nu in range(2,num):
        if num%nu ==0:
            print("it is not prime",num)
            break
    else:
        print("prime",num)

