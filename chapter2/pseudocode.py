"""Palingrams"""
# Load digital dictionary as a list of words
# Start an empty list to hold palingrams
# For word in word list:
#     Get length of word
#     If length > 1:
#         Loop through the letters in the word:
#             If reversed word fragment at front of word is in word list and letters
#             after form a palindromic sequence:
#                Append word and reversed word to palingram list
#             If reversed word fragment at end of word is in word list and letters
#             before form a palindromic sequence:
#                Append reversed word and word to palingram list
# Sort palingram list alphabetically
# Print word-pair palingrams from palingram list



"""Palindromes"""
# Load digital dictionary file as a list of words
# Create an empty list to hold palindromes
# Loop through each word in the word list:
#    If word sliced forward is the same as word sliced backward:
#       Append word to palindrome list
# Print palindrome list
