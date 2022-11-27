# Find TF-IDF
import pandas as pd
import numpy as np
import string
from pythainlp.tokenize import word_tokenize
from pythainlp.corpus import thai_stopwords


class Findtfidf:
    def __init__(self, data_frame):
        self.data_frame = data_frame
    
    # Cut string
    def cut_string(self, text):
        self.text = text
        self.token = word_tokenize(
            text=self.text,
            engine='newmm',
            keep_whitespace=False
        )

        return self.token

    # Stop word
    def perform_removal(self, word):
        self.stop_word = thai_stopwords()
        # Stirp
        self.removal_word = word.strip()
        # Change upper to lower
        self.removal_word = self.removal_word.lower()
        # Clean stop word
        if self.removal_word in self.stop_word:
            return ""
        else:
            return self.removal_word


        
    