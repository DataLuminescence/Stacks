num1 = 42 #Integer variable declaration
num2 = 2.3 #Float variable declaration
boolean = True #Boolean variable declaration
string = 'Hello World' #String variable declaration
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] #List variable declaration
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} #Dictionary variable declaraton
fruit = ('blueberry', 'strawberry', 'banana') #Tuple variable declaration
print(type(fruit)) #Log statement, type check
print(pizza_toppings[1]) #Log statement, list,  access value
pizza_toppings.append('Mushrooms') #List, add value
print(person['name']) #Log statement, dictionary, access value
person['name'] = 'George' #Dictionary Change value
person['eye_color'] = 'blue' #Dictionary Add Value
print(fruit[2]) #Log statement, tuple, access value

if num1 > 45: #Conditional, if
    print("It's greater") #Log statement
else: #Conditional, else
    print("It's lower") #Log statement

if len(string) < 5: #Conditional, if, length check
    print("It's a short word!") #Log statement
elif len(string) > 15: #Conditional, else if, length check
    print("It's a long word!") #Log statement
else: #Conditional, else
    print("Just right!") #Log statement

for x in range(5): #For loop, integer variable declaration, stop
    print(x) #Log statement
for x in range(2,5): #For loop, integer variable declaration, start, stop
    print(x) #Log statement
for x in range(2,10,3): #For loop, integer variable declaration, start, stop, increment
    print(x) #Log statement
x = 0 #Integer variable declaration
while(x < 5): #While loop, integer variable declaration, stop
    print(x) #Log statement
    x += 1 #Increment

pizza_toppings.pop() #List delete value at end of list
pizza_toppings.pop(1) #List delete value at index 1

print(person) #Log statement prints dictionary
person.pop('eye_color') #Dictionary, delete value 'eye color'
print(person) #Log statement prints dictionary

for topping in pizza_toppings: #For loop, integer variable declaration, stop, iterate through list
    if topping == 'Pepperoni': #Conditional, if
        continue #Send user back to start of the loop
    print('After 1st if statement') #Log statement
    if topping == 'Olives': #Conditional, if
        break #Exits the loop

def print_hello_ten_times(): #Function declaration
    for num in range(10): #For loop, integer variable declaration, stop
        print('Hello') #Log statement

print_hello_ten_times() #Function call

def print_hello_x_times(x): #Function declaration, pass argument
    for num in range(x): #For loop, integer variable declaration, stop, pass argument
        print('Hello') #Log statement

print_hello_x_times(4) #Function call, parameter

def print_hello_x_or_ten_times(x = 10): #Function declaration, pass argument, integer variable declaration
    for num in range(x): #For loop, integer variable declaration, stop, pass argument
        print('Hello') #Log statement

print_hello_x_or_ten_times() #Function call
print_hello_x_or_ten_times(4) #Function call, parameter


"""
Bonus section
"""

# print(num3) #NameError: name <variable name> is not defined
# num3 = 72 #Integer variable declaration
# fruit[0] = 'cranberry' #TypeError: 'tuple' object does not support item assignment
# print(person['favorite_team']) #KeyError: 'favorite_team'
# print(pizza_toppings[7]) #IndexError: list index out of range
#   print(boolean) #IndentationError: unexpected indent
# fruit.append('raspberry') #AttributeError: 'tuple' object has no attribute 'append'
# fruit.pop(1) #AttributeError: 'tuple' object has no attribute 'pop'