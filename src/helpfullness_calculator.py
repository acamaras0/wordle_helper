
class HelpFull:
    def __init__(self):
        pass

    def _assign_word_helpfullness(self, word: str, words: list):
        pass

    def get_helpfullness_word_tuples(self, words: list):
        for word in words:
            self._assign_word_helpfullness(word, words)


"""
 _______________________________________________
/ To give best suggestions first, we should     \ 
| make the words into tuples (helpfulness, word) |
|                                                |
| This is in order to be able to hash them by    |
| order of likely helpfullness...                |
|                                                |
| Which in turn we can calculate by iterating    |
| words and calculating how many words would be  |
\ left on average after that guess...           /
 -----------------------------------------------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/
                ||----w |
                ||     ||
"""""""""""""""""""""""""""""""""""""""""""""""""""
