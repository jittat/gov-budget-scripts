import sys

def append_map(st_src, st_des, m):
    for s,t in zip(st_src, st_des):
        if s not in m:
            m[s] = t

def build_map(train_filename):
    lines = open(train_filename).readlines()
    lcount = int(len(lines)/2)

    cmap = {}
    for i in range(lcount):
        append_map(lines[i*2],lines[i*2+1],cmap)
    return cmap

def main():
    cmap = build_map('train.txt')
    input_filename = sys.argv[1]
    lines = open(input_filename).readlines()
    for i in range(len(lines)):
        #print(lines[i][:-1],end='|')
        out = []
        for c in lines[i]:
            if ord(c) < 32:
                pass
            if ord(c) < 128:
                out.append(c)
            elif c in cmap:
                out.append(cmap[c])
            else:
                out.append('*')
        print(''.join(out[:-1]))

if __name__ == '__main__':
    main()

