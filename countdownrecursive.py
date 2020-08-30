import random
import itertools
import rpn

#generate a random number
# bignumber = random.randint(1,999)
bignumber = 6
print(bignumber)
# smallnumbers = ['8','3','2','10','25','7']
smallnumbers = [3,2]
print(smallnumbers)

ops = ['+','-','*','/']



# take thing
# is it my answer
# what would I need to combine with this to make it my answer
# do I have that thing
# can I make that thing
#     take thing

def infix(a,b,op):
    string  = '(' + str(b) + ' ' + op + ' ' + str(a) + ')'
    return string

def makenumber(input, output):
    solution = []
    remainingnums = input.copy()
    for num in input:
        print(num)
        if num == output:
            print(solution)
        else:
            remainingnums.remove(num)
            for remnum in remainingnums:
                print(remnum)
                for op in ops:
                    print(op)
                    print(infix(num,remnum,op))
                    if remnum != None:
                        solution = solution + [infix(num,remnum,op)]
                        newnum = float(eval(infix(num,remnum,op)))
                        remainingnums = [newnum] + [remainingnums.remove(remnum)]
                        makenumber(remainingnums, output)
                    elif remainingnums == [output]:
                        print(solution)
                    else:
                        print(solution)
                        print('going back') 

makenumber(smallnumbers,bignumber)






