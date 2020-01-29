import nltk
from nltk.corpus import stopwords
import re

txt = open("text.txt","r")
content = txt.read()

text = re.sub(r'\[[0-9]*\]',' ',content)
#text = re.sub(r'\s+',' ',text)
text = re.sub(r'\.',' ',text)
text = re.sub(r'\,',' ',text)
text = text.lower()
text = re.sub(r'\d',' ',text)
text = re.sub(r'\s+',' ',text)
#print(text)
sentences = nltk.sent_tokenize(text)
sentences = [nltk.word_tokenize(sentence) for sentence in sentences]
for i in range(len(sentences)):
    sentences[i] = [word for word in sentences[i] if word not in stopwords.words('english')]
duplicate = []
for i in range(len(sentences)):
	for word in sentences[i]:
		if word not in duplicate:
			duplicate.append(word)
print(duplicate)
length = len(duplicate)
matrix =[]
for i in range(length):
	sub = []
	for j in range(length):
		if(i==j):
			sub.append(text.count(duplicate[i]))
		else:
			sub.append((text.count(duplicate[i]+" "+duplicate[j]))+(text.count(duplicate[j]+" "+duplicate[i])))
	matrix.append(sub);
values=[]
for i in range(length):
	total = 0
	val = 1
	for j in range(length):
		if(i == j):
			val = matrix[i][j]
		else:
			total += matrix[i][j]
	values.append(float(total/val))

for i in range(length):
	print(duplicate[i], values[i])
final = []
st = ""
for i in range(length-1):
	if(values[i]==values[i+1]):
		st = duplicate[i]+" "+duplicate[i+1]
		index = i+1
		while(index<length-1):
			if(values[index]==values[index+1]):
				st = st + values[index+1]
				index = index+1
			else:
				final.append(st)
				break
		i = index - 1

print(final)
	
