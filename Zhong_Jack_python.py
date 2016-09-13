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
    words = text.split( ) # get each word from the string
    output = "" # initialize
    for i in words:
        output += eng_sw(i) + " " # add each word to the output
    return output

'''try
translate('merry christmas Lalala 123')
'''


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
    
'''try
char_freq('abcabczz')
'''





# --------------------Question 3--------------------
'''
encoder/decoder of ROT-13.
'''

key = {'a':'n', 'b':'o',
'c':'p', 'd':'q', 'e':'r', 'f':'s', 'g':'t', 'h':'u', 'i':'v',
'j':'w', 'k':'x', 'l':'y', 'm':'z', 'n':'a', 'o':'b', 'p':'c',
'q':'d', 'r':'e', 's':'f', 't':'g', 'u':'h', 'v':'i', 'w':'j',
'x':'k', 'y':'l', 'z':'m', 'A':'N', 'B':'O', 'C':'P', 'D':'Q',
'E':'R', 'F':'S', 'G':'T', 'H':'U', 'I':'V', 'J':'W', 'K':'X',
'L':'Y', 'M':'Z', 'N':'A', 'O':'B', 'P':'C', 'Q':'D', 'R':'E',
'S':'F', 'T':'G', 'U':'H', 'V':'I', 'W':'J', 'X':'K', 'Y':'L',
'Z':'M'}

string = 'Pnrfne pvcure? V zhpu cersre Pnrfne fnynq!'
output = '' 

for i in string:
    if i in key:
        output += key[i] # if the character is in key, use decode
    else:
        output += i # if the character is not in key, return original
    
print (output)



# --------------------Question 4--------------------


# --------------------Question 5--------------------


# --------------------Question 6--------------------



# --------------------Question 7--------------------
'''
employ reduce() fuction
function max_in_list() takes a list of numbers and 
returns the largest one
'''

def max_in_list(*num): #return the biggest number in tuple
    biggest = 0 
    for i in num:
        if i > biggest:
            biggest = i
    return biggest
  
from functools import reduce  
max_num = reduce (max_in_list,[1,3,76,4,1,34,99]) # user may modify this line
print (max_num)



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
    return words, [len(word) for word in words]
    

'''try these
map_to_lengths_for (['words','adf','adfa','12'])
map_to_lengths_map (['words','adf','adfa','12'])
map_to_lengths_lists (['words','adf','adfa','12'])
'''



# --------------------Question 9--------------------

# --------------------Question 10--------------------

# --------------------Question 11--------------------

# --------------------Question 12--------------------



















