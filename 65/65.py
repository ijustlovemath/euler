from fractions import Fraction

def e_sequence(n):
    seq = []

    k = 1
    while len(seq) < n:
        seq.extend([1, 2*k, 1])
        k += 1

    return seq[:n]

def sum_seq(n):
    seq = e_sequence(n)
    convergent = Fraction(0, 1)
    for denom in seq[::-1]:
        print(f"1 / {convergent} + {denom}")
        convergent = Fraction(1, convergent + denom)

    return convergent

def sum_seq2(n):
    seq = e_sequence(n)
    def recurse(subseq):
        try:
            return Fraction(1, subseq[0] + recurse(subseq[1:]))
        except IndexError:
            return Fraction(0, 1)
    return recurse(seq)

def final():
    whole = Fraction(2, 1)
    total = whole + sum_seq(99)
    print(total)
    print(e_sequence(9))
    print(sum(int(c) for c in str(total.numerator)))


final()
