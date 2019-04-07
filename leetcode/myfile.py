import random


def canwe(buckets, llist, n):
    if len(llist)>n:
        return False
    else:
        which_l = []
        for l in llist:
            can_l = []
            for i, b in enumerate(buckets):
                if l in b:
                    can_l.append(i)
            if can_l==[]:
                return False
            which_l.append(can_l)

        leng = len(llist)
        for _ in range(100):
            label = [1 for num in range(n)]
            _i = 0

            while _i<leng:
                flag1 = 1
                for x in which_l[_i]:
                    if label[x]==1:
                        flag1 = 0
                        break
                if flag1==1:
                    break
                else:
                    r = random.choice(which_l[_i])
                    while label[r]==0:
                        r = random.choice(which_l[_i])
                    label[r] = 0
                _i+=1
            if _i == leng:
                return True
        return False



while True:
    s1 = raw_input()
    n = int(s1)
    if s1 != '':
        word = list(raw_input())
        buckets = []
        for i in range(n):
            buckets.append(list(raw_input()))
        print canwe(buckets, word, n)
    else:
        continue