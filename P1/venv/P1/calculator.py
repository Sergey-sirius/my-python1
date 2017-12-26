x=float(input('x'))
y=float(input('y'))
oper=input('rule')
result = None

if oper == '+':
    result=x+y
elif oper == '-':
    result=x-y
else:
    print('Not support rule')


if result is not None:
    print('result',result)