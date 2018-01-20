def myf1():
    print("eeeeee test1")

print(min(-5,12,-4))

xs = {"2222","11111","333"}
print(min(xs))

xs = {2222,11111,333}
print(min(xs))

def b_min(first,*args):
    l1=float("-inf")
    hi=255
    res=hi
    for arg in (first, ) + args:
        if arg < res and l1 < arg < hi:
            res=arg
    return max(res,l1)

print("----------------------")
print(b_min(1211, -1322, 256))
