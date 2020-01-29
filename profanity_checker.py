'''def profanity_checker(words):
        output = []
#	for keys in words:
#		key_word = keys.split()
#		print(key_word)
        for word in words:
                out = search_word_in_file(word) 
                if(out != 'None'):
                        output.append(out)
        return output


def search_word_in_file( word ):
        f = open("profanity.txt","r")
        profanity_file = f.read()
        if word in profanity_file:
                print
'''
from profanity_check import predict, predict_prob
f = open("profanity.txt","r")
inputs = f.read().split('\n')
o1 = open("output1.txt","w")
o2 = open("output2.txt","w")
for word in inputs:
        if(predict([word])==0):
                st = word+"    "+str(predict_prob([word]))+"\n"
                o1.write(st)
        else:
                st = word+"    "+str(predict_prob([word]))+"\n"
                o2.write(st)
