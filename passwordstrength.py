# PasswordStrength.py
# Name 
# Date 

""" Assesses passwords for their strength.
"""
from math import *

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
UPPER = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
LOWER = 'abcdefghijklmnopqrstuvwxyz'
DIGITS = '0123456789'
EVERYTHING = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()'
ROW2 = 'qwertyuiop'
ROW3 = 'asdfghjkl'
def HowMany(s1,s2):
    num = 0
    for c in s1:
        if s2.count(c) > 0:
            num = num + 1
    return num

def HowManyTriplets(s1,s2):
    num=0
    for c in range(0,len(s1)):
        if s2.count(s1[c]) > 0:
            if (c+3)<=len(s1):
                if s1[c+1] in s2 and s1[c+2] in s2:
                    num+=1
        else:
            num=0
    return num
     
def B1(s):
    """ Returns an int that is a score associated
    with password length.
    
    PreC: s is a valid password string."""
    
    return 3*min(len(s),15)

def B2(s):
    '''returns bonus score for mix of upper and lower case letters'''
    L = HowMany(s, LOWER)#number of lower case letters
    N = HowMany(s, LOWER+UPPER) #number of lower and upper case letters in general
    U = HowMany(s, UPPER) #number of upper case letters
    if N == 0:
        return 0
        #if there is no letter, the score is zero
    else:
        return int(floor(40.0*(1-(float(L)/float(N)))*(1-(float(U)/float(N)))))
        #the bonus score formula when there are letters

def B3(s):
    pass

def B4(s):
    pass

def B5(s):
    pass

def B6(s):
    pass

def D1(s):
    pass
    
def D2(s):
    pass

def D3(s):
    pass

def D4(s):
    '''
    returns two times the total number of consecutive look-a-likes
    '''
    count = 0  #starts with user input
    N = len(s) # length of the password
    for i in range(N-1): # for every character in the range of the password
        ch1 = s[i] # one character
        ch2 = s[i+1] # the character after the previou sone
        if EVERYTHING.index(ch1) <= 25 and EVERYTHING.index(ch2) <= 25:
            count = count + 1
            # if the two characters are both upper case letters
        elif 26 <= EVERYTHING.index(ch1) <= 51 and 26 <= EVERYTHING.index(ch2) <= 51:
            count = count + 1
            #if the two characters are both lower case letters
        elif 52 <= EVERYTHING.index(ch1) <= 62 and 52 <= EVERYTHING.index(ch2) <= 62:
            count = count +1
            #if the two characters are both numbers
        elif 63 <= EVERYTHING.index(ch1) <= 71 and 63 <= EVERYTHING.index(ch2) <= 71:
            count = count +1
            #if the two characters are both special characters
    return count*2

            
def D5(s):
    pass

def D6(s):
    '''returns three times the total number of row-2 triplets'''
    return 3*HowManyTriplets(s,ROW2)

def D7(s):
    '''returns three times the total number of row-3 triplets'''
    return 3*HowManyTriplets(s,ROW3)

def D8(s):
    pass
    
def PWS(s):
    pass

if __name__ == '__main__':
    s = raw_input('Enter a string: ')
    print 'B1 = %2d' % (B1(s))
    print 'B2 = %2d' % (B2(s)) 
    print 'D4 = %2d' % (D4(s))
    print 'D6 = %2d' % (D6(s))
    print 'D7 = %2d' % (D7(s))
    
           
    

