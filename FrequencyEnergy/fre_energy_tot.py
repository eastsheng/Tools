# reference code
# https://blog.csdn.net/askme_/article/details/106795560
mylist=[(3, 'a'), (7, 'b'), (4, 'a'), (5, 'c'), (2, 'a'), (1, 'b')]

mynewlist=[(sum(i[0] for i in group), key) for key, group in itertools.groupby(sorted(mylist, key = lambda i: i[1]), lambda i: i[1])]

print(mynewlist)
[(9, 'a'), (8, 'b'), (5, 'c')]