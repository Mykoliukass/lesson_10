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
from typing import Union

three_or_more_sentences = ""
def check_sentences(string_to_check:str) -> bool:
    if string_to_check.count(".") < 3 or (string_to_check.count(".") == 3 and string_to_check[0]=="."):
        return True
    else:
        return string_to_check if string_to_check[0]!="." else string_to_check[1:]
def get_sentences() -> str:
    While True:
        three_or_more_sentences = input("Please provide me with three or more sentences. They should all end with a point '.': ")
        check_sentences(three_or_more_sentences)
print(three_or_more_sentences)
