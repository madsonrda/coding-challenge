import sys

def main():
    sentence = raw_input()
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


if __name__ == '__main__':
    main()
