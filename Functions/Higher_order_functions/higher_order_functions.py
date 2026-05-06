# import math
# from functools import reduce
#
# l=[12,15,7,18,20,21,25]
#
# print(list(filter(lambda x : (x%3!=0 or x%5!=0) and (x%3==0 or x%5==0),l)))
#
#
# c=[15,20,26,35,27,19,35,34]
# # a=list(map(lambda x: ((9//5)*x)+32,c))
# # print(a)
# # three=list(filter(lambda x : x%3==0,list(map(lambda x: ((9//5)*x)+32,c))))
# # print(three)
#
# print(reduce(lambda x,y: x+y,list(filter(lambda x : x%3==0,list(map(lambda x: ((9//5)*x)+32,c))))))
#
# ast=[3,5,10,8,1,15,7,6]
# # print(math.pi)
# print(reduce(lambda x,y : x+y ,list(filter(lambda x: x>75 , list(map(lambda x: math.pi*(x**2),ast))))))
#


l=[[1,2],[3,4],[5,6]]
print(list(map(lambda x: list(map(lambda y: y+5,x)),l)))


def adding(l):
    for i in range(l):
        for j in range(i):
            print(j+5)
    print(list(map(lambda x: list(map(lambda y: y + 5, x)), l)))
    return list(map(lambda x: list(map(lambda y: y + 5, x)), l))
print(adding(l))
