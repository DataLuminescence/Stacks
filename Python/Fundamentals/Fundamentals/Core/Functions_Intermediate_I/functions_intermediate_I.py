x = [ [5,2,3], [10,8,9] ] 

# x[1][0] = 15
# print(x)

########################################################################################################################

students1 = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]

# students1[0]['last_name'] = 'Bryant'
# print(students1)

########################################################################################################################

sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}

# sports_directory['soccer'][1] = 'Andres'
# print(sports_directory)

########################################################################################################################

z = [ {'x': 10, 'y': 20} ]

z[0]['y'] = 30
print(z)



students2 = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

def iterateDictionary(students2):
    for i in students2:
        for j in students2-1:
            print(students2[x],"-"
    
    
    
    return

iterateDictionary(students2) 
# should output: (it's okay if each key-value pair ends up on 2 separate lines;
# bonus to get them to appear exactly as below!)
# first_name - Michael, last_name - Jordan
# first_name - John, last_name - Rosales
# first_name - Mark, last_name - Guillen
# first_name - KB, last_name - Tonel
