# --------------------Question 1--------------------
##Prof G - Good header docs!       
def translate(english=[]):
    '''
    function translate() takes a list of English words and returns a list of
    Swedish words.
    
    Parameter:
    a list
    
    Returns:
    The corresponding translation according to the dictionary in a list
    '''
    ## Take care of spaces, uppercases and words that are not in dictionary 
    ##Prof G - Nice way to handle case and unknown words!
    output = [] # initialize
    eng_sw = {"merry":"god","christmas":"jul","and":"och",
              "happy":"gott","new":"nytt","year":"år"} # define a dictionary 
    for i in english:             # for each word from the list
        if i.lower() in eng_sw:           # if the word is in dictionary
            output.append(eng_sw[i.lower()]) # add swedish to the list   
        else:                             # if the word isn't in dictionary
            output.append(i.lower())      # add the original word
    return output                            


print(translate(['Merry', 'christmas', 'AND', 'Lalala', '123']))




# --------------------Question 2--------------------

def char_freq(string=''):
    '''
    function char_freq() takes a string and builds a
    frequency listing of the characters contained in it and return a dictionary

    Parameter:
    a string
    
    Returns:
    frequency list of characters
    '''

    freq_list = {} # create a dictionary
    for i in string: 
        if i in freq_list:
            freq_list[i] += 1 # if key is already in dic, add 1 count
        else: 
            freq_list[i] = 1 # if key is not in dic, create it
    return freq_list    
    

print(char_freq('abbabcbdbabdbdbabababcbcbab'))




# --------------------Question 3--------------------

def decoder(string):
    '''
    function decoder takes each letter in the plain text and replace it by a
    letter 13 positions down the alphabet
    *encoder/decoder of ROT-13 (Caesar cipher where the shift is 13)
    
    Parameter:
    a string
    
    Return:
    result of Caesar cipher where the shift is 13
    '''
    ## Take care of non-characters
    ##Prof G - Can you shorten the key and still handle case?
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


print(decoder('Pnrfne pvcure? V zhpu cersre Pnrfne fnynq!'))




# --------------------Question 4--------------------

import re
##Prof G - Nice implementation!
def correct(string):
    '''
    function correct() takes a string and sees to it that 
    1) two or more occurrences of the space character is compressed into one 
    2) inserts an extra space after a period 
       if the period is directly followed by a letter.
       
    Parameter:
    a string
    
    Return:
    a corrected string according to the rules
    '''    
    ## create new strings applying rules
    ## Take care of . followed by character And . followed by some spaces

    space = re.sub('\ +', ' ', string) # substitute 2 or more spaces with 1
                                       # (\ is for escaping control character)

    dot = re.sub(r'(\.)(\w)', r'\1 \2', space) 
        # if we see a combination like (.)(letter)
        # substitute for (.) + a space + (letter)
    return dot
 
 
print(correct("This is very       funny and cool.Indeed!"))
print(correct("This.   is very       funny and cool.     Indeed!"))
 



# --------------------Question 5--------------------

import re
def make_3sg_form(verb):
    '''
    function make_3sg_form() is given a verb in infinitive
    form and returns its third person singular form. 
    a. If the verb ends in y, remove it and add ies 
    b. If the verb ends in o, ch, s, sh, x or z, add es 
    c. By default just add s 
    
    Parameter:
    a verb in string
    
    Return:
    the verb's third person singular form
    '''
    ##Prof G - How does it handle mixed case?
    if verb.endswith('y'):                             # if the verb ends in y
        return re.sub('y', 'ies', verb)                # substitute y for ies
    elif verb.endswith(('o','ch','s','sh','x','z')):   # if ends in those
        return verb + 'es'                             # add es
    else:
        return verb + 's'                              # all other cases add s   


print(make_3sg_form('try'))
print(make_3sg_form('brush'))
print(make_3sg_form('run'))
print(make_3sg_form('FIX'))




# --------------------Question 6--------------------

import re  ##Prof G - Only need to import once and then it was not used here.
def make_ing_form(verb):
    '''
    function make_ing_form() is given a verb in infinitive form and returns its
    present participle form
    a. If the verb ends in e, drop the e and add ing (if not exception: be,
                                                      see, flee, knee, etc.) 
    b. If the verb ends in ie, change ie to y and add ing 
    c. For words consisting of consonant-vowel-consonant, double the final letter 
       before adding ing 
    d. By default just add ing 
    
    Parameter:
    verb in a string
    
    Return:
    verb in present participle form
    '''

    exception = ['be','see','flee','knee'] # you can add more exceptions here 
    vowel = ['a','e','i','o','u'] # vowel list
    if verb.endswith('ie'):      # do ie before e because it is a special case
        return re.sub('ie', 'ying', verb)              # ie to ying
    elif verb.endswith('e') and verb not in exception: # ends with e but not 
                                                       # in exception
        return re.sub('e', 'ing', verb)                # e to ing
    elif verb[-3] not in vowel and verb[-2] in vowel and verb[-1] not in vowel:
                            # the last 3 digits represented by[-3],[-2],[-1]
                            # letter is consonant if it is not in vowel
        return verb + verb[-1] + 'ing' # double final letter and add ing
    else:
        return verb + 'ing'            # in all other cases, add ing


print(make_ing_form('lie'))
print(make_ing_form('see'))
print(make_ing_form('move'))
print(make_ing_form('hug'))




# --------------------Question 7--------------------

from functools import reduce
def max_in_list(list1):
    '''
    employ reduce() fuction
    function max_in_list() takes a list of numbers and 
    returns the largest one
    
    Parameter:
    a list of numbers
    
    Return:
    the largest number using reduce function
    '''
    
    return reduce(lambda x, y: max(x,y), list1) # iterate max funtion for list
    

print(max_in_list([1,3,56,232,64]))




# --------------------Question 8--------------------

def map_to_lengths_for(words):
    '''
    this program maps a list of words into a list of integers
    representing the lengths of the corresponding words.
    
    Parameter:
    a list of words
    
    Return:
    a list of lengthes of corresponding words
    '''
    
    lengths = []                  # initialize
    for word in words:
        lengths.append(len(word)) # add counts to the list
    return lengths                # return correponding counts


def map_to_lengths_map(words):
    '''
    this program maps a list of words into a list of integers
    representing the lengths of the corresponding words.
    
    Parameter:
    a list of words
    
    Return:
    a list of lengthes of corresponding words
    '''
    
    return list(map(len, words)) # apply iteration of len function to 
                                 # words and make a list


def map_to_lengths_lists(words):    
    '''
    this program maps a list of words into a list of integers
    representing the lengths of the corresponding words.
    
    Parameter:
    a list of words
    
    Return:
    a list of lengthes of corresponding words
    '''
    
    return [len(word) for word in words] # count them 1 by 1 and print
    

print(map_to_lengths_for (['words','adf','adfa','12']))
print(map_to_lengths_map (['words','adf','adfa','12']))
print(map_to_lengths_lists (['words','adf','adfa','12']))




# --------------------Question 9--------------------

from functools import reduce
def find_longest_word(words):
    '''
    function find_longest_word() takes a list of words
    and returns the length of the longest one. 
    
    Parameter:
    a list of string
    
    Return:
    length of the longest one
    '''
    
    return reduce (max, list(map(len,words))) 
        # first use Question 8's map_to_lengths_map to get a list of lengthes
        # secondly repeatedly take max of the first two numbers and replace
    
    
print(find_longest_word(['happy', 'satisfy', 'four']))




# --------------------Question 10--------------------

def filter_long_words(words, n):
    '''
    function filter_long_words() takes a list of words and an integer
    n and returns the list of words that are longer than n.
    
    Parameter:
    a list of words, an integer
    
    Return:
    words that are longer than n
    '''
    
    return list(filter(lambda word: len(word) > n, words))
        # create a lambda function that compares length of a word to n
        # keep words which passed the lambda function and discard the rest
    

print(filter_long_words(['hello','my','name','is','Jacklalala'], 3))




# --------------------Question 11--------------------

def translate(words):
    '''
    function translate() takes a list of English words and
    returns a list of Swedish words
    
    Parameter:
    a list of English words in a list
    
    Return:
    a list of Sswedish words in a list
    '''
    ##Prof G - How to handle mixed case?
    dic = {"merry":"god","christmas":"jul","and":"och","happy":"gott",
       "new":"nytt","year":"år"} # dictionary
    return list(map(lambda x: dic.get(x), words))
        # first create a temp. function to get the value from dictionary
        # then use map function to iterate and return as a list


print(translate(["merry","christmas","AND","happy","new","year","123"]))




# --------------------Question 12--------------------

## Implement the higher order functions map(), filter()and reduce()
## use help(funtion) to get their usage

# map------------------------------------------------

def map1(func, iterables):
    '''
    function map() make an iterator that computes the function using arguments 
    from each of the iterables. 
    
    Parameter:
    a function and a list
    
    Return:
    interate through the list with the function and return a list of results
    '''
    
    output = [] # initialize output
    for i in iterables:
        output.append(func(i)) # add function results 1 by 1 to output
    return output
    

print(map1(lambda x: x + 1, [1,2,3,4,5,99])) # add 1 to all elements
 
 
#filter----------------------------------------------  
 
def filter1(function, iterable):
    '''
    Return an iterator yielding those items of iterable for which function(item)
        is true.
    If iterable is a string or a tuple, the result also has that type; 
        otherwise it is always a list. 
        
    Parameter:
    a function and iterables
    
    Returns:
    items of iterable for which function(item) is true
    '''
    
    if isinstance(iterable, tuple): # if iterable is a tuple
        output = ()                 # initialize output to a tuple
        for i in iterable:
            if function(i):
                output += (i,)      # add item
        return output
                
    elif isinstance(iterable, str): # if iterable is a string
        output = ''                 # initialize output to a string
        for i in iterable:
            if function(i):
                output += i         # add item
        return output    

    else:   
        output = []                 # initialize output to a list
        for i in iterable:
            if function(i):
                output.append(i)    # add item
        return output 


print(filter1(lambda x: x>1, (1,3,5,-1,99,-99))) # filter elements >1 in tuple
print(filter1(lambda x: x=='a', 'adsfasdfczvaaaa.a')) # filter out a's
print(filter1(lambda x: x>1, [-4,-3,-2,-1,0,1,2,3,4,5,6])) # elements >1 in list


#reduce----------------------------------------------

def reduce1(function, sequence, initial=None):
    '''
    Apply a function of two arguments cumulatively to the items of a sequence,
    from left to right, so as to reduce the sequence to a single value.
    For example, reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]) calculates
    ((((1+2)+3)+4)+5).  If initial is present, it is placed before the items
    of the sequence in the calculation, and serves as a default when the
    sequence is empty.
    
    Parameter:
    a function and sequence
    
    Return:
    a single value after reduction
    '''
    
    output = sequence    # initialize output to sequence    
    if initial:
        output.insert(0, initial)
        
    while len(output) > 1: # when the list has more than 1 element
        output[1] = function(output[0], output[1])
                # get function result from 1st and 2nd element
                # replace the 2nd element with the result
        del output[0] # delete the 1st element so the 2nd becomes 
                        # the 1st element in the next iteration
    return output
    

print(reduce1(max, [-2,-1-0,1,2,]))
print(reduce1(lambda x,y: x+y, [-2,-1-0,1,2,]))
print(reduce1(max, [1,2,3], 4))
print(reduce1(max,[],1))

