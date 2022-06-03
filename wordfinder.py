import random

"""Word Finder: finds random words from a dictionary."""

class WordFinder:
    ...

    def __init__(self, path):
        """Read dictionary """

        file = open(path)
        self.words = self.parse(file)
        print(f"{len(self.words)} words read")
    

    def parse(self, file):
        """Parse file into list"""

        list = []
        for word in file:
            w = word.strip()
            list.append(w)
        return list
        # return [word.strip() for word in file]


    def random(self):
        """Return random word(s)"""

        return random.choice(self.words)
