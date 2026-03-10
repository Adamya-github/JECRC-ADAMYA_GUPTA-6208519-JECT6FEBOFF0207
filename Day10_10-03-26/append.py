file = open('jecrc.txt', 'a+')

# file.write('JECRC is a very .............\n')
# file.write('JECRC is also ***********\n')
file.writelines([
  '\nHere, food is ------\n',
  'Eco system is _____\n',
  'Faculties are very .........\n'
])
file.seek(0)
print(file.read())

file.close()