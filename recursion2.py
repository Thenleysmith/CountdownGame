import random
import itertools
import rpn

#generate a random number
# bignumber = random.randint(1,999)
bignumber = 40
print(bignumber)
# smallnumbers = ['8','3','2','10','25','7']
smallnumbers = [2,20,10,4]
print(smallnumbers)

ops = ['+','-','*','/']

# take thing
# is it my answer
# what would I need to combine with this to make it my answer
# do I have that thing
# can I make that thing
#     take thing

def infix(a,b,op):
    string  = '(' + str(a) + ' ' + op + ' ' + str(b) + ')'
    return string

def evaluateop(a,b,op):
    if a > b:
        if op == '/':
            if a%b == 0:
                a = list(a.keys())[0]



def evaluations(a,b,ops):
    resultvals = []
    resultexps = []

    for op in ops:
        if a > b:
            if op == '/':
                if a%b == 0:
                    resultvals = resultvals + [a//b]
                    resultexps = resultexps + [infix(a,b,op)]
            else:
                resultvals = resultvals + [eval(infix(a,b,op))]
                resultexps = resultexps + [infix(a,b,op)]

    return {resultvals[i] : resultexps[i] for i in range(len(resultvals))}






def makenumber(input, output):
    for num in input:
        if num == output:
            print(num)
            return
        remnums = input.copy()
        remnums.remove(num)
        for remnum in remnums:
            evals = evaluations(num,remnum, ops)
            for value in evals:
                if value == output:
                    print(evals[value] + ' = '+ str(value))
            

makenumber(smallnumbers,bignumber)