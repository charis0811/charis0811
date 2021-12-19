# # revenue = [[]]*3
# # actors=['a','b','c']

# # for i in range(3):
# #     revenue[0].append(actors[i])

# #     # rng=[[1,2],[3,4],[5,6],[7,8]]
# #     # for i in range(4):
# #     #     for j in range(3):
# #     #         revenue[1].append(rng[j][2])

# # print(revenue)


# # List = [] # 宣告一個一維串列
# # actors=['a','b','c']

# # for i in range(4):
# #     List.append([]) # 令其轉為二維串列形式

# # for j in range(3):
# #         # 將亂數產生的值放入串列中
# #     List.append(actors[j])

# # print(List)

# import random


# List = [] # 宣告一個一維串列
# actors=['a','b','c']
# for i in range(4):
#     List.append([]) # 令其轉為二維串列形式

#     for j in range(3):
#         # 將亂數產生的值放入串列中
#         List[i].append(actors[j])
#     break
# print(List)

graph = [[] for i in range(3)]
actors=['a','b','c']
actors2=['d','e','f']

for i in range(3):
    graph[i].append(actors[i])

for i in range(3):
    graph[i].append(actors2[i])

print(graph) #[['a', 'd'], ['b', 'e'], ['c', 'f']]