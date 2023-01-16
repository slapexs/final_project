from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd
from pythainlp.tokenize import word_tokenize
from pythainlp.corpus import thai_stopwords

df = pd.read_csv('./document/clustered_company.csv')
th_stopword = list(thai_stopwords())

keyword = 'บริการลักษณะ Digital Solution (Marketing)'

class Calculate_cosinesim:
    def __init__(self, keyword, amount_cluster:int, df) -> None:
        self.keyword = keyword
        self.cluster = amount_cluster
        self.df = df
    
    # Filter detail by cluster
    def filter_detail(self):
        self.cluster_detail = []
        for c in range(self.cluster):
            temp = []
            for i in range(len(self.df)):
                if self.df.iloc[i]['cluster'] == c:
                    temp.append(self.df.iloc[i]['detail'])
            self.cluster_detail.append(temp)
        return self.cluster_detail
    
    def segment_and_clean_text(self, text):
        self.words = word_tokenize(text, None, 'newmm', False)
        self.cleaned_words = [word for word in self.words if word not in th_stopword]
        return "".join(self.cleaned_words)
    
    def cluster_wordseg(self):
        self.temp = []
        for c in range(self.cluster):
            self.temp_detail = "".join(self.filter_detail()[c])
            self.temp.append(self.segment_and_clean_text(self.temp_detail))
            
        return self.temp

    def calculate_cosine(self, detail):
        self.keyword = self.segment_and_clean_text(self.keyword)
        self.detail = self.segment_and_clean_text(detail)
        self.vectorizer = TfidfVectorizer()
        self.vector = self.vectorizer.fit_transform([self.keyword, self.detail])
        self.similarity = cosine_similarity(self.vector, self.vector)
        return self.similarity

    def response_cosine(self):
        return [self.calculate_cosine(i)[0][1] for i in self.cluster_wordseg()]
