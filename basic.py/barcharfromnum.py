num = [12,3,15,4,67]

print('\nCreat a bar chart using numbers:')

print(f'Index{"Value":>8}  Bar')

for index,value in enumerate(num):
    print(f'{index:>3}{value:>8}  {"$"*value}')