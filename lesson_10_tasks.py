# # def add_two_numbers(a,b):
# #     print(a+b)
# # add_two_numbers(2,5)
# # add_two_numbers(154,13)
# # add_two_numbers(9,648)
# def say_labas():
#     print('Labas')
# say_labas()

# def add_two_num(a:str,b:str) -> str:
#     return a+b
# nr_sum =add_two_num("2","5")
# print(nr_sum)

# # # Create a function that takes string as parameter and returns number of letters from that string.
# def counting_letters(my_string:str) -> int:
#     return sum(1 for char in my_string if char not in "!@#$%^&*(),-_=+[]{}|:'\".<>?0123456789/" and char != " ")
# # print(counting_letters("This, is a string"))

# def get_squared(a:int) -> int:
#     return a**2
# def make_a_string(b:str, c:int) -> str:
#     return b +str(get_squared(c))
# print(make_a_string("salut", 5))

# def make_a_list(a:str, b:int) -> list:
#     return [a,b]
# print(make_a_list("salut", 5))

# def count_spaces_in_a_string(string:str) -> int:
#     return sum(1 for char in string if char == " ")
# print("Amount of spaces is: ", count_spaces_in_a_string("Va cia tai tikrai daugybe tarpu yra as manau"))  

# def arrange_string(string: str) -> str:
#     return ''.join(sorted(string.lower())).strip()
# print("Your sorted string is:", arrange_string("Va cia tai kose makalose turetu pasidaryt"))

# def palindrome_checker(string:str) -> bool:
#     return string == string[::-1]
# print(palindrome_checker("sedek uzu kedes"))

# def is_egg_boiled(minutes:int) -> str:
#     if minutes <5:
#         return "Eggs are not yet ready"
#     elif minutes <10:
#         return "Bon appetit, eggs are ready to eat!"
#     else:
#         return "What the hell, dude"
# print(is_egg_boiled(25))

# Create a function that adds a string ending to each member in a list.
# def add_ending(my_list:list)->list:
#     return [str(part)+"GotStringed" for part in my_list]
# print(add_ending([5, "Septyniolika", 984, "kintamasis"]))

# from typing import Union

# def pick_your_type(number:int) -> Union[str,bool]:
#     if number >=500:
#         return "You rule bro, thats a high number!"
#     else:
#         return False
# print(pick_your_type(756))

# Create a mini python program which would take two numbers as an input and would return their sum, subtraction, division, multiplication.
# It was told, that function should only do ONE thing, so:
a = float(input("Please provide me with your first number: "))
b = float(input("Please provide me with another number: "))
def adding_nums(a:float,b:float) -> str:
    return "sum is equal to: "+ str(a+b)
def substracting_nums(a:float,b:float) -> str:
    return "Difference is equal to: "+ str(a-b)
def dividing_nums(a:float,b:float) -> str:
    return "Division is equal to: " +str(a/b)
def multiplying_nums(a:float,b:float) -> str:
    return "Multiplication is equal to: " +str(a*b)
list_of_functions =[adding_nums, substracting_nums, dividing_nums, multiplying_nums]
print([function(a,b) for function in list_of_functions])