# character_name = "John"
# character_age = "35"
# is_male = True
#
# print("John is\n35 years old")
# print(character_name + " is " + character_age + " years old")
#
# phrase = "Trail Boss"
# print(phrase)
# print(phrase + " is cool")
# print(phrase.lower())
# print(phrase.isupper())
# print(len(phrase))
# print(phrase[2])
# print(phrase.index("a"))
# print(phrase.replace("a", "Z"))
# phrase2 = phrase.replace("a", "Z")
# print(phrase2)
# print(-2.0987)
#
# print(3 * 4 + 8)
# print(3 * (4 + 8))
# print(10 % 3)
# my_num = -5
# print(my_num)
# print(phrase + " " + str(my_num))
# print(abs(my_num))
# print(pow(5, 3))
# print(max(5, 2))
# print(min(5, 2))
# print(round(4.5))
#
# from math import *
# print(ceil(3.7))
# print(floor(3.7))
# print(sqrt(36))
#
# name = input("Enter your name: ")
# age = input("Enter your age: ")
# print("Hello " + name + "! You are " + age)

# num1 = input("Enter a number: ")
# num2 = input("Enter another number: ")
# result = float(num1) + int(num2)
#
# print(result)
#
# color1 = "Red"
# color2 = "Blue"
#
# print("Roses are red")
# print("violets are blue")
# print(f'{color1} roses')
# print(f'violets are {color2.lower()}')

# friends = ["Josh", "Craig"]
# friends2 = ["James", "Pete", "Cam"]
#
# print(friends)
# print(friends[1])
# print(friends[-1])
# print(friends[0:2])
# friends.extend(friends2)
# print(friends)
# friends.append("Jake")
# print(friends)
#
# name = 'world'
# program ='python'
# print('Hello %s! This is %s.'%(name, program))
#
#
# name = 'world'
# print('Hello, {}'.format(name))

# a_dict = {'color': 'blue', 'fruit': 'apple', 'pet': 'dog'}
# # d_items = a_dict.items()

# for item in a_dict.items():
#     print(item)
#     print(type(item))

# for key in a_dict.keys():
#     print(key)

# prices = {'apple': 0.40, 'orange': 0.35, 'banana': 0.25}
# for k, v in prices.items():
#     prices[k] = round(v * 0.9, 2)


# print("TEST")

# class Student:

#     def __init__(self, name, major, gpa, is_on_probation):
#         self.name = name
#         self.major = major
#         self.gpa = gpa
#         self.is_on_probation = is_on_probation

# student1 = Student("Jim", "Econ", 3.3, False)
# student2 = Student("John", "Econ", 5.1, False)

# print(student1.name)
# print(student2.name, student2.gpa)

from Question import Question

question_prompts = [
    "What color are apples?\n(a) Red/Green\n(b) Magenta\n(c) Orange\n\n",
    "What color are oranges?\n(a) Red/Green\n(b) Magenta\n(c) Orange\n\n",
    "What color are strawberries?\n(a) Red/Green\n(b) Magenta\n(c) Orange\n\n"
]

qs = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "c"),
    Question(question_prompts[2], "a")
]


def run_test(questions):
    score = 0
    for question in qs:
        ans = input(question.prompt)
        if ans == question.ans:
            score += 1
    print(f'You got {str(score)}' + "/" + str(len(qs)) + " correct")


run_test(qs)
