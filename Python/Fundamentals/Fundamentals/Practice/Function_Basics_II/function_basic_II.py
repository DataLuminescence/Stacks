
def countdown(num):
    num_list = []
    for x in range(num,-1,-1):
        num_list.append(x)
    return num_list

a = countdown(5)
print(a)


def print_and_return(list):
    print(list[0])
    return list[1]

b = print_and_return([1,2])
print(b)


def first_plus_length(list):
    sum = list[0]
    sum += len(list)
    return sum

c = first_plus_length([1,2,3,4,5])
print(c)


def  values_greater_than_second(list):
    if len(list) < 2:
        return False   
    list2 = []
    for x in range(0, len(list)):
        if list[x] > list[1]:
            list2.append(list[x])
    print(len(list2))
    return list2

d =  values_greater_than_second([5,2,3,2,1,4])
print(d)
e =  values_greater_than_second([3])
print(e)

def length_and_value(size,value):
    list3 = []
    for x in range(0,size):
        list3.append(value)
    return list3

f = length_and_value(4,7)
print(f)
g = length_and_value(6,2)
print(g)