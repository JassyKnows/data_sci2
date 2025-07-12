# Exo 1
# name = input("Please enter your name :   ").lower()
# age = int(input("Please enter your age :  "))
# year_in_hundred = (2025-age) + 100
# print(f"your age in 100 years will be {year_in_hundred}")

# Exo 2

# import random
# ran_num = random.randint(1,9)
# n = 0
# while True:
#     contin= input("Would you like to continue or exit:    ")
#     if contin == "continue":
#         user_num = int(input("Guess a number between 1 and 9:   "))
#         if user_num > ran_num:
#             print("Too high")
#             n=n+1
#         elif user_num < ran_num:
#             print("Too low")
#             n=n+1
#         else:
#             print("Correct")
#             break
#     else: 
#         break

# print(f"The number of tries is {n}")

# Exo 3
# def ne_list(a):
#     new_list = []
#     new_list.append(a[0])
#     new_list.append(a[-1])
#     return new_list

# print(ne_list([5,10,15,25]))

# Exo 4
import random
lowercase_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j','k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't','u', 'v', 'w', 'x', 'y', 'z']
uppercase_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J','K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T','U', 'V', 'W', 'X', 'Y', 'Z']
digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~']
strong_weak = input("would you like a weak or strong password:    ")
if strong_weak == "weak":
    p1 = "".join(random.choices(lowercase_letters, k=2))
    p2 = "".join(random.choices(uppercase_letters, k=2))
    p3 = "".join(random.choices(digits, k=2))
    p4 = "".join(random.choices(symbols, k=2))
    password_pre = p1 + p2 + p3 + p4
    p_list = list(password_pre)
    random.shuffle(p_list)
    password = "".join(p_list)
    print(f"Your password is {password}")
if strong_weak == "strong":
    p1 = "".join(random.choices(lowercase_letters, k=4))
    p2 = "".join(random.choices(uppercase_letters, k=4))
    p3 = "".join(random.choices(digits, k=4))
    p4 = "".join(random.choices(symbols, k=4))
    password_pre = p1 + p2 + p3 + p4
    p_list = list(password_pre)
    random.shuffle(p_list)
    password = "".join(p_list)
    print(f"Your password is {password}")




    














