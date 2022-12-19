import json
import ast
import pandas as pd
from pythainlp.tokenize import word_tokenize

f = open('./accuracy/manual.json')
manual = json.load(f)
f.close()

'''Pythainlp'''
# newmm
newmm = './accuracy/newmm_df.csv'
df_newmm = pd.read_csv(newmm)

# deepcut
deepcut = './accuracy/deepcut_df.csv'
df_deepcut = pd.read_csv(deepcut)

# longest
longest = './accuracy/longest_df.csv'
df_longest = pd.read_csv(longest)

'''
    Accuracy calculate
'''
list_accuracy = []

def sort_index(value):
    return value[1]

def convert_to_list(text:str):
    return ast.literal_eval(text)

def word_tokenize_accuracy(reference, hypothesis):
  # Tokenize the reference and hypothesis strings
  reference_tokens = reference
  hypothesis_tokens = hypothesis

  # Calculate the number of correctly tokenized words
  correct_count = 0
  for i in range(min(len(reference_tokens), len(hypothesis_tokens))):
    # Check word by word
    # if reference_tokens[i] == hypothesis_tokens[i]:

    # Check some word in sentense
    if hypothesis_tokens[i] in reference_tokens:
      correct_count += 1

  # Calculate the accuracy as the number of correct tokens divided by the total number of tokens
  accuracy = correct_count / len(reference_tokens)
  return accuracy

# Calculate accuracy the word_tokenize_accuracy function
for i in range(100):
    hypothesis_newmm = convert_to_list(df_newmm.iloc[i]['detail'])
    hypothesis_deepcut = convert_to_list(df_deepcut.iloc[i]['detail'])
    hypothesis_longest = convert_to_list(df_longest.iloc[i]['detail'])
    reference = manual[f'{i}']

    accuracy_newmm = word_tokenize_accuracy(reference, hypothesis_newmm)
    accuracy_deepcut = word_tokenize_accuracy(reference, hypothesis_deepcut)
    accuracy_longest = word_tokenize_accuracy(reference, hypothesis_longest)
    # [newmm, deepcut, longest]
    list_accuracy.append([accuracy_newmm, accuracy_deepcut, accuracy_longest])


# Convert accuracy to percent
def percent_accuracy(score:list, digits:int) -> list:
    newmm_score = 0
    deepcut_score = 0
    longest_score = 0

    for i in range(len(score)):
        newmm_score += score[i][0]
        deepcut_score += score[i][1]
        longest_score += score[i][2]
    
    newmm_score = round(newmm_score, digits)
    deepcut_score = round(deepcut_score, digits)
    longest_score = round(longest_score, digits)
    return [newmm_score, deepcut_score, longest_score]

accuracy = percent_accuracy(list_accuracy, 2)

print(f'newmm: {accuracy[0]}%')
print(f'deepcut: {accuracy[1]}%')
print(f'longest: {accuracy[2]}%')