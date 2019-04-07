class NumberIntoChinese:
    # cn ='十百千万十万百万千万亿'
    cn = ['', '十', '百', '千', '万', '十', '百', '千', '亿']
    digit = '零一二三四五六七八九'
    def __init__(self, a):
        self.s = str(a)

    def trans(self):
        result = ''
        if self.s == '0':
            return '零'

        for i, c in enumerate(self.s[::-1]):
            if c!='0':
                result += NumberIntoChinese.cn[i]
                result += NumberIntoChinese.digit[int(c)]
            else:
                if i==0 or result[-1]=='零' or result[-1]=='万':
                    pass
                else:
                    result += NumberIntoChinese.digit[int(c)]

                if NumberIntoChinese.cn[i] == '万':
                    result += NumberIntoChinese.cn[i]

        result = result[::-1]
        if len(result)>1 and result[0]=='一' and result[1]=='十':
            return result[1:]
        return result

for a in (0, 10, 15, 123, 1000020, 10003, 474154010):

    c = NumberIntoChinese(a)
    print(a, ': ', c.trans())