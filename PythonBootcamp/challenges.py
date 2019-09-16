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



# def find_greater_numbers(l):
#     count = 0
#     for i in range(len(l)):
#         for j in range(i+1, len(l)):
#             # print(l[i], l[j], l[i] < l[j])
#             if l[i] < l[j]:
#                 count += 1
#     print(count)
#     return count


# find_greater_numbers([1,2,3]) # 3 
# find_greater_numbers([6,1,2,7]) # 4
# find_greater_numbers([5,4,3,2,1]) # 0
# find_greater_numbers([]) # 0


# def is_odd_string(s):
#     return sum(1 + ord(char) - ord('a') for char in s) % 2 != 0


# print(is_odd_string('a')) # True
# print(is_odd_string('aaaa')) # False
# print(is_odd_string('amazing')) # True
# print(is_odd_string('veryfun')) # True
# print(is_odd_string('veryfunny')) # False


# def valid_parentheses(parens):
#     count = 0
#     i = 0
#     while i < len(parens):
#         if (parens[i] == '('):
#             count += 1
#         if (parens[i] == ')'):
#             count -= 1
#         if (count < 0):
#             return False
#         i += 1
#     return count == 0

# def valid_parentheses(s):
#     count = 0
#     for i in range(len(s)):
#         import pdb; pdb.set_trace()
#         if s[i] == '(':
#            count += 1
#         elif s[i] == ')':
#             count -= 1
            
#         if count < 0:
#             return False
#     return count == 0


# print(valid_parentheses("()")) # True 
# print(valid_parentheses("()))")) # False 
# print(valid_parentheses(")(()))")) # False 
# print(valid_parentheses("(")) # False 
# print(valid_parentheses("(())((()())())")) # True 
# print(valid_parentheses('))((')) # False
# print(valid_parentheses('())(')) # False
# print(valid_parentheses('()()()()())()(')) # False


# def reverse_vowels(s):
#     l = list(s)
#     vowels = [char for char in l if char in 'aeiouAEIOU']
#     count = 0
#     for i in range(len(l)):
#         if l[i] in vowels:
#             l[i] = vowels[-count-1]
#             count += 1
#    return "".join(l)


# reverse_vowels("Hello!") # "Holle!" 
# reverse_vowels("Tomatoes") # "Temotaos" 
# reverse_vowels("Reverse Vowels In A String") # "RivArsI Vewols en e Streng"
# reverse_vowels("aeiou") # "uoiea"
# reverse_vowels("why try, shy fly?") # "why try, shy fly?"


# def three_odd_numbers(l):
#     for i in range(len(l)):
#         l_3 = l[i:i+3]
#         if len(l_3) == 3 and sum(l_3) % 2 != 0: 
#             return True
#     return False




# three_odd_numbers([1,2,3,4,5]) # True
# three_odd_numbers([0,-2,4,1,9,12,4,1,0]) # True
# three_odd_numbers([5,2,1]) # False
# three_odd_numbers([1,2,3,3,2]) # False





# def running_average():
#     call_count, num_count = [0, 0]
#     def inner(num):
#         nonlocal call_count, num_count
#         call_count += 1
#         num_count += num
#         average = num_count/call_count
#         return print(round(average, 2))
#     return inner

    
# rAvg = running_average()
# rAvg(10) # 10.0
# rAvg(11) # 10.5
# rAvg(12) # 11

# rAvg2 = running_average()
# rAvg2(1) # 1
# rAvg2(3) # 2



# def letter_counter(s):
#     def inner(char):
#         nonlocal s
#         s = s.lower()
#         return print(s.count(char))
#     return inner



# counter = letter_counter('Amazing')
# counter('a') # 2
# counter('m') # 1

# counter2 = letter_counter('This Is Really Fun!')
# counter2('i') # 2
# counter2('t') # 1 



# def once(func):
#     count = 0
#     def inner(*args):
#         nonlocal count
#         count += 1
#         if count > 1:
#             return None
#         return func(*args)
#     return inner


# def add(a,b):
#     return a+b

# oneAddition = once(add)

# print(oneAddition(2,2)) # 4
# print(oneAddition(2,2)) # None
# print(oneAddition(12,200)) # None




# def next_prime(num):
#     for n in range(1, num+1):
#         for i in range(1, n):
#             if n % i == 0:
#                 break
#             print(n)

# next_prime(10)



# primes = next_prime()
# print([next(primes) for i in range(100)])
# # [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]


def is_prime(num):
    for i in range(2, num):
            if num % i == 0:
                    break
    else:
            print(True)

