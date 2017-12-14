'''
Python program to reverse a string

For example, if the string is "deliver", return "reviled". If the string is "the rain in spain", return "spain in rain the".

Use the concept of "recursion".
'''

def reverseString(A):

   if A is "":
       return ""

   # in the first iteration, A[-1] is 'g', A[0:-1] is 'abcdef'
   return A[-1]+reverseString(A[0:-1]) 


A = 'abcdefg'
print reverseString(A)



def reverseWords(B):
   # words is a list containing all words in sentence B
   old_word_list = B.split(" ")
   new_word_list = []

   for i in range(len(old_word_list)):
       new_word_list.append(old_word_list[-(i+1)])

   return " ".join(new_word_list)


B = 'the rain in spain'
print reverseWords(B)


