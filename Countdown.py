'''
Script for finding solutions to Countdown "Numbers Game" problems

To do
- Not require use of all numbers
- Keep only unique solutions up to commutation
- Enforce "no non-integer steps" rule
- Does this actually contain all the steps? what about combining different bracket sets?
- Random small numbers picking
'''

import random
import itertools
import rpn

#generate a random number
bignumber = random.randint(1,999)
print(bignumber)
smallnumbers = ['8','3','2','10','25','1']
print(smallnumbers)

ops = ['+','-','*','/']

numperms = list(itertools.permutations(smallnumbers))
no_nums = len(smallnumbers)
no_ops = no_nums - 1
#print(numperms)

opperms = list(itertools.product(ops,repeat=no_ops))

'''
we are going to generate the trial solutions in postfix notation, and compute using rpn
(and also convert to infix operators for ease of reading and use eval() to check the result)
'''

def infix(a,b,op):
    string  = '(' + b + ' ' + op + ' ' + a + ')'
    return string

def expand(numperm,opperm):
    numstack = list(numperm)
    opstack = list(opperm)
    #print(numstack + opstack)

    while len(numstack) > 1:
        b = numstack.pop()
        a = numstack.pop()
        op = opstack.pop(0)
        numstack.append(infix(a,b,op))
       # print(numstack + opstack)

    return numstack[0]


for numperm in numperms:

    for opperm in opperms:
        
        trialsolnrpn = ' '.join([str(num) for num in numperm]) + ' ' + ' '.join([str(op) for op in opperm])
        trialsolnbinops = expand(numperm,opperm)
        # print(trialsolnrpn)
        # print(trialsolnbinops)
        

        #binopsresult = float(eval(trialsolnbinops))
        rpnresult = float(rpn.solve_rpn(trialsolnrpn))

        if rpnresult.is_integer() and int(rpnresult) == bignumber:
            print(trialsolnbinops + '   ' + str(rpnresult))
        


        #error = float(rpnresult) - binopsresult
        # print(trialsolnrpn + '   ' + trialsolnbinops + '   ' + str(rpnresult))

        #print('Binop result: ' + str(binopsresult) + '\n'
        #    + 'rpn result: ' + str(rpnresult)  + '\n')
        #print(trialsolnbinops + ' = ' + opperm(result) + '  ('+str(result.is_integer())+')')

print('No further solutions')
#print(bignumber)