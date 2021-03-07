from textblob import TextBlob

file1 = open('1.txt', 'r+')

a = file1.read()

print('original text: ', str(a))

b = TextBlob(a)

print('corrected text: ', str(b.correct()))

file1.close()

# overrides the text
c = open('1.txt', 'w')
c.write(str(b.correct()))
c.close()