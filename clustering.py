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
spx_char = ['”', '-', '),', '\"', '…', '​', '​​', '​“', '‎', '–', '‘', '’', '“', '•', '™', '≥']


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

k = 8
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
# plt.figure(figsize=(10, 5))
# # set a title
plt.title("Group of companies", fontdict={"fontsize": 18})
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