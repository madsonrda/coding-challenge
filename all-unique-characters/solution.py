import sys

def countChar(sentence):
    d = {}
    unique = True
    for i in range(len(sentence)):
        if sentence[i] in d:
            unique = False
            break
        else:
            d[sentence[i]] = True

    if unique:
        print("all characters are unique")

def countChar2(sentence):
    mask = 0
    unique = True
    for i in range(len(sentence)):
        val = ( ord(sentence[i]) - ord('a') )
        if  (  mask &  1 << val ) > 0:
            unique = False
            break
        mask |= 1 << val
    if unique:
        print("all characters are unique")


def main():
    sentence = raw_input()
    countChar2(sentence)


if __name__ == '__main__':
    main()
