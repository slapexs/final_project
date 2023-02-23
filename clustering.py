from pythainlp.tokenize import word_tokenize
from pythainlp.corpus import thai_stopwords
import pandas as pd
import numpy as np
import string
import nltk
# nltk.download('stopwords')
from nltk.corpus import stopwords

data = './file_test_accuracy/test.csv'
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
    token_pattern=None,
    lowercase=True,
)


# Train
tfidf_vector = vectorizer.fit_transform(list_company_detail)
# print(tfidf_vector.shape)
tfidf_array = np.array(tfidf_vector.todense())
df_tfidf = pd.DataFrame(tfidf_array, columns=vectorizer.get_feature_names_out())
df_tfidf = df_tfidf.drop(df_tfidf.columns[[k for k in range(-15, 0, 1)]], axis = 1)


'''
    KMeans clustering
'''
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

X = df_tfidf
scaler = StandardScaler()
X = scaler.fit_transform(df_tfidf)

# centroids
pca = PCA(n_components=len(df_tfidf))
pca_vecs = pca.fit_transform(df_tfidf)
x_value = pca_vecs[:, 0]
y_value = pca_vecs[:, 1]
df_tfidf['x_value'] = x_value
df_tfidf['y_value'] = y_value

k = 6
kmeans = KMeans(n_clusters=k)
# # Fit model
kmeans.fit(df_tfidf[['x_value', 'y_value']])
clusters = kmeans.labels_

'''
    Visualize the Clustering
'''
df_tfidf['cluster'] = clusters


import matplotlib.pyplot as plt
# # set image size
plt.figure(figsize=(12, 6))
# # set a title
plt.title(f'{k} groups', fontdict={"fontsize": 18})
# # set axes names
plt.xlabel("X", fontdict={"fontsize": 16})
plt.ylabel("Y", fontdict={"fontsize": 16})
# # create scatter plot with seaborn, where hue is the class used to group the data
plt.scatter(x_value, y_value, c=clusters, cmap="Set2")
centroids = kmeans.cluster_centers_
# # centroids
plt.scatter(centroids[:,0], centroids[:,1], marker='x', c='red')
# plt.show()
plt.savefig(f"./screenshort/{k}_cluster.png")