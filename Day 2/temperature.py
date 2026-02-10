import nltk
from nltk.tokenize import word_tokenize

text = "temperature control in genai by adjusting the number of tokens used in the input to influence the creativity of the output response by setting a lower temperature value for more factual responses and a higher temperature value for more creative responses.You need to call Python explicitly with the file path. You can't just type the path directly in PowerShell." 
tokens = word_tokenize(text)

token_length = len(tokens)

# temperature conditions
if token_length <= 5:
    temperature = 0.2
    temp = "factual"
elif token_length <= 15:
    temperature = 0.6
    temp = "balanced"
else:
    temperature = 0.9
    temp = "creative"
print("Selected temperature:", temperature)
print("Temperature type:", temp)
