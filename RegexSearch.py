import os, re

path_for_files = input('Enter path: ')
found_files = os.listdir(path_for_files)
print(found_files)

reg_in = input('Enter an regular expression: ')
reg = re.compile(reg_in)

for files in found_files:
    open_file = open(path_for_files + '\\' + files)
    read_files = open_file.read()
    found_reg = reg.findall(read_files)
    print(files, '=>', found_reg)
    open_file.close()

