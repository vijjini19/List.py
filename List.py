'''list is represented in square brackets[]
we can reprsent a empty list
a list can contain several data types in it ,it can even contain one more list in it.
list is mutable,modifications can be made
list is a sequential type'''
# a="welcome"
# a[0]='t'   #TypeError:'str' object does not support item assignment

# a=None
# print(type(a)) #class 'NoneType'

# a=["python"]
# print(a[0][1])  #y

# a=['h','e','l']
# print(a,type(a))
# a[0]='s'
# print(a)  #['s', 'e', 'l']
# a[-1]='u'
# print(a)  #['s','e','u']

# s=[6,3.5,"hai",True,False,[2,3]]
# print(s,type(s))
# s[2]="hey"
# print(s)  #[6,3.5,'hey',True,False,[2,3]]
# print(s[-1][0])  #2

'''append()-this method will add a elements at the end of the list'''
# n=[2,4.5,"hey",[3,7]]
# n.append(5)
# print(n)  #[2,4.5,'hey',[3,7],5]

'''clear()-this method will clears the all elements in the list'''
# n=[2,4.5,"hey",[3,7]]
# n.clear()
# print(n)  #[]

'''copy()'''
# n=[5,16,34,67]
# print(n)
# b=n.copy()
# print(b)

'''count()-this method will count how many times particular element is there in list'''
# n=[2,2,4.5,"hey",[3,7]]
# print(n.count(2)) #2
# print(n.count([3,7])) #1

'''extend()'''
# a=[3,5,7]
# b=[6,2,1]
# a.extend(b)
# print(a)  #[3,5,7,6,2,1]
# b.extend(a)
# print(b)  #[6,32,1,3,5,7]

'''index()'''
# a="welcome"
# print(a.index('t'))  #ValueError:substring not found
# n=[2,4.5,'hai',4,6]
# print(n.index(4))  #3
# print(n.index(6))  #4
# print(n.index('hai'))  #2

'''insert()'''
# w=[12,14,16,13,78]
# w.insert(2,'hi')
# print(w)  #[12,14,'hi',16,13,78]

'''pop()'''
# m=[12,13,14,15,16]
# m.pop()
# print(m)
# m.pop(2)
# print(m) #[12, 13, 15, 16]

'''remove'''
# n=[2,2,4.5,"hey",[3,7]]
# n.remove('hey')
# print(n)  #2, 2, 4.5, [3, 7]

'''reverse()'''
# n=[1,2,3,4,5]
# print(n[::-1])
# n.reverse()
# print(n)

'''sort()'''
# n=[1,5,8,2,3,9,3]
# n.sort()
# print(n)  #1, 2, 3, 3, 5, 8, 9














