"""
#write a python program to developing a simple student information management module 
#create a student class  and that include attributes such as name ,roll number,and branch add amethod display_deatails() to print student information
class Student:
    def __init__(self, name, roll_number, branch):
        self.name =name
        self.roll_number = roll_number
        self.branch = branch

    def display_deatils(self):
        print(f"Student Name: {self.name}")
        print(f"Roll Number: {self.roll_number}")
        print(f"Branch: {self.branch}")
student1 = Student("Anu", "101", "Computer Science")
student1.display_deatils()
student2 = Student("Ravi", "102", "Mechanical Engineering")
student2.display_deatils()
student3 = Student("Maya", "103", "Electrical Engineering")
student3.display_deatils()


#TASK 2
#write a python program to utility function to display multiples of a given number.generate a function that prints the first 10 multiples of a given number using a loop.
def display_multiples(number):
    print(f"First 10 multiples of {number}:")
    for i in range(1, 11):
        multiple = number * i
        print(multiple)
display_multiples(5)


#TASK 3
# write a python program to uilding a basic classification system based on age.using  nested if-elif-else conditional statements to classify age groups (e.g., child, teenager, adult, senior).
def classify_age(age):
    if age < 0:
        return "Invalid age"
    elif age <= 12:
        return "Child"
    elif age <= 19:
        return "Teenager"
    elif age <= 59:
        return "Adult"
    else:
        return "Senior"
age = 25
age_group = classify_age(age)
print(f"Age: {age}, Age Group: {age_group}")
age = 70
age_group = classify_age(age)
print(f"Age: {age}, Age Group: {age_group}") """

#TASK 4
#write a python program to calculate the sum of the first n natural numbers by using a  sum_to_n() function using a for loop.
def sum_to_n(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total
n = 10
result = sum_to_n(n)
print(f"Sum of first {n} natural numbers: {result}")
n = 20
result = sum_to_n(n)
print(f"Sum of first {n} natural numbers: {result}") 

#TASK 5
#write a program to designing a basic banking application. by creating aa Bank Account class with methods such as deposit(), withdraw(), and check_balance().
class BankAccount:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New balance: {self.balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"Withdrew {amount}. New balance: {self.balance}")
            else:
                print("Insufficient funds.")
        else:
            print("Withdrawal amount must be positive.")

    def check_balance(self):
        print(f"Current balance: {self.balance}")
account = BankAccount("John Doe", 1000)
account.check_balance()
account.deposit(500)
account.withdraw(200)
account.check_balance()
account.withdraw(1500)  


# wri