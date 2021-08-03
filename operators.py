# # # mylist = [1,2,3]
# # # for num in range(0,12,2):
# # #     print(num)
# # # print(list(range(0,12,2)))
# # # # index_count = 0
# # # for letter in 'abcde':
# # #     print(f'at index {index_count} the letter is {letter}')
# # #     index_count+= 1
# # index_co = 0
# # word = "abcde"
# # for lette in word:
# #      print(word[index_co])
# #      index_co+= 1
# result = []
# results = [x if x % 2 == 0 else 'odd' for in range(0,11)]
# print(results)
# mylist = []
# for x in [2,4,6]:
#      for y in [100,200,300]:
#           mylist.append(x*y)
# print(mylist)
# mylist = [ x*y for x in [2,44,6] for y in [200,250,300]]
# print(mylist)
print([x for x in range(0,11) if x%3 == 0])