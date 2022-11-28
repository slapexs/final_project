# Find TF-IDF
import pandas as pd
import numpy as np
import string
from pythainlp.tokenize import word_tokenize
from pythainlp.corpus import thai_stopwords
from string import punctuation
import re

# TF-IDF
from sklearn.feature_extraction.text import TfidfVectorizer

class Findtfidf:
    def __init__(self, data_frame):
        self.data_frame = data_frame
    
    # Cut string
    def cut_string(self, text):
        self.regex_pat = f'[{punctuation}]'
        self.clean_split = re.sub(self.regex_pat, ' ', text)
        self.token = word_tokenize(
            text=self.clean_split,
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
        if (self.removal_word in self.stop_word) or self.removal_word.isdigit():
            return ""
        else:
            return self.removal_word
    

    '''
    Identity function
        function ที่ส่ง input ออกเป็น output ทันทีโดยไม่ได้ทำอะไร เพราะข้อมูลที่เราจะนำมาใช้เป็นภาษาไทยและเราได้ทำการเตรียมข้อมูลเบื้องต้นและเปลี่ยนให้อยู่ในรูปแบบ list เรียบร้อยแล้ว
        ref: https://bigdata.go.th/big-data-101/data-science/tf-idf-2/
    '''
    def identify_fun(self, split_text):
        return split_text
    
    # Create TfidfVectorizer
    def create_tfidfvectorizer(self):
        self.tfidf_vectorizer = TfidfVectorizer(
            analyzer='word',
            tokenizer=self.identify_fun,
            preprocessor=self.identify_fun,
            token_pattern=None
        )

        return self.tfidf_vectorizer