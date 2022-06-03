import random

"""Word Finder: finds random words from a dictionary."""

with open('simple.txt') as file:
    file_contents = file.read()
    print(file_contents) 
    print(type(list(file_contents))) 



# class WordFinder:
#     ...

#     # wf = open("words.txt", "r")
      
#     # for word in wf:
#     #     return random.choices(word)

#     def __init__(self, path):
#         file = open(path)
#         self.words = file.readlines()

#         print(f"{len(self.words)} words read")
    
#     def random(self):
#         """Return random word(s)"""
#         return random.choice(self.words)
