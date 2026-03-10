file = open('temp1.txt', 'w')
# file.write('I am the first line!\n')
file.writelines([
  'First line\n',
  'Second line\n',
  'Third line\n'
])

file.close()