# a=(1,2,3)
# print((a*4))

#
# def fun(l1,num):
#     if len(l1)==2:
#         return l1
#     else:
#         for i in l1:
#             if num % 3 == 0:
#                 l1.pop(0)
#                 ret=fun(l1,num+1)
#                 return ret
#             l1.append(l1.pop(0))
#             num += 1
# l1=list(range(20))
# ret=fun(l1,8)
# print(ret)


# def test(ren,count=8):
#     b = count
#     for i in ren:
#         if len(ren) == 2:
#             return ren
#         if b % 3 == 0:
#             b += 1
#             ren.remove(i)
#         b += 1
#     print(ren)
#     return test(ren,b)
#
# ren = list(range(20))
# test(ren)

# c=1
# # # def f():
# # #     global c
# # #     for i in range(1,4):
# # #         c+=1
# # # f()
# # # print(c)


a={'a':1,'b':5,'c':3,'d':9}
l=sorted(a.items(),key=lambda x:x[1])
print(dict(l))
