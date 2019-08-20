# from csv import reader

# with open('fighters.csv') as file:
#     csv_reader = reader(file)
#     headers = next(csv_reader)
#     print(f'Csv headers are {headers}')
#     for row in csv_reader:
#         print(f'{row[0]} from {row[1]} is {row[2]}cm tall')

# from csv import DictReader

# with open('fighters.csv') as file:
#     csv_reader = DictReader(file)
#     for row in csv_reader:
#         print(row['Name'])


# from csv import reader, writer

# with open('fighters.csv') as file:
#     csv_reader = reader(file)
#     next(csv_reader)
#     fighters = list(csv_reader)

# with open('users.csv', 'w') as file:
#     csv_writer = writer(file)
#     csv_writer.writerow(['Id', 'Name', 'Email'])
#     i = 0
#     for fighter in fighters:
#         csv_writer.writerow([i, fighter[0], f'{fighter[0].lower()}@gmail.com'])
#         i += 1

# from csv import DictWriter

# with open('users.csv', 'w') as file:
#     headers = ['id', 'user', 'email']
#     csv_writer = DictWriter(file, fieldnames=headers)
#     csv_writer.writeheader()
#     csv_writer.writerow({
#         'id': 1,
#         'user': 'John',
#         'email': 'john_1@gmail.com'
#     })


# def find_user(f_name, l_name):
#     with open('users.csv') as file:
#         if [f_name, l_name] in file:
#             return file.index([f_name, l_name])
#         return '{} {} not found.'.format(f_name, l_name)



from csv import reader, writer

def update_users(old_fname, old_lname, new_fname, new_lname):
    
    with open('users.csv') as file: 
        csv_reader = reader(file)
        data = list(csv_reader)
        
    count = 0
    for row in data:
        if [old_fname, old_lname] in data:
            data[data.index([old_fname, old_lname])] = [new_fname, new_lname]
            count += 1
            
    with open('users.csv', 'w') as file:
        csv_writer = writer(file)
        for row in data:
            csv_writer.writerow(row)
            
    return 'Users updated: {}.'.format(count)
        

print(update_users("Grace", "Hopper", "Hello", "World")) # Users updated: 1.
print(update_users("Colt", "Steele", "Boba", "Fett")) # Users updated: 2.
print(update_users("Not", "Here", "Still not", "Here")) # Users updated: 0.
