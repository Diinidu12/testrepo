def average(*args):
    "Return mean of a non-empty tuple of memories"
    sum=0.0
    for x in args:
        sum+=x
    return sum/len(args)

u=average(1,2,3,4)
v=average(1,2,3,4,5)
print(u)
print(v)
