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
