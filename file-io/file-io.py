# def statistics(file):
#     with open(file) as f:
#         data = f.read()
#     stats = {
#         'lines': len(data.split('\n')),
#         'words': len(data.split()),
#         'characters': len(list(data))
#     }

#     return stats

# print(statistics('test-text.txt'))

def find_and_replace(file, search, replace):
    with open(file) as f:
        data = f.read()

    new_data = data.replace(search, replace)
    with open(file, 'w') as f:
        f.write(new_data)

find_and_replace('test-text.txt', 'test', 'Test')