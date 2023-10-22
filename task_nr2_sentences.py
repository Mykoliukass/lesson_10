# Task nr.2:
# Create a program , which takes no less than 3 differnt sentences. The input should have all 
# error checking in mind. The program then should create a dictionary of whith key values 
# corresponding to words `long` (more than 9 letters in a words) `medium`(7 letters)
# `short` (5 words). Then the pgrogram should create a new sentences (if 3 provided, 3 new sentences should be returned) 
# with following rules attached:
# All sentences should have same (or less) words amount as entered one;
# The most frequent letter from the sentence (from input) should be dominated in a new sentence as well.

# The program should return new sentences with statitstics of ratio how many words was used from all sections 
# NECESSARY Short < 35% , medium: 25% , long 10%, words cannot repeat IN THE SAME sentence. 
# (as for exmpale: long 25%,medium 45%, short 30%)
# Trys ilgi sakiniai, turi būti su taškais būtinai and all.
from typing import Union, List, Dict

def check_sentences(input_text: str) -> Union[bool, List[str]]:
    sentences = [sentence.strip() for sentence in input_text.split('.') if sentence.strip()]
    if len(sentences) < 3:
        return False
    elif any(char in "!@#$%^&*(),-_=+[]{}|:'\"<>?/" for char in input_text):
        return False
    return sentences

def get_sentences() -> List[str]:
    while True:
        user_input = input("Please provide me with three or more sentences. They should all end with a period '.': ")
        result = check_sentences(user_input)
        if result:
            return result
        else:
            print("Invalid input. Please provide at least three different sentences. Make sure there are no other special symbols besides the dot.")

def words_to_dictionary_by_length(list_of_sentences: List[str]) -> Dict[str, List[str]]:
    dictionary_by_length = {'short': [], 'medium': [], 'long': []}
    clean_words = [remove_end_dot(word) for sentence in list_of_sentences for word in sentence.split()]
    [dictionary_by_length['short'].append(clean_word) for clean_word in clean_words if len(clean_word) < 5]
    [dictionary_by_length['long'].append(clean_word) for clean_word in clean_words if len(clean_word) >= 8]
    [dictionary_by_length['medium'].append(clean_word) for clean_word in clean_words if 5 <= len(clean_word) < 8]
    return dictionary_by_length

def remove_end_dot(word: str) -> str:
    return word.replace(".", "")

sentences = get_sentences()
print("You entered:", sentences)
print("Your dictionary:", words_to_dictionary_by_length(sentences))

