import pandas as pd
import numpy as np
from pythainlp.tokenize import word_tokenize
from pythainlp.corpus import thai_stopwords
import nltk
# nltk.download('stopwords')
from nltk.corpus import stopwords
import matplotlib.pyplot as plt
import string
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer

data = './document/clustered_company.csv'
df = pd.read_csv(data)

th_stopword = list(thai_stopwords())
eng_stopword = stopwords.words('english')
list_company_detail = []
th_number = ['๑','๒','๓','๔','๕','๖','๗','๘','๙','๐']
spx_char = ['”', '-', '),', '\"', '…', '​', '​​', '​“', '‎', '–', '‘', '’', '“', '•', '™', '≥', '\n', '\t', '!', 'aaa']

def clean_string(detail:list) -> list:
    temp_clean = []
    for i in detail:
        if i not in string.punctuation and i not in string.digits and i not in spx_char and i not in th_number:
            temp_clean.append(i.lower())
    return ''.join(temp_clean)

def clean_stopword(token:list) -> list:
    temp = []
    for i in token:
        if i not in th_stopword and i not in eng_stopword and i not in th_number:
            temp.append(i)
    return temp

cluster = 6
keyword = 'ออกแบบเว็บไซต์ด้วย react js ทำเกี่ยวกับการเขียนเว็บ การตลาดออนไลน์ด้วย และ SEO'
search_keyword = clean_stopword(word_tokenize(clean_string(str(keyword).lower()), None, 'newmm', False))

documents = []
for i in range(len(df)):
    if df.iloc[i]['cluster'] == cluster:
        sample = clean_string(str(df.iloc[i]['detail']).lower())
        text_cleaned = clean_stopword(word_tokenize(sample, None, 'newmm', False))
        documents.append(text_cleaned)

def fake_tokenize(word):
    return word

vectorizer = TfidfVectorizer(
    analyzer='word',
    tokenizer=fake_tokenize,
    preprocessor=fake_tokenize,
    token_pattern=None,
    lowercase=True,
)

'''
    TF-IDF search keyword
'''
search_vector = vectorizer.fit_transform(search_keyword)
search_array = np.array(search_vector.todense())
df_tfidf_search = pd.DataFrame(search_array, columns=vectorizer.get_feature_names_out())
maxlength = len(df_tfidf_search.columns)
ans_search = []
for k in df_tfidf_search.iloc[0]:
    ans_search.append(k)
    ans_search.sort(reverse=True)

'''
    TFI-DF cluster document
'''

tfidf_vector = vectorizer.fit_transform(documents)
tfidf_array = np.array(tfidf_vector.todense())
df_tfidf_cluster = pd.DataFrame(tfidf_array, columns=vectorizer.get_feature_names_out())
word_in_cluster = [w for w in df_tfidf_cluster.columns]

def create_word_in_table(keyword, columns):
    temp = []
    for i in range(len(keyword)):
        for k in range(len(columns)):
            if keyword[i] == columns[k]:
                temp.append(int(k))
    # Create table
    table = [0 for zero in range(len(columns))]
    for i in temp:
        table[i] = 1
    return table

table_of_columns = [[1 for i in range(len(word_in_cluster))]]
table_of_keyword = [create_word_in_table(search_keyword, word_in_cluster)]

'''
    Cosine similarity
'''
cosine_sim = cosine_similarity(table_of_columns, table_of_keyword)
print(f'Keyword: {search_keyword}')
print(f'cluster: {cluster}\ncosine similarity: {cosine_sim[0][0]}')

