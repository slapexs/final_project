from findtfidf import Findtfidf
import pandas as pd

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

print(docs)