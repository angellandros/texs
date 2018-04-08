import sys


# usage: python3 clean_cites.py cites.txt
# where cites.txt is the output of export_cites.py
if __name__ == '__main__':
    s = set()
    with open(sys.argv[-1], 'r') as f:
        for line in f:
            word = line.strip()
            try:
                label = word[word.index('{')+1:word.index('}')]
                for l in label.split(','):
                    s.add(l)
            except ValueError:
                print('substring not found in ' + word)
    for label in sorted(list(s)):
        print(label)
