from textblob import TextBlob

sentence = ['inconsstent', 'roght estemate']

textblob_objects = []

for word in sentence:
    textblob_objects.append(TextBlob(word))

for textblob_object in textblob_objects:
    print(textblob_object.correct())