# 1)输入"1+1"，输出2
# 2)输入"2+2*4"，输出10
# 3)输入"(2+2)*4"，输出16

def solution(x):
    sum = 0
    if x.find('(') == -1:

        sub1 = x.split('+')

        for item in sub1:
            if item.find('*') == -1:
                sum += int(item)
            else:
                sub2 = item.split('*')
                mul = 1
                for item in sub2:
                    if not item.find('(') == -1:
                        x2 = item.replace('(', '')
                        x2 = x2.replace(')', '')
                        mul *= solution(x2)
                    else:
                        mul *= int(item)
                sum += int(sub2[0]) * int(sub2[1])
    else:

        if x.find('*')==-1:

            sub1 = x.split('+')

            for item in sub1:

                if not item.find('(')==-1:
                    item=item.replace('(','')
                    sum+=int(item)
                elif not item.find(')')==-1:
                    item = item.replace(')', '')
                    sum += int(item)
                else:
                    sum += int(item)
        else:

            if not x.find(')*') == -1:
                mul=1
                sub1 = x.split('*')

                for item in sub1:
                    if not x.find('(') == -1:
                        x2 = item.replace('(', '')
                        x2 = x2.replace(')', '')
                        mul *= solution(x2)

                    else:
                        mul *= int(item)
                return mul
            elif not x.find('*(') == -1:
                mul=1
                sub1 = x.split('*')

                for item in sub1:
                    if not x.find('(') == -1:
                        x2 = item.replace('(', '')
                        x2 = x2.replace(')', '')
                        mul *= solution(x2)

                    else:
                        mul *= int(item)
                return mul
            elif not (x.find('+(')==-1):
                sub1 = x.split('+')
                for item in sub1:
                    if not x.find('(') == -1:
                        x2 = item.replace('(', '')
                        x2 = x2.replace(')', '')
                        sum += solution(x2)
                    else:
                        sum += int(item)



            elif not (x.find(')+')==-1):

                sub1 = x.split('+')
                for item in sub1:
                    if not x.find('(') == -1:
                        x2 = item.replace('(', '')
                        x2 = x2.replace(')', '')
                        sum += solution(x2)
                    else:
                        sum += int(item)



            else:
                sub1 = x.split('*')
                mul = 1
                for item in sub1:
                    if not x.find('(') == -1:
                        x2 = item.replace('(', '')
                        x2 = x2.replace(')', '')
                        mul *= solution(x2)
                    else:
                        mul *= int(item)
                return mul




    return sum
    # print(sum)
        # if not x.find('*')==-1:
        #     sub1=x.split('*')
if __name__ == '__main__':
    a='2*((2+2)+3)'
    # x=a.replace('(','')
    # x=x.replace(')','')
    # print(x)
    print(solution(a))