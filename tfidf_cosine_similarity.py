from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd
from pythainlp.tokenize import word_tokenize
from pythainlp.corpus import thai_stopwords

df = pd.read_csv('./document/clustered_company.csv')
th_stopword = list(thai_stopwords())

keyword = 'บริการลักษณะ Digital Solution (Marketing) Agency - Online marketing'

cluster = 7
def segment_and_clean_text(text):
    words = word_tokenize(text, None, 'newmm', False)
    cleaned_words = [word for word in words if word not in th_stopword]
    return "".join(cleaned_words)

def calculate_socine(keyword, cluster_detail):
    keyword_search = segment_and_clean_text(keyword)
    detail = segment_and_clean_text(cluster_detail)
    vectorizer = TfidfVectorizer()
    # Fit the vectorizer to the tokenized documents
    vectors = vectorizer.fit_transform([keyword_search, detail])

    # Calculate the cosine similarity between the two documents
    similarity = cosine_similarity(vectors, vectors)

    return similarity[0][1]

cluster_detail = []
for c in range(cluster):
    temp = ""
    for i in range(len(df)):
        if df.iloc[i]['cluster'] == c:
            temp = "".join(df.iloc[i]['detail'])
    cluster_detail.append(temp)

cosine_values = []
for k in range(len(cluster_detail)):
    cosine_values.append(calculate_socine(keyword, cluster_detail[k]))
print(cosine_values)
print(f'max cosine similarity: {max(cosine_values)}')
print(f'cluster: {cosine_values.index(max(cosine_values))}')