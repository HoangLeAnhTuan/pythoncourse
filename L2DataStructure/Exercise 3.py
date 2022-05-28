string = 'Python programming is the best course to learn'


#Part a
print('The length of the string is: ',len(string))

#Part b
print('First five characters of the string is: ',string[:5])

#Part c 
print ('Last ten characters of the string is: ',string[36:46])

#Part d
print ('String after replace \"Python\" into \"DUT\" is: ',string.replace("Python","DUT"))

#Part e
print ('The placement of the \"best\" in string is: ',string.find('best'))

#Part f
print ('Are the characters in the string all uppercase ?',string.isupper())

#Part g
print ('The string after split is: ',string.split(' '))