from pythainlp.tokenize import word_tokenize
import pandas as pd

rawf = '../../file_test_accuracy/cleaned_companies.csv'
raw_df = pd.read_csv(rawf)
n = 190
# cut_newmm = word_tokenize(raw_df.iloc[n]['รายละเอียดธุรกิจ'], None, 'newmm', False)
# cut_longest = word_tokenize(raw_df.iloc[n]['รายละเอียดธุรกิจ'], None, 'longest', False)
# cut_deepcut = word_tokenize(raw_df.iloc[n]['รายละเอียดธุรกิจ'], None, 'deepcut', False)
print(raw_df.iloc[n]['รายละเอียดธุรกิจ'])