import random

"""Word Finder: finds random words from a dictionary."""

class WordFinder:
    ...

    def __init__(self, path):
        """Read dictionary 
        >>> wf = WordFinder('simple.txt')
        3 words read
        >>> wf.random() in ["cat", "dog", "chicken"]
        True
        """

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


class SpecialWordFinder(WordFinder):

    """Ensures only returns words, not spaces/comments
    >>> swf = SpecialWordFinder("special.txt")
    3 words read

    >>> swf.random() in ['kale', 'parsnips', 'apple', 'mango']
    True
    """

    def parse(self, file):
        return [word.strip() for word in file if word.strip() and not word.startswith('#')]