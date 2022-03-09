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


# #11 Prediction: We will print 500 before the function begins. The function has not yet been called so we will ignore the
# next 3 lines and print b with a value of 500 once more. Then we call the function which creates a local variable of b 
# and gives it a value of 300. b will then be printed with this value. Then we use the value of b outside the function
# to print be as 500 once more
# b = 500
# print(b)
# def foobar():
#     b = 300
#     print(b)
# print(b)
# foobar()
# print(b)


# #12 Prediction: We will print 500 before the function begins. The function has not yet been called so we will ignore the
# next 4 lines and print b with a value of 500 once more. Then we call the function which creates a local variable of b 
# and gives it a value of 300. Function returns a value of 300 for b but does not set it equal to b variable outside 
# function. Therefore when b prints againt we print 500 one more time.
# b = 500
# print(b)
# def foobar():
#     b = 300
#     print(b)
#     return b
# print(b)
# foobar()
# print(b)


#13 Prediction: We will print 500 before the function begins. The function has not yet been called so we will ignore the
# next 4 lines and print b with a value of 500 once more. The variable b is printed out one more time with a value of 500.
# Then we call the function which creates a local variable of b and gives it a value of 300. This value is printed out 
# from within the function  Then we set b equal to the returned value of the function (300). We print b with a value of 
# 300. 
# b = 500
# print(b)
# def foobar():
#     b = 300
#     print(b)
#     return b
# print(b)
# b=foobar()
# print(b)


#14 Prediction: We call foo function and print 1 then call bar which prints 3 then foo resumes printing 2
# def foo():
#     print(1)
#     bar()
#     print(2)
# def bar():
#     print(3)
# foo()


#15 Prediction: Call foo function to set y to the return value of function. Print 1, then call bar function 
# when setting x to return value of bar. Print 3. Print 5. Print 10.
def foo():
    print(1)
    x = bar()
    print(x)
    return 10
def bar():
    print(3)
    return 5
y = foo()
print(y)