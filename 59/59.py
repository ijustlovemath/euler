from itertools import cycle, product

def is_ascii(integer):
    return integer < 128
    return (integer == ord(' ')
        or (integer >= ord('a') and integer <= ord('z'))
        or (integer >= ord('A') and integer <= ord('Z'))
    )

def compose(cyphertext, key_character):
    return cyphertext ^ key_character

def reveal(key):
    return ''.join(chr(k) for k in key)

def decrypt(message, key):
    return ''.join(chr(compose(m, k)) for m, k in zip(message, cycle(key)))

def get_words():
    with open('/usr/share/dict/cracklib-small', 'r') as f:
        return set([line.strip('\r\n') for line in f.readlines()])

def main():
    with open('p059_cipher.txt', 'r') as f:
        lines = f.readlines()

    dictionary = get_words()

    values = [int(value) for line in lines for value in line.split(',')]

    keys = product(range(ord('a'), ord('z') + 1), repeat=3)

    for key in keys:
        characters = cycle(key)
        if all(is_ascii(compose(c, v)) for c, v in zip(characters, values)):

            candidate = decrypt(values, key)
            
            words = candidate.split()
            N = len(words)

            if N < 5:
                continue
    
            count = 0
            for word in words:
                if word in dictionary:
                    count += 1

            if float(count) > 0.5 * N:
                print(f'key: {reveal(key)}, candidate: {candidate}')
                print(sum(ord(c) for c in candidate))


if __name__ == '__main__':
    main()
