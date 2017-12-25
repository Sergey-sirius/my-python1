str1 = 'hel'
str2 = 'lo'
result = str1 + str2

print(result)

a = 48
b = 73

message1 = '%d + %d = %d' % (a, b, a + b)
print(message1)

message2 = '{} - {} = {}'.format(a, b, a - b)
print(message2)


#indexatia strok

s = 'Hello, World!'

# (vernutsia v 7 uroke)
print(s[0])   # index 0
print(s[4])   # 4
print(s[-1])  # minus s konza

print(s[2:7])    # s 2 po 5
print(s[2:7:2])  #s 2 po 5 shag 2