from textblob import TextBlob

a = 'cmputr'
b = TextBlob(a)

print('corrected text: ', b.correct())