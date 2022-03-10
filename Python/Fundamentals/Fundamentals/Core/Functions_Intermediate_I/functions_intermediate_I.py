x = [ [5,2,3], [10,8,9] ] 

x[1][0] = 15
print(x)

########################################################################################################################

students1 = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]

students1[0]['last_name'] = 'Bryant'
print(students1)

########################################################################################################################

sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}

sports_directory['soccer'][1] = 'Andres'
print(sports_directory)

########################################################################################################################

z = [ {'x': 10, 'y': 20} ]

z[0]['y'] = 30
print(z)

########################################################################################################################

students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

def iterateDictionary(some_list):
    for dict in some_list: #Dict 1-4 in students list
        tempstring = "" #Store values as a string 
        for i,key in enumerate(dict): #For every dictionary I will assign keys to every key starting at 0
            tempstring += f"{key} - {dict[key]}" #We concatenate the key and the value at that key for all keys and values of dict
            if i < len(dict)-1: #We concetenate a , at the end of every 0th value ex Micheal,
                tempstring += ", "
        print(tempstring)

iterateDictionary(students) 

def iterateDictionary2(key_name, some_list):
    for dict in some_list:
        tempstring = ""
        for i,key in enumerate(dict):
            if(key == key_name):
                tempstring += f"{dict[key]}"
        print(tempstring)

iterateDictionary2('first_name', students)

iterateDictionary2('last_name', students)

dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfo(some_dict):
    for some_list in some_dict:
        print()
        print(len(some_dict[some_list]), str(some_list).upper() ) 
        for x in some_dict[some_list]:
            print(x)

printInfo(dojo)
