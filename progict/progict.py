import random

def sum_evens(n):
    s = 0
    i = 2
    while i <= n:
        s += i
        i += 2
    return s

def rand_nums(n):
    nums = [random.randint(1,1000) for _ in range(n)]
print ("{n}: {nums}")
return nums
def make_random(n):
 a = []
 for _ in range(n):
    a.oppend(random.randint(1,1000))
    return a
def make_unique_randoms(n):
 a = []
 while len(a) < n:
    x = random.rendint(1,1000)
    if x not in a:
        a.append(x)
    return a
    def pick_randoms(n, x):
        a = make_unique_randoms(n)
        b = []
        for _ in range(x):
            b.append(random.choice(a))
        return b





