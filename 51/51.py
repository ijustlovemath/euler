from itertools import combinations

def primes_sieve(limit, primality=None, smallest=2):
    if primality is None:
        primality = [True] * limit                          # Initialize the primality list
        primality[0] = primality[1] = False

    for (i, isprime) in enumerate(primality):
        if isprime:
            if i >= smallest:
                yield i
            for n in range(i*i, limit, i):     # Mark factors non-prime
                primality[n] = False

def find_family(size=1, primes=None, seed=None, positions=None):
    def get_digit(value, index):
        temp = value // 10 ** index
        return temp % 10

    def replace(value, digit, positions):
        for p in positions:
            value = value - (10**p * get_digit(value, p)) + (digit * 10**p)
        return value

    initial_seed = seed
    result = {initial_seed}
    for digit in range(10):
        seed = replace(seed, digit, positions)
        if seed in primes:
            result.add(seed)
    if len(result) == size:
        print(f"found result, {initial_seed} % {positions} = {result}")
        return min(result)

n = 6 # first billion should have it
primes = list(primes_sieve(10**n, smallest=10**(n-1)))
primes_tester = set(primes)

final_prime = 10**n

for i in range(1, n+1):
    all_indices = list(combinations(range(n), i))
    for change_indices in all_indices:
        for seed in primes:
            candidate = find_family(size=8, seed=seed, primes=primes_tester, positions=change_indices)
            if candidate and candidate < final_prime:
                print(f"=== NEW smallest: {candidate} ===")
                final_prime = candidate

