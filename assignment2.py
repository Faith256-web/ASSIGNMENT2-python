# The volume of a sphere with radius r is (4/3)* pie * r**2.
# What is the volume of the sphere with radius 5.
# Make sure the program enters the radius from the keyboard and provide the answer in 2 decimal places.
radius=(input("enter the radius of the sphere"))
volume=(4/3) * pie * (radius**3)
print(f"the volume of the sphere with radius {radius} is {volume:.2}")

# Create a program to calculate the area of the triangle (1/2 *base * height).
#Base and height should be entered using a keyboard.
base=float(input("enter the base of the triangle:"))
height=float(input("enter the height of the triangle:"))
area_of_the_triangle=(1/2 * base * height)
print(f"the area of the triangle")


# Question One
# WITI has tasked you to automate a simple grading system.
# As a python student, write a program using to display the grades that
# the students will be recieving based on the mark scored in a subject.
# 90% - 100%  Grade is A
# 80% - 89%   Grade is B
# 70% - 79%   Grade is C
# 60% - 69%   Grade is D
# 50% - 59%   Grade is E
# < 50% Fail
percentage=int(input("enter the students score: "))
if 90 <= percentage <= 100 :
    print("A")
elif 80 <= percentage < 90 :
    print("B")    
elif 70 <= percentage < 80 :
    print("C")    
elif 60 <= percentage < 70 :
    print("D")  
elif 50 <= percentage < 60 :
    print("E")
else:
    print("Fail")  

# WITI Academy is proposing a sacco to help students save their money.
# Design a platform that will do the following.
# Welcome to , WITI Academy Sacco.
# 1. Deposit Money
# 2. Withdraw Money
# 3. Check Balance
# Ensure if the student selects 1, money is deposited and the minimum deposit should be 1000.
# If the student selects 2, money should be withdrawn and a minimum withdrawal is 500.
# If the studentselects 3, the account balance should be  displayed.
initial_balance = 0
print("welcome to witi academy sacco")
print("1 deposit money")
print("2 withdraw money")
print("3 check balance")
choice= input("select option 1,2,3,4")
if choice == "1":
    amount= float(input("enter the amount of deposit"))
    if amount >= 1000:
        initial_balance += amount
        print(f"successfully withdrew {amount}. new balance is {initial_balance}")
    else:
        print("minimum deposit is 1000")
elif choice == "2":
     amount = int(input("enter amount to withdraw"))
     if amount >= 500:
        if initial_balance >= amount:
            initial_balance -= amount
            print(f"successfully withdrew {amount}. new balance is {initial_balance}")
        else:
         print("insufficient balance") 
     else:
        print("minimum withdraw")
elif choice == 3:
  print(f"current balance is {initial_balance}.")
else:
     print("invalid request")

 
          