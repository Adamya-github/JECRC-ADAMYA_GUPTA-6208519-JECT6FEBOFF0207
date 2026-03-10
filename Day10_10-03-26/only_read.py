file = open('temp1.txt', 'r')
# '''
# 1. read(): Display the file content as it is.
# 2. readline(): Display single line of data at a time
# 3. readlines(): Dispaly that how data is stored during write operation
# '''
print(file.read())
file.seek(0)
print(file.readline())
print(file.readline())
print(file.readline())
print(file.readline())  ## empty line

file.seek(0)
print(file.readlines())
file.close()

# file = open('notes.txt', 'r')

# print(file.read())
# file.close()

'''
<module>
    file = open('notes.txt', 'r+')
           ^^^^^^^^^^^^^^^^^^^^^^^
FileNotFoundError: [Errno 2] No such file or directory: 'notes.txt'
'''