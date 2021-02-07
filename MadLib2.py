import re, os
file = input('Please enter name file: ')
readfile = open(file)
rawString = readfile.read()
print([rawString])
readfile.close

reg = re.compile('ADJECTIVE|NOUN|VERB')

while reg.search(rawString) != None:
    search_span = reg.search(rawString).span()

    if rawString[search_span[0]:search_span[1]] == 'ADJECTIVE':
        replacer = input('Enter an adjective: ')
    elif rawString[search_span[0]:search_span[1]] == 'NOUN':
        replacer = input('Enter a noun: ')
    elif rawString[search_span[0]:search_span[1]] == 'VERB':
        replacer = input('Enter a verb: ') 

    rawString = rawString[:search_span[0]] +\
        rawString[search_span[0]:search_span[1]].replace(
        rawString[search_span[0]:search_span[1]], replacer) +\
        rawString[search_span[1]:]

print(rawString)

write_file = open('panda2.txt', 'w')
write_file.write(rawString)
write_file.close()
    
