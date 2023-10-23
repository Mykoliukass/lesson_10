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
# from typing import Union, List, Dict
# import random 
# def check_sentences(input_text: str) -> Union[bool, List[str]]:
#     sentences = [sentence.strip() for sentence in input_text.split('.') if sentence.strip()]
#     if len(sentences) < 3:
#         return False
#     return sentences

# def get_sentences() -> List[str]:
#     while True:
#         user_input = input("Please provide me with three or more sentences. They should all end with a period '.': ")
#         result = check_sentences(user_input)
#         if result:
#             return result
#         else:
#             print("Invalid input. Please provide at least three different sentences. Make sure there are no other special symbols besides the dot.")

# def words_to_dictionary_by_length(list_of_sentences: List[str]) -> Dict[str, List[str]]:
#     dictionary_by_length = {'short': [], 'medium': [], 'long': []}
#     clean_words = [remove_end_dot(word) for sentence in list_of_sentences for word in sentence.split()]
#     [dictionary_by_length['short'].append(clean_word) for clean_word in clean_words if len(clean_word) < 5]
#     [dictionary_by_length['long'].append(clean_word) for clean_word in clean_words if len(clean_word) > 9]
#     [dictionary_by_length['medium'].append(clean_word) for clean_word in clean_words if 5 <= len(clean_word) <= 9]
#     return dictionary_by_length

# def remove_end_dot(word: str) -> str:
#     return word.replace(".", "")

# sentences = get_sentences()

# From the clasified words we can take one and replace the old one in the original sentence with this word.
# Then we could shuffle those words around shuffled_list = random.sample(original_list, len(original_list))
# To take a random word from a list of strings: random_string = random.choice(my_list)


from typing import Union, List, Dict
import random

def check_sentences(input_text: str) -> Union[bool, List[str]]:
    sentences = [sentence.strip() for sentence in input_text.split('.') if sentence.strip()]
    if len(sentences) < 3:
        return False
    return sentences
def get_sentences() -> List[str]:
    while True:
        user_input = input("Please provide me with three or more sentences. They should all end with a period '.': ")
        result = check_sentences(user_input)
        if result:
            return result
        else:
            print("Invalid input. Please provide at least three different sentences.")
def classify_word(word: str) -> str:
    if len(word) > 9:
        return 'long'
    elif 8 >= len(word) >= 6:
        return 'medium'
    else:
        return 'short'
def create_word_dictionary(sentences: List[str]) -> Dict[str, List[str]]:
    dictionary_by_length = {'short': [], 'medium': [], 'long': []}
    for sentence in sentences:
        clean_words = [remove_end_dot(word) for word in sentence.split()]
        [dictionary_by_length['short'].append(clean_word) for clean_word in clean_words if len(clean_word) < 5]
        [dictionary_by_length['long'].append(clean_word) for clean_word in clean_words if len(clean_word) >= 8]
        [dictionary_by_length['medium'].append(clean_word) for clean_word in clean_words if 5 <= len(clean_word) < 8]
    return dictionary_by_length
def remove_end_dot(word: str) -> str:
    return word.replace(".", "")
def find_most_frequent_letter(sentence: str) -> str:
    letter_counts = {letter: sentence.count(letter) for letter in set(sentence)}
    most_frequent_letter = max(letter_counts, key=letter_counts.get)
    return most_frequent_letter
def generate_new_sentence(original_sentence: str, word_dict: Dict[str, List[str]]) -> str:
    words = [word.strip(".,!?") for word in original_sentence.split()]
    most_frequent_letter = find_most_frequent_letter(original_sentence)
    new_sentence = [word_dict[classify_word(word)].pop(0) if word_dict[classify_word(word)] else word for word in words]
    result_sentence = ' '.join(new_sentence) + "."
    return result_sentence
def get_all_new_sentences():
    sentences = get_sentences()
    word_dict = create_word_dictionary(sentences) 
    new_sentences = []
    for sentence in sentences:
        new_sentence = generate_new_sentence(sentence, word_dict)
        new_sentences.append(new_sentence)
    
    print("\nOriginal Sentences:")
    for sentence in sentences:
        print(sentence)
    
    print("\nGenerated Sentences:")
    for new_sentence in new_sentences:
        print(new_sentence)

get_all_new_sentences()