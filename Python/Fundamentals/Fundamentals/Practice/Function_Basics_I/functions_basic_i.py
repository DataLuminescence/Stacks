#1 Prediction: The function will print out the number 5
# def number_of_food_groups():
#     return 5
# print(number_of_food_groups())

#2 Prediction: The function will throw an error because we are not passing arguments for b, and c in the first function
# def number_of_military_branches():
#     b=0
#     c=1
#     return 5
# print(number_of_days_in_a_week_silicon_or_triangle_sides() + number_of_military_branches())

#3 Prediction: The function will print out the number 5
# def number_of_books_on_hold():
#     return 5
#     return 10
# print(number_of_books_on_hold())

#4 Prediction: The function will print out the number 5
# def number_of_fingers():
#     return 5
#     print(10)
# print(number_of_fingers())

#5 Prediction: The function will print out the number 5. No return statement so x has a value of none
# def number_of_great_lakes():
#     print(5)
# x = number_of_great_lakes()
# print(x)

#6 Prediction: The function will call itself once to print 1+2 and again to print 2+3. However, with no return statement.
# the print statement will throw an error since the functions have no value.
# def add(b,c):
#     print(b+c)
# print(add(1,2) + add(2,3))

#7 Prediction: The function will return the string value of 25 after parsing the arguments of b and c
# def concatenate(b,c):
#     return str(b)+str(c)
# print(concatenate(2,5))

#8 Prediction: The function will print 100. Then print 10 after not meeting the conditional statement of b < 10
# def number_of_oceans_or_fingers_or_continents():
#     b = 100
#     print(b)
#     if b < 10:
#         return 5
#     else:
#         return 10
#     return 7
# print(number_of_oceans_or_fingers_or_continents())


#9 Prediction: The function will print 7 after the conditional statement is met and 7 is returned. Then it will print 14
# after the conditional statement is not met and 14 is returned. Then it will call the function two more times and add 
# their returns of 7 and 14, thus printing 21
# def number_of_days_in_a_week_silicon_or_triangle_sides(b,c):
#     if b<c:
#         return 7
#     else:
#         return 14
#     return 3
# print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3))
# print(number_of_days_in_a_week_silicon_or_triangle_sides(5,3))
# print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3) + number_of_days_in_a_week_silicon_or_triangle_sides(5,3))


#10 Prediction: The function will take 3, and 5 as arguments and return their sum of 8 to print
# def addition(b,c):
#     return b+c
#     return 10
# print(addition(3,5))


# #11
b = 500
print(b)
def foobar():
    b = 300
    print(b)
print(b)
foobar()
print(b)


# #12
# b = 500
# print(b)
# def foobar():
#     b = 300
#     print(b)
#     return b
# print(b)
# foobar()
# print(b)


# #13
# b = 500
# print(b)
# def foobar():
#     b = 300
#     print(b)
#     return b
# print(b)
# b=foobar()
# print(b)


# #14
# def foo():
#     print(1)
#     bar()
#     print(2)
# def bar():
#     print(3)
# foo()


# #15
# def foo():
#     print(1)
#     x = bar()
#     print(x)
#     return 10
# def bar():
#     print(3)
#     return 5
# y = foo()
# print(y)