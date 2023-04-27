# input_string = input('Enter elements of a list separated by space: ')
# print("\n")
# user_list = input_string.split()
# threeList = []

# # convert each item to int type
# for i in range(len(user_list)):
#     # convert each item to int type
#     user_list[i] = int(user_list[i])
#     if i % 3 == 0 and user_list[i] % 3 == 0:
#         threeList.append(user_list[i])

# print(*threeList)


print(*[i for j, i in enumerate(input('Enter elements of a list separated by space: ').split()) if int(i) % 3 == 0 and j % 3== 0])