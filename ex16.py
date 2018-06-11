from sys import argv

script, filename = argv

print(f'Erasing {filename}')
input('Confim?')

target = open(filename, 'w')

target.truncate()

line1 = input('Line 1:')
line2 = input('Line 2:')
line3 = input('Line 3:')

print('Writing lines to file')

target.write(line1 + '\n' + line2 + '\n' + line3 + '\n')

target.close()