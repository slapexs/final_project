from findtfidf import Findtfidf
import pandas as pd
import numpy as np
from pythainlp.corpus import thai_stopwords

sample = './data_csv/combine_company.csv'
df = pd.read_csv(sample)
fnd_tfidf = Findtfidf(data_frame=df)

text = []

# Clean string comma
def clean_comma(text:list):
    temp = []
    for item in text:
        if item != ',':
            temp.append(item)

    return temp

for i in range(len(df)):
    temp_text = df.iloc[i]['รายละเอียดธุรกิจ']
    temp_cut = fnd_tfidf.cut_string(temp_text)
    text.append(clean_comma(temp_cut))


# Clean stop word
docs = []
stop_word_obj = thai_stopwords()
sets_stopword = [stop_word_obj]
list_stopword = [list(i) for i in sets_stopword]
for detail in text:
    doc = list(map(fnd_tfidf.perform_removal, detail))
    doc = list(filter(lambda word: (word not in list_stopword and word != ''), doc))
    docs.append(doc)


# sample
tfidf_vectorizer = fnd_tfidf.create_tfidfvectorizer()
tfidf_vector= tfidf_vectorizer.fit_transform(docs[100:106])
tfidf_array = np.array(tfidf_vector.todense())

# Train with all docs
tfidf_vector2 = tfidf_vectorizer.fit_transform(docs)
tfidf_array2 = np.array(tfidf_vector2.todense())



#แปลงเป็น DataFrame เพื่อง่ายแก่การอ่าน
# df1 = pd.DataFrame(tfidf_array,columns=tfidf_vectorizer.get_feature_names())
df2 = pd.DataFrame(tfidf_array2, columns=tfidf_vectorizer.get_feature_names_out())

# View top 10 ifidf score
# print(df1.apply(lambda s: s.nlargest(10).index.tolist(), axis=1).ravel())
print(df2.iloc[577:587, :].apply(lambda s: s.nlargest(5).index.tolist(), axis=1).ravel())