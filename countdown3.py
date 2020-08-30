'''
Script for finding solutions to Countdown "Numbers Game" problems

To do
- Not require use of all numbers
- Keep only unique solutions up to commutation
- Enforce "no non-integer steps" rule
- Does this actually contain all the steps? what about combining different bracket sets?
- Random small numbers picking


It is widely acknowledged that this is an AWFUL idea
'''

import random
import itertools
import rpn

#generate a random number
bignumber = random.randint(1,999)
print(bignumber)
smallnumbers = ['8','3','2','10','25','7']
print(smallnumbers)

ops = ['+','-','*','/']

numperms = list(itertools.permutations(smallnumbers))
no_nums = len(smallnumbers)
no_ops = no_nums - 1
#print(numperms)


opperms = list(itertools.combinations_with_replacement(ops,r=no_ops))
firstpaircombos = list(itertools.combinations(smallnumbers, r = 2 ))
counter = 0
for opperm in opperms:
    for combo in firstpaircombos:
        remainingnumbers = smallnumbers.copy()
        remainingnumbers.remove(combo[0])
        remainingnumbers.remove(combo[1])
        firstnumbers = combo
        endings = list(itertools.permutations(list(remainingnumbers)+list(opperm)))
        for ending in endings:
            trial = list(firstnumbers) + list(ending)
            trialrpn = ' '.join([str(symbol) for symbol in trial])
            rpnresult = float(rpn.solve_rpn(trialrpn))
            counter = counter + 1
            if counter%5000 == 0:
                print(counter)
            if rpnresult.is_integer() and int(rpnresult) == bignumber:
                print(trialrpn + ' = ' + str(rpnresult))



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