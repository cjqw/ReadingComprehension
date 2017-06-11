#!/usr/bin/python3.5

result_file = 'result.txt'
input_file = 'data/test.txt'

if __name__ == '__main__':
    entity = {}
    s = []
    with open(result_file,'r') as fin:
        for i in range(10):
            fin.readline()
            entity[int(fin.readline())] = i
        while True:
            line = fin.readline()
            if line:
                answer = int(line.strip())
                s.append(entity.get(answer,0))
            else:
                break
    acc = 0
    with open(input_file,'r') as fin:
        for idx in s:
            for i in range(20): fin.readline()
            st = fin.readline().strip().lower()
            st = st.split('\t')
            choice = st[len(st) - 1].split('|')
            ans = st[1]
            result = choice[idx]
            if result == ans:
                acc += 1
            print(result)
            fin.readline()


            

