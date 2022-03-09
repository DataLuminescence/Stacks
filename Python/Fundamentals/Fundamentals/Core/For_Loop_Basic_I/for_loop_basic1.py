def basic():
    for x in range(0,151):
        print(x)

def multiples_of_five():
    for x in range(0,1001,5):
        print(x)

def counting_the_dojo_way():
    for x in range(1,101):
        if(x%5 == 0):
            print("Coding")

        if(x%10 == 0):
            print("Coding Dojo")
        else:
            print(x)

def whoa_that_sucker_huge():
    sum = 0
    for x in range(1,500000,2):
        sum += x
    print(sum)

def countdown_byfours():
    for x in range(2018,0,-4):
        if(x > 0):
            print(x)

def flexible_counter(lowNum, highNum, mult):
    lowNum
    highNum 
    mult
    for x in range(lowNum,highNum+1):
        if(x%mult == 0):
            print(x)

basic()
multiples_of_five()
counting_the_dojo_way()
whoa_that_sucker_huge()
countdown_byfours()
flexible_counter(2, 9, 3)