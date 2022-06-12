from nltk.corpus import wordnet
from string import ascii_lowercase

def has_numbers(str):
    return any(char.isdigit() for char in str)

def convert_to_number(word):
    #Make letter to number conversion dict, where a = 1
    letters_to_numbers = {letter:(number + 1) for number, letter in enumerate(ascii_lowercase)}

    #Iterate through letters, convert, and sum
    word_value = 0
    for char in word:
        if(char.isalpha()): #to ignore symbols e.g. dashes, underscores
            word_value += letters_to_numbers.get(char)
            #print(letters_to_numbers.get(char))

    return word_value

#Get all words in wordnet
all_words = wordnet.words()

#Isolate words that don't contain numbers
#num_words = 0
words = []

#Test: view all words that contain numbers -- none of these are normal words
#for word in all_words:
#    if has_numbers(word):
#        print(word)

for word in all_words:
    if not has_numbers(word):
        #print(word)
        words.append(word)
        #num_words += 1

#print(num_words) -- 146722

#Make dict to map words to values
words_to_values = {word:0 for word in words}

#Fill dict
for word in words:
    words_to_values[word] = convert_to_number(word)

count_even = 0
count_odd = 0

for word in words:
    if(words_to_values[word] % 2 == 0):
        count_even += 1
    else:
        count_odd += 1

print("Even:", count_even)
print("Odd:", count_odd)
