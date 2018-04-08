if __name__ == '__main__':
    l = []
    with open('main.tex', 'r') as f:
        for line in f:
            if '%' in line:
                line = line[:line.index('%')]
            for word in line.split(' '):
                if '\\cite' in word:
                    l.append(word)
    for i in l:
        i = i.strip()
        i = i[i.index('\\cite'):]
        print(i)
