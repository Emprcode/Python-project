# """Task no 1:
# you are working on a search engine. the given code takes a text and a word as input and passes them to a function called search().
# The search() function should return "Word found" if the word is present in the text, or "Word not found", if its not. """

# text = str(input())
# word =  str(input())

# def search(text, word):
#     if (word in text):
#         return "Word found"
#     else:
#         return "word not found"

# result = search(text, word)
# print(result)

# """ you need to  make a program for a leaderboard. THe program needs to output the numbers output 1 to 9, each on a seprate line, followed by dot"""

# print("""
# 1.
# 2.
# 3.
# 4.
# 5.
# 6.
# 7.
# 8.
# 9.
# """)

# tips calculator

bill  = int(input("Enter the bill amount: "))
tip = float((bill*25)/100)

print(tip)