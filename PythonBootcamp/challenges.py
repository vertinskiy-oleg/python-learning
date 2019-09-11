# def list_check(l):
#     return all(type(i) == list for i in l)


# print(list_check([[],[1],[2,3], (1,2)])) # False
# print(list_check([1, True, [],[1],[2,3]])) # False
# print(list_check([[],[1],[2,3]])) # True


# def includes(col, val, index=0):
#     if type(col) == dict:
#         return val in col.values()
#     else:
#         return val in col[index:]

# print(includes([1, 2, 3], 1)) # True 
# print(includes([1, 2, 3], 1, 2)) # False 
# print(includes({ 'a': 1, 'b': 2 }, 1)) # True 
# print(includes({ 'a': 1, 'b': 2 }, 'a')) # False
# print(includes('abcd', 'b')) # True
# print(includes('abcd', 'e')) # False

# def two_list_dictionary(keys, values):
#     d = dict(zip(keys, values))
#     if len(keys) > len(values):
#         for i in keys[len(values)::]:
#             d[i] = None
#     return d

# print(two_list_dictionary(['a', 'b', 'c', 'd', 'e', 'f', 'g'], [1, 2, 3])) # {'a': 1, 'b': 2, 'c': 3, 'd': None}
# print(two_list_dictionary(['a', 'b', 'c']  , [1, 2, 3, 4])) # {'a': 1, 'b': 2, 'c': 3}
# print(two_list_dictionary(['x', 'y', 'z']  , [1,2])) # {'x': 1, 'y': 2, 'z': None}


def range_in_list(l, *args):
    if len(args) == 2:
        start, end = args
    elif len(args) == 1:
        start, end = args[0], len(l) - 1
    else:
        start, end = 0, len(l) - 1
    return sum(l[start:end + 1])


print(range_in_list([1,2,3,4],0,2)) #  6
print(range_in_list([1,2,3,4],0,3)) # 10
print(range_in_list([1,2,3,4],1)) #  9
print(range_in_list([1,2,3,4])) # 10
print(range_in_list([1,2,3,4],0,100)) # 10
print(range_in_list([],0,1)) # 0
