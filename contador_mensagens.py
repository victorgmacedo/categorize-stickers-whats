#
from re import *
file = open('C:\\Users\\victor.macedo\\Downloads\\whats\\_chat.txt', 'r', encoding="utf8")

patternAmor = compile(r'(\[\d{2}\/\d{2}\/\d{4} \d{2}:\d{2}:\d{2}\] Amor)')
patternEu = compile(r'(\[\d{2}\/\d{2}\/\d{4} \d{2}:\d{2}:\d{2}\] Victor)')

patternEuTeAmoAmor = compile(r'(Amor.*:.*Te Amo.*)', IGNORECASE)
patternEuTeAmoVictor = compile(r'(Victor.*:.*Te Amo.*)', IGNORECASE)

text = file.read()

iterator = finditer(patternAmor, text)

count = 0
for match in iterator:
    count += 1
print("Mensagens Ketley: " + str(count))

iterator = finditer(patternEu, text)
count = 0
for match in iterator:
    count += 1
print("Mensagens Victor: " + str(count))

iterator = finditer(patternEuTeAmoAmor, text)
count = 0
for match in iterator:
    count += 1
print("Mensagens de [te amo] Ketley: " + str(count))

iterator = finditer(patternEuTeAmoVictor, text)
count = 0
for match in iterator:
    count += 1
print("Mensagens de [te amo] Victor: " + str(count))