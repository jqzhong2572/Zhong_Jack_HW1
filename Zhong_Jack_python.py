# --------------------Question 1------------------
    '''
    function translate() takes a list of English words and returns a list of
    Swedish words.
    '''

def dictionary(word):
    dictionary={"merry":"god","christmas":"jul","and":"och",\
           "happy":"gott","new":"nytt","year":"år"} # define a dictionary 
# search for each word for its value, if it's not in the dictionary return the
# same word and continue           
    if word in dictionary:
        return dictionary.get(word) # if the word is in dictionary, return value
    else:
        return word # if the word isn't in dictionary, return the original

def translate(text): # the funtion itself
    words = text.split( ); # get each word from the string
    output = "" # initiate output
    for i in words:
        output = output + dictionary(i) + " " # add each word to the output
    return output




# --------------------Question 2------------------
