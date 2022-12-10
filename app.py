from pythainlp.tokenize import word_tokenize
from pythainlp.corpus import thai_stopwords
import pandas as pd
import numpy as np
import string
import nltk
# nltk.download('stopwords')
from nltk.corpus import stopwords

data = './data_csv/data_cleaned.csv'
df = pd.read_csv(data)

th_stopword = list(thai_stopwords())
eng_stopword = stopwords.words('english')
list_company_detail = []
th_number = ['๑','๒','๓','๔','๕','๖','๗','๘','๙','๐']

def clean_string(text:str) -> str:
    clean_token = text
    for pair in (('\n', ''), ('\t', ''), ('!', '')):
        clean_token =clean_token.replace(*pair)

    clean_token = clean_token.translate(str.maketrans('','',string.punctuation))
    clean_token = str(clean_token).translate(str.maketrans('','',string.digits))
    return clean_token

def clean_stopword(token:list) -> list:
    temp = []
    for i in token:
        if i not in th_stopword and i not in eng_stopword and i not in th_number:
            temp.append(i)
    return temp

for i in range(len(df)):
    sample = clean_string(str(df.iloc[i]['รายละเอียดธุรกิจ']).lower())
    text_cleaned = clean_stopword(word_tokenize(sample, None, 'newmm', False))
    list_company_detail.append(text_cleaned)

'''
    TFI-DF
'''
from sklearn.feature_extraction.text import TfidfVectorizer
def fake_tokenize(word):
    return word

vectorizer = TfidfVectorizer(
    analyzer='word',
    tokenizer=fake_tokenize,
    preprocessor=fake_tokenize,
    token_pattern=None
)

reject = [' ่',' ์',' ์ฟแวร์',' ์ส'' ํา',' ํากกว่ํา',' ํารวจ',' ําหนด',' ําะ',' ําา',' ําเนิด',' ํา้านม']

tfidf_vector = vectorizer.fit_transform(list_company_detail)
tfidf_array = np.array(tfidf_vector.todense())
df_tfidf = pd.DataFrame(tfidf_array, columns=vectorizer.get_feature_names_out())
df_tfidf = df_tfidf.drop(df_tfidf.columns[[k for k in range(-15, 0, 1)]],axis = 1)

print(df_tfidf)
