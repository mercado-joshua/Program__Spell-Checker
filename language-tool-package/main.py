import language_tool_python

tool = language_tool_python.LanguageTool('en-US')

text = """
LanguageTool offers spell and grammar checking. Just paste your text here and click the ‘Check Text’ button. Click the colored phrases for details on potential errors. __or __use this text _**_too see an_ few _of of_ the problems that LanguageTool can _detecd_. What do you _thinks __of grammar checkers? Please __not __that they are not perfect. Style issues get a blue marker: It’s 5 __P.M. in the afternoon. __The weather was nice on __Thursday, 27 June 2017
"""

# get the matches
matches = tool.check(text)

# print(matches)

my_mistakes = []
my_corrections = []
start_positions = []
end_positions = []

for rules in matches:
    if len(rules.replacements)>0:
        start_positions.append(rules.offset)
        end_positions.append(rules.errorLength + rules.offset)
        my_mistakes.append(text[rules.offset:rules.errorLength + rules.offset])
        my_corrections.append(rules.replacements[0])

my_new_text = list(text)

for m in range(len(start_positions)):
    for i in range(len(text)):
        my_new_text[start_positions[m]] = my_corrections[m]
        if (i > start_positions[m] and i < end_positions[m]):
            my_new_text[i] = ''

my_new_text = ''.join(my_new_text)

print(my_new_text)