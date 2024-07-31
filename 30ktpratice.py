#dictionary
#creating

dictionary = {}

#adding 

phonebook = ({'Namratha': '790692902', 'jadhav' : '7389339190', 'kadam': '2831131929'})
print(phonebook)

#cessing values 
print(phonebook['Namratha'])
print(phonebook.get('sonu'))

# updating 
phonebook["jadhav"] = "555666888"
print(phonebook)

phonebook["Namratha"] = 'sonu'
print(phonebook)

#deleting
menu_iteam = ('sandwhich','pasta','salad','maggie')
my_list = list(menu_iteam)
del my_list[2]
new_list = tuple(my_list)
print(new_list)

#length()
my_dict = {'a':1, 'b':2, 'c':3}
length = len(my_dict)
print(length)

#pop
subjects = {'hindi':30,'telugu':40,'english':50}
print(subjects.pop('telugu'))
print(subjects)

#popiteam 
print(subjects.popitem())

#keys
print(subjects.keys())

#values
print(subjects.values())


#iteams

phonebook = ({'Namratha': '790692902', 'jadhav' : '7389339190', 'kadam': '2831131929'})
for iteam in phonebook.items():
    print(iteam)
    print(phonebook.items())

#copy

school = subjects.copy()
print(school)
school["telugu"] = "H.V.S"

#update
