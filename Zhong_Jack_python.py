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

'''try this
translate('merry christmas Lalala 123')
'''


# --------------------Question 2--------------------






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



















