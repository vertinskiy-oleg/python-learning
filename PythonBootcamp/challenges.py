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


# def range_in_list(l, *args):
#     if args:
#         if len(args) == 2:
#             start, end = args[0], args[1] if args[1] < len(l) else len(l)
#         else:
#             start, end = args[0], len(l)
#     else:
#         start, end = 0, len(l)
#     print(start, end)
#     return sum(l[start:end + 1])

# def range_in_list(l, start=0, end=None):
#     end = end or len(l)
#     return sum(l[start:end + 1])


# print(range_in_list([1,2,3,4],0,2)) #  6
# print(range_in_list([1,2,3,4],0,3)) # 10
# print(range_in_list([1,2,3,4],1)) #  9
# print(range_in_list([1,2,3,4])) # 10
# print(range_in_list([1,2,3,4],0,100)) # 10
# print(range_in_list([],0,1)) # 0



# def same_frequency(num_1, num_2):
#     num_1_s, num_2_s = str(num_1), str(num_2)
#     if len(num_1_s) == len(num_2_s):
#         return all(num_1_s.count(n) == num_2_s.count(n) 
#                     for n in num_1_s)
#     return False


# print(same_frequency(551122,221515)) # True
# print(same_frequency(551122,231515)) # False
# print(same_frequency(321142,3212215)) # False
# print(same_frequency(1212, 2211)) # True
# print(same_frequency(1212, 2251)) # False


# def find_the_duplicate(l):
#     for n in l:
#         if l.count(n) == 2:
#             return n
#     return None


# print(find_the_duplicate([1,2,1,4,3,12])) # 1
# print(find_the_duplicate([6,1,9,5,3,4,9])) # 9
# print(find_the_duplicate([2,1,3,4])) # None



# def mode(l):
#     freq = {n : l.count(n) for n in l}
#     for k,v in freq.items():
#         print(k,v)
#         if v == max(freq.values()):
#             return k
    


# print(mode([2,4,1,2,3,3,4,4,5,4,4,6,4,6,7,4])) # 4




# def sum_up_diagonals(matrix):
#     total = 0
#     for i in range(len(matrix)):
#         total += matrix[i][i] + matrix[i][-i-1]
#     print(total)
#     return total


# list1 = [
#   [ 1, 2 ],
#   [ 3, 4 ]
# ]
 
# sum_up_diagonals(list1) # 10

# list2 = [
#   [ 1, 2, 3 ],
#   [ 4, 5, 6 ],
#   [ 7, 8, 9 ]
# ]
 
# sum_up_diagonals(list2) # 30
 
# list3 = [
#   [ 4, 1, 0 ],
#   [ -1, -1, 0],
#   [ 0, 0, 9]
# ]

# sum_up_diagonals(list3) # 11

# list4 = [
#   [ 1, 2, 3, 4 ],
#   [ 5, 6, 7, 8 ],
#   [ 9, 10, 11, 12 ],
#   [ 13, 14, 15, 16 ]
# ]
 
# sum_up_diagonals(list4) # 68

#
#