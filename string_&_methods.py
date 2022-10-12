# print(len(("python"))) # 6

# a="python"
# print(a,type((a)))  # 'str'
# print(a[0]) # 0

# print("python"[0]) # p
# print("python"[1]) # y
# print("python"[2]) # t
# print("python"[3]) # h
# print("python"[4]) # o
# print("python"[5]) # n
# print("python"[6]) # IndexError: string index out of range

# """concatenation:=""" 
# "used omly for strings will combine more than one strings together . we use + to represent concatenation in the string concept ."
# "string is immutable , modifications cannot be made"

# v= "department"
# print(v[3]+v[2]+v[3]+v[4]+v[5]+v[6]+v[7]+v[8]+v[9]) # apartment

# print("python"[-1]) # n
# print("python"[-2]) # o
# print("python"[-3]) # h
# print("python"[-4]) # t
# print("python"[-5]) # y
# print("python"[-6]) # p
# print("python"[-7]) # IndexError: string index out of range

"""Slicing"""
# w="python"
# print(w[:]) # python
# print(w[0:]) # python
# print(w[0:6]) # python
# print(w[0:0])
# print(w[0:1]) # p 
# print(w[0:2]) # py
# print(w[0:3]) # pyt
# print(w[0:4]) # pyth
# print(w[0:5]) # pytho
# print(w[0:6]) # python
# print(w[0:7]) # python
# print(w[0:99]) # python
# print(w[0:0]) # 
# print(w[3:2]) # 
# print(w[5:3]) # 
# print(w[0:-1]) # pytho
# print(w[0:-2]) # pyth
# print(w[0:-3]) # pyt
# print(w[0:-4]) # py
# print(w[0:-5]) # p
# print(w[0:-6]) # 
# print(w[0:-7]) # 

# r="python"
# print(r[2:5]) # tho
# print(r[3:4]) # h
# print(r[5:2]) #
# print(r[5:5]) #

# y="python"
# print(y[-1:-6])
# print(y[2:-3]) # t
# print(y[-6:]) # python

c="python"
# print(c[: :]) # python
# print(c[0: :1]) # python
# print(c[: :2]) # pto
print(c[: :-4]) # ny
print(c[: :-5]) 
print(c[: :-6]) 
print(c[1: :]) 
print(c[2: :]) 
print(c[3: :]) 
print(c[4: :]) 
print(c[5: :]) 
print(c[6: :]) 
print(c[1: 6:]) 
print(c[2:5 :]) 
print(c[3:4 :]) 
print(c[4:3:]) 
print(c[5:2 :]) 
print(c[6:1:]) 