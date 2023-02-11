from pythainlp import word_tokenize

text = 'นอนตากลมดูดาว'

result = word_tokenize(text, None, 'newmm', False)
print(result)