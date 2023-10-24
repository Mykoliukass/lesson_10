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

from typing import Union, List, Dict, Set

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
    # Filter out non-alphabetic characters and convert to lowercase
    clean_sentence = ''.join(char.lower() for char in sentence if char.isalpha())

    letter_counts = {letter: clean_sentence.count(letter) for letter in set(clean_sentence)}
    most_frequent_letter = max(letter_counts, key=letter_counts.get)
    return most_frequent_letter

def calculate_word_ratios(sentences: List[str]) -> Dict[str, float]:
    total_words = 0
    short_words = 0
    medium_words = 0
    long_words = 0

    for sentence in sentences:
        words = [word.strip(".,!?") for word in sentence.split()]
        total_words += len(words)

        for word in words:
            word_class = classify_word(word)
            if word_class == 'short':
                short_words += 1
            elif word_class == 'medium':
                medium_words += 1
            elif word_class == 'long':
                long_words += 1

    # Check if total_words is zero to avoid dividing by zero
    if total_words == 0:
        return {'short': 0, 'medium': 0, 'long': 0}

    short_ratio = (short_words / total_words) * 100
    medium_ratio = (medium_words / total_words) * 100
    long_ratio = (long_words / total_words) * 100

    return {'short': short_ratio, 'medium': medium_ratio, 'long': long_ratio}

def print_ratios(ratios: Dict[str, float], decimal_places: int = 2) -> None:
    for length, ratio in ratios.items():
        rounded_ratio = round(ratio, 2)
        print(f"{length.capitalize()} Words: {rounded_ratio}%")

def generate_new_sentence(original_sentence: str, word_dict: Dict[str, List[str]]) -> Union[str, None]:
    words = [word.strip(".,!?") for word in original_sentence.split()]
    most_frequent_letter = find_most_frequent_letter(original_sentence)

    # Initialize lists to keep track of word lengths in the new sentence
    short_words = []
    medium_words = []
    long_words = []

    # Initialize a set for already used words
    used_words = set()

    new_sentence = []

    # Calculate the desired number of short, medium, and long words
    total_words = len(words)
    target_short = int(0.35 * total_words)
    target_medium = int(0.25 * total_words)
    target_long = int(0.1 * total_words)

    # Set a limit on the number of attempts to generate a sentence
    max_attempts = 100
    attempts = 0

    while (
        len(short_words) < target_short or
        len(medium_words) < target_medium or
        len(long_words) < target_long
    ) and attempts < max_attempts:
        for word in words:
            word_class = classify_word(word)

            if word_class in word_dict:
                replacement_word = get_word_for_letter(word_dict[word_class], most_frequent_letter, used_words)

                # If a replacement word is found, add it to the used_words set
                if replacement_word:
                    used_words.add(replacement_word)
                    new_sentence.append(replacement_word)

                    # Updating the number of each word length count
                    update_word_counts(word_class, replacement_word, short_words, medium_words, long_words)
                else:
                    # If no suitable replacement is found, break and retry generating a new sentence
                    new_sentence = []
                    short_words = []
                    medium_words = []
                    long_words = []
                    break
        attempts += 1

    if (
        len(short_words) >= target_short and
        len(medium_words) >= target_medium and
        len(long_words) >= target_long
    ):
        result_sentence = ' '.join(new_sentence) + "."
        return result_sentence
    else:
        return None  # Indicate that it's not possible to create a sentence with the given requirements

def get_word_for_letter(word_list: List[str], target_letter: str, used_words: Set[str]) -> str:
    # Filter words that contain the target letter
    filtered_words = [word for word in word_list if target_letter in word]

    # Remove words that have already been used in this sentence
    filtered_words = [word for word in filtered_words if word not in used_words]

    # If there are available words, return the first one; otherwise, return an empty string
    return filtered_words[0] if filtered_words else ""

def update_word_counts(word_class: str, word: str, short_words: List[str], medium_words: List[str], long_words: List[str]) -> None:
    if word_class == 'short':
        short_words.append(word)
    elif word_class == 'medium':
        medium_words.append(word)
    elif word_class == 'long':
        long_words.append(word)
def get_all_new_sentences():
    sentences = get_sentences()
    word_dict = create_word_dictionary(sentences)
    new_sentences = []

    print("\nOriginal Sentences:")
    for i, sentence in enumerate(sentences, start=1):
        print(f"{i}. {sentence}")

        new_sentence = generate_new_sentence(sentence, word_dict)
        if new_sentence is not None:
            new_sentences.append(new_sentence)
            ratios = calculate_word_ratios([new_sentence])
            print(f"\nGenerated Sentence {i}:")
            print(new_sentence)
            print("\nWord Ratios in Generated Sentence:")
            print_ratios(ratios)
        else:
            print(f"\nCould not generate a sentence for Original Sentence {i}.")

    if new_sentences:
        print("\nCombined Generated Sentences:")
        for new_sentence in new_sentences:
            print(new_sentence)

        ratios = calculate_word_ratios(new_sentences)
        print("\nWord Ratios in Combined Generated Sentences:")
        print_ratios(ratios)

get_all_new_sentences()

