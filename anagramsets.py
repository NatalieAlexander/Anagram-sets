# print program header
print("***** Anagram Set Search *****")

################################################################################

# try/except block
try: #find lexicon file
    with open("EnglishWords.txt", "r") as words_file:
        words_file = words_file.read().splitlines() #read all lines of file and split lines at \n
        skip_lines = words_file.index("START") #lines to skip until "START" is found
        words_file = words_file[skip_lines:] #only include lines from "START" to end of file

except FileNotFoundError: #if lexicon file not found, print error message and exit program
    print("Sorry, could not find file 'EnglishWords.txt'.")
    sys.exit(1)
    
################################################################################
    
# get user input: word length
input_word_length = int(input("Enter word length: ")) #ensure integer input value

# print searching
print("Searching...")

# get user input: output file name
out_file = input("Enter file name: ")

# print writing results
print("Writing results...")

################################################################################

# word_length_match function
def word_length_match(input_word_length, lexicon=words_file):
    """
    function to find words in lexicon with matching length as input length
    parameters: input word length and a lexicon file
    """
    
    #initialize empty list to append words with matching length as input length
    matched_length = []
    
    #for loop to find length  of words in lexicon == input word length
    for word in words_file:
        word = word.strip() #strip trailing \n
        word_length = len(word) #get length of word
        
        #if statement to find words with matching length as input length
        if word_length == input_word_length:
            matched_length.append(word) #append words to list wih matching length as input length
        else:
            pass
        
        #sort alphabetically
        matched_length.sort()      
    return matched_length #return list of words with matching word length as input length

# all words in search space have length = input_word_length
search_space = word_length_match(input_word_length, words_file)

################################################################################

# alphabet list
alphabet = [ 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# initialize empty list of lists to track matching letters
freq = [[] for letter in range(len(alphabet))] 

################################################################################


# letter match function
def letter_match(word, alphabet=alphabet, freq=freq):
    """
    function that tracks and matches each letter in the alphabet also found in the word
    parameters: input word, list of letters in the alphabet and empty freq list for each letter in the alphabet
    """

    word = list(word) #convert word to list of letters
    i = 0 #iterable
    
    #nested for loop to find matching letters 
    for letter_alphabet in alphabet:
        for letter_word in word:
            if letter_word == letter_alphabet: #find matching letters
                freq[i].append(letter_alphabet) #track all matching letters
            else:
                pass
        i += 1
    return freq #return list of lists with matching letters

################################################################################

letters_matched_search_space = [] #initialize empty list

# for loop to track matching letters of each word in the search space
for word in search_space:
    freq = [[] for letter in range(len(alphabet))] #initialize empty list of lists
    letters_matched_word = letter_match(word, alphabet, freq) #track matching letters 
    letters_matched_search_space.append(letters_matched_word) #append inner list to outer list

################################################################################
    
# letter_count function
def letter_count(freq, alphabet=alphabet):
    """
    function that counts frequencies of each letter in the alphabet
    parameters: freq list containing matching letters, and list of letters in the alphabet
    """

    my_freq_dict = {} #initialize empty dictionary to hold letter:frequency
    i = 0 #iterable
    
    # for loop to track counts of letters
    for i in range(len(freq)):
        counts = len(freq[i]) #count occurance of each letter
        my_freq_dict[alphabet[i]] = counts
        i += 1
    return my_freq_dict #retun dictionary of letter:frequency

################################################################################

freq_search_space = [] #initialize empty list to contain letter freq of words in search space

# for loop that generates a list of dictionaries
# each dictionary contains the letter:frequency for each word in the search space
for letters_matched_word in letters_matched_search_space:
    freq = letter_count(letters_matched_word, alphabet) #letter_count function
    freq_search_space.append(freq) #append dictionary to list

################################################################################

# find_anagrams function
def find_anagrams(input_word, input_word_counts, alphabet=alphabet, lexicon=search_space):
    """
    function that counts frequencies of each letter in the lexicon
    parameters are the input word, counts of each letter in the word, alphabet list and lexicon file
    """
    
    anagrams = [] #initialize empty list to attach matched anagrams
    
    #for loop to find anagrams of input word
    for word in lexicon:
        word = word.strip() #remove trailing white spaces \n
        freq = [[] for letter in range(len(alphabet))] #initialize empty list of 26*lists for each word in lexicon 
        letter_match(word, alphabet, freq) #letter_match function
        counts = letter_count(freq, alphabet) #letter_count function
        
        #a match is found if dictionary of lexicon letter counts = dictionary of input word's letter counts
        if counts == input_word_counts: #do not include the input word
            anagrams.append(word) #append anagram to anagrams list
        else:
            pass
    
    #sort anagrams list in alphabetical order
    anagrams.sort() 
    
    #return list of anagrams, where freq of letters in input word = freq of letters in lexicon words
    #If anagrams list is empty, return error message
    return anagrams if len(anagrams) > 0 else "Sorry, anagrams of '%s' could not be found." %input_word

################################################################################

all_anagrams = [] #initialize empty list to contain all anagrams

# for loop to find all anagrams in the search space 
for word, freq in zip(search_space, freq_search_space):
    list_anagrams = find_anagrams(word, freq, alphabet, search_space) #find_anagrams function
    if len(list_anagrams) > 1: #must be more than 1 word
        all_anagrams.append(list_anagrams) #append all anagrams to empty list

# ensure anagrams are not duplicates        
all_anagrams = set(map(tuple, all_anagrams))

# convert inner tuples to inner lists
all_anagrams = sorted(list(map(list, all_anagrams)))

################################################################################

# write all anagrams to output file
with open(out_file, "w") as out_file:
    for anagram in all_anagrams:
        out_file.write(str(anagram)+"\n") #include newline

################################################################################



    