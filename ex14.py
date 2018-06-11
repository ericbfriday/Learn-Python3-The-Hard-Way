from sys import argv
script, user_name = argv
prompt = '> '

print(f'Hi {user_name}, I\'m the {script} script')
print('I am here to ask you a few questions.')
print(f'Do you like me, {user_name}?')
likes = input(prompt)

print(f'Where do you live, {user_name}?')
location = input(prompt)

print(f'What kind of computer do you have?')
computer = input(prompt)

print(f'''
So you said that you like me? {likes}
You live in {location}.
and you own a {computer}.
''')
