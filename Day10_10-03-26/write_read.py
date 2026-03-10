file = open('temp2.txt', 'w+')
file.writelines([
  'First line\n',
  'Second line\n',
  'Third line\n'
])

## To make the python interpreter to point at a specific index, we use seek(index).
file.seek(0)
print(file.read())

file.close()