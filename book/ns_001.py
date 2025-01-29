# СТРОКИ (Операции со строками)

cmd = "interface Gi0/0"
print(cmd[0])
# i
print(cmd[1])
# n
print(cmd[-1])
# 0
print(cmd[-2])
# /
print(cmd[0:5])
# inter
print(cmd[3:7])
# erfa
index = 3
count = 4
print(cmd[index: index + count])
# erfa
print(cmd[2:])
# terface Gi0/0
print(cmd[:7])
# interfa
print(cmd[7:])
# ce Gi0/0
print(cmd[-7:])
# e Gi0/0
print(cmd[1:6])
# nterf
print(cmd[1:6:2])
# nef
s = "0123456789"
print(s[0:9:2])
# 02468
print(s[0:9:3])
# 036
print(s[::2])
# 02468
print(s[::3])
# 0369
num = 255
print(bin(num))
# 0b11111111
bin_num = bin(num)
print(bin_num[2:])
# 11111111
