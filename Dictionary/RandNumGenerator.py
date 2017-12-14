# Given a dictionary named 'fruits', generate a random entries of 'apple', 'orange', and 'banana',
# so that the distribution of randomly generated entries match the one from the dictionary.

import numpy as np

class Solution(object):
    def RandNum(self, d, numEntry):

        total = float(sum(d.values()))        

        d['orange'] = d['orange']/total
        d['apple'] = d['apple']/total + d['orange']
        d['banana'] = 1
        
        #print d['orange'], d['apple'], d['banana']

        for i in range(numEntry):
            num = np.random.uniform()
            #print i, num

            if num < d['orange']:
               print 'orange'
            elif num > d['apple']:
               print 'banana'
            else:
               print 'apple'
 


fruits = {'orange': 2, 'apple': 3, 'banana':5}
numEntry = 100

a = Solution()
a.RandNum(fruits, numEntry)
#Ans = a.RandNum(fruits)
#print Ans


