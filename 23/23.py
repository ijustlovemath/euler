import math

max_imperfect = 28123

def divisor_set(n):
    divisors = {1}

    for i in range(2, 1 + int(math.sqrt(n))):
        if n % i == 0:
            divisors = divisors.union({i, n//i})

    return divisors
    

def is_abundant(n):
    return sum(divisor_set(n)) > n

def abundant_list(maximum):
    return [n for n in range(1, maximum + 1) if is_abundant(n)]

necessary_abundants = set(abundant_list(max_imperfect))

print(abundant_list(270))

def cannot_be_written_as_sum(n):
    for k in necessary_abundants:
        if k >= n:
            continue

        if n - k in necessary_abundants:
            return False
    return True
    
total_unable = 0
for n in range(1, max_imperfect + 1):
    if cannot_be_written_as_sum(n):
        total_unable += n

print(total_unable)
