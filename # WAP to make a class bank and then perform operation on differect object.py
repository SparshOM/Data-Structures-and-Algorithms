# WAP to make a class bank and then perform operation on differect objects (deposit,withdraw)
class Bank():
    """ Performing transactions """

    # to initialize the account
    def _init_(self,name,phonenumber,balance = 0.0):
        self.name = name
        self.phonenumber = phonenumber
        self.balance = balance
    
    # to deposit the money 
    def deposit(self,amount):
        self.balance += amount
        return self.balance
            
    # to withdraw money from account
    def withdraw(self,amount):
        if amount > self.balance:
            print("Bhaiya paisa nhi hai account me")
        else:
            self.balance-=amount
        return self.balance
    
name = input("enter your name: ")
phnum = input("enter your phone number ")
b = Bank(name,phnum)
print("Enter d for deposit\nEnter w for withdraw\nEnter e to exit ")
while(True):
    
    choice = input("Enter your choice ")
    if choice == 'e' or choice == 'E':
        break
    elif choice == 'd' or choice =='D':
        amt = float(input("Enter amount that you want to deposit "))
        print("\tbalance after deposit :",b.deposit(amt))   
    elif choice == 'w' or choice =='W':
        amt = float(input("Enter amount that you want to withdraw "))
        print("\tbalance after withdraw :",b.withdraw(amt))   
    else:
        print("\tWrong choice try again")