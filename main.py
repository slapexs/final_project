from findtfidf import Findtfidf
import pandas as pd
import numpy as np

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
for detail in text:
    doc = list(map(fnd_tfidf.perform_removal, detail))
    doc = list(filter(lambda word: (word != ''), doc))
    docs.append(doc)


# sample
tfidf_vectorizer = fnd_tfidf.create_tfidfvectorizer()
tfidf_vector= tfidf_vectorizer.fit_transform(docs[10:106])
tfidf_array = np.array(tfidf_vector.todense())

#แปลงเป็น DataFrame เพื่อง่ายแก่การอ่าน
df1 = pd.DataFrame(tfidf_array,columns=tfidf_vectorizer.get_feature_names())

# View top 10 ifidf score
print(df1.apply(lambda s: s.nlargest(10).index.tolist(), axis=1).ravel())