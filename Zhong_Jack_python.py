# --------------------Question 1--------------------
'''
function translate() takes a list of English words and returns a list of
Swedish words.
'''

def eng_sw(word):
    eng_sw={"merry":"god","christmas":"jul","and":"och",\
           "happy":"gott","new":"nytt","year":"år"} # define a dictionary 
# search for each word for its value, if it's not in the dictionary return the
# same word and continue           
    if word in eng_sw:
        return eng_sw.get(word) # if the word is in dictionary, return value
    else:
        return word # if the word isn't in dictionary, return the original

def translate(text): # the funtion itself
    words = text.split( ) # get each word from the string using split()function
    output = "" # initialize
    for i in words:
        output = output + eng_sw(i) + " " # add each word to the output
    return output


translate('merry christmas Lalala 123')




# --------------------Question 2--------------------
'''
function char_freq() takes a string and builds a
frequency listing of the characters contained in it and return a dictionary
'''

def char_freq(s):
    dic = {} # create a dictionary
    for i in s: 
        if i in dic:
            dic[i] += 1 # if key is already in dic, add 1 count
        else: 
            dic[i] = 1 # if key is not in dic, create it
    return dic    
    

char_freq('abbabcbdbabdbdbabababcbcbab')




# --------------------Question 3--------------------
'''
encoder/decoder of ROT-13.
'''

def decoder(string):
    key = {'a':'n', 'b':'o',
           'c':'p', 'd':'q', 'e':'r', 'f':'s', 'g':'t', 'h':'u', 'i':'v',
           'j':'w', 'k':'x', 'l':'y', 'm':'z', 'n':'a', 'o':'b', 'p':'c',
           'q':'d', 'r':'e', 's':'f', 't':'g', 'u':'h', 'v':'i', 'w':'j',
           'x':'k', 'y':'l', 'z':'m', 'A':'N', 'B':'O', 'C':'P', 'D':'Q',
           'E':'R', 'F':'S', 'G':'T', 'H':'U', 'I':'V', 'J':'W', 'K':'X',
           'L':'Y', 'M':'Z', 'N':'A', 'O':'B', 'P':'C', 'Q':'D', 'R':'E',
           'S':'F', 'T':'G', 'U':'H', 'V':'I', 'W':'J', 'X':'K', 'Y':'L',
           'Z':'M'} # dictionary
    output = '' # where the result is stored
    for i in string:
        if i in key:
            output += key[i] # if the character is in key, use decode
        else:
            output += i # if the character is not in key, return original
    return output


string = 'Pnrfne pvcure? V zhpu cersre Pnrfne fnynq!'
decoder(string)




# --------------------Question 4--------------------
'''
function correct() takes a string and sees to it that 
1) two or more occurrences of the space character is compressed into one, and 
2) inserts an extra space after a period 
   if the period is directly followed by a letter. 
'''

import re
def correct(string):
    string = re.sub('\ +', ' ', string) # if it matches spaces 
                                        # (\ is for escaping control character)
    string = re.sub('\.', '. ', string) # if it matches . with no space after
    return string
   
   
correct("This is very       funny and cool.Indeed!")
 



# --------------------Question 5--------------------
'''
function make_3sg_form() is given a verb in infinitive
form and returns its third person singular form. 
a. If the verb ends in y, remove it and add ies 
b. If the verb ends in o, ch, s, sh, x or z, add es 
c. By default just add s 
'''

import re
def make_3sg_form(verb):
    if verb.endswith('y'): # if the verb ends in y
        return re.sub('y', 'ies', verb) # substitute y for ies
    elif verb.endswith(('o','ch','s','sh','x','z')): # if ends in those
        return verb + 'es' # add es
    else:
        return verb + 's' # all other cases add s   


make_3sg_form('try')
make_3sg_form('brush')
make_3sg_form('run')
make_3sg_form('fix')




# --------------------Question 6--------------------
'''
function make_ing_form() is given a verb in infinitive form and returns its
present participle form
a. If the verb ends in e, drop the e and add ing (if not exception: be,
   see, flee, knee, etc.) 
b. If the verb ends in ie, change ie to y and add ing 
c. For words consisting of consonant-vowel-consonant, double the final letter 
   before adding ing 
d. By default just add ing 
'''

import re  
exception = ['be','see','flee','knee'] # you can add more exceptions here 
vowel = ['a','e','i','o','u'] # vowel list

def make_ing_form(verb):
    if verb.endswith('ie'): # do ie before e because it is a special case
        return re.sub('ie', 'ying', verb) # ie to ying
    elif verb.endswith('e') and verb not in exception: # ends with e but not 
                                                       # in exception
        return re.sub('e', 'ing', verb) # e to ing
    elif verb[-3] not in vowel and verb[-2] in vowel and verb[-1] not in vowel:
                            # the last 3 digits represented by[-3],[-2],[-1]
                            # letter not in vowel is in consonant
        return verb + verb[-1] + 'ing' # double final letter and add ing
    else:
        return verb + 'ing' # in all other cases, add ing


make_ing_form('lie')
make_ing_form('see')
make_ing_form('move')
make_ing_form('hug')




# --------------------Question 7--------------------
'''
employ reduce() fuction
function max_in_list() takes a list of numbers and 
returns the largest one
'''

from functools import reduce
def max1(*num): # return the biggest number in tuple
    biggest = 0 
    for i in num:
        if i > biggest:
            biggest = i # replace biggest by the biggest item in list
    return biggest
  
  
def max_in_list(list1):
    return reduce (max1,list1) # iterate max funtion for list
    

list1 = [1,3,56,2,64]
max_in_list(list1)



# --------------------Question 8--------------------
'''
this program maps a list of words into a list of integers
representing the lengths of the correponding words.
'''

def map_to_lengths_for(words):
    lengths = [] # initialize
    for word in words:
        lengths.append(len(word)) # add counts to the list
    return words, lengths # return corresponding counts


def map_to_lengths_map(words):
    return words, list(map(len, words)) # apply iteration of len function to 
                                        # words and make a list


def map_to_lengths_lists(words):
    return words, [len(word) for word in words] # count them 1 by 1 and print
    

map_to_lengths_for (['words','adf','adfa','12'])
map_to_lengths_map (['words','adf','adfa','12'])
map_to_lengths_lists (['words','adf','adfa','12'])




# --------------------Question 9--------------------


'''
function find_longest_word() takes a list of words
and returns the length of the longest one. 
'''

from functools import reduce
def find_longest_word(words):
    return reduce (max, list(map(len,words))) 
        # first use Question 8's map_to_lengths_map to get a list of length
        # secondly repeatedly take max of the first two numbers and replace
    
    
words = ['happy', 'satisfy', 'four']
find_longest_word(words)




# --------------------Question 10--------------------
'''
function filter_long_words() takes a list of words and an integer
n and returns the list of words that are longer than n.
'''

def filter_long_words(words, n):
    return list(filter(lambda word: len(word) > n, words))
        # first create a temp. function that compares length of a word to n
        # then filter out words whose value is True
    
    
words = ['hello','my','name','is','Jacklalala']
filter_long_words(words, 3)




# --------------------Question 11--------------------
'''
function translate() takes a list of English words and
returns a list of Swedish words
'''

def translate(words):
    dic = {"merry":"god","christmas":"jul","and":"och","happy":"gott",
           "new":"nytt","year":"år"} # dictionary
    return list(map(lambda word: dic.get(word), words))
        # first create a temp. function to get the value from dictionary
        # then use map function to iterate and return as a list

words = ["merry","christmas","and","happy","new","year","123"]
translate(words)




# --------------------Question 12--------------------
'''
Implement the higher order functions map(), filter()and
reduce()
'''

def map1(function, list1):
    output = [] # initialize output
    for i in list1:
        output.append(function(i)) # add function results 1 by 1 to output
    return output
    
'''test example'''   
list1 = [1,3,5,7,1,3,45,999,123]
def function(x):
    x += 1
map1(function, list1)    
#-------------------------------------------------------------------    


def filter1(function, list1):
    output = [] # initialize output
    for i in list1:
        if function(i) == True: # if item i passes filter
            output.append(i) # add i to output list
    return output
        
'''test example'''  
list1 = [1,3,5,7,1,3,45,999,123]
def function(x):
    if x > 15:
        return True
    else:
        return False
filter1(function, list1)        

#-------------------------------------------------------------------
def reduce1(function, list1):
    output = list1 # casually copy the list XD
    while len(output) > 1: # when the list has more than 1 element
        output[1] = function(list1[0],list1[1])
                # replace the second element with result of function using the
                # first and second elements so the list is reduced once
        del list1[0] # delete the first item so the second becomes the first
                     # in the next iteration
    return output
    
'''test example'''
list1 = [1,3,5,7,1,3,45,999,123]
reduce1(max, list1)

















