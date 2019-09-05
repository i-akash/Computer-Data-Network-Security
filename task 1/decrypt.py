from string import ascii_lowercase
import re


one=['a','i']
two=['of', 'to', 'in', 'it', 'is', 'be', 'as', 'at', 'so', 'we', 'he', 'by', 'or', 'on', 'do', 'if', 'me', 'my', 'up', 'an', 'go', 'no', 'us', 'am']
three=['the', 'and','for', 'are', 'but', 'not','you', 'all', 'any', 'can', 'had', 'her', 'was', 'one', 'our', 'out', 'day', 'get', 'has', 'him', 'his', 'how', 'new', 'now', 'old', 'see', 'two', 'way', 'who', 'boy', 'did','let', 'put', 'say', 'she', 'too']


def decrypt():

        mapper={}
        mapper['a']='b'
        mapper['b']='x'
        mapper['c']='i'
        mapper['d']='c'
        mapper['e']='l'
        mapper['g']='y'
        mapper['h']='o'
        mapper['j']='d'
        mapper['k']='t'
        mapper['l']='h'
        mapper['m']='n'
        mapper['n']='g'
        mapper['o']='a'
        mapper['p']='v'
        mapper['q']='u'
        mapper['r']='k'
        mapper['s']='f'
        mapper['t']='w'
        mapper['u']='e'
        mapper['v']='r'
        mapper['w']='m'
        mapper['y']='p'
        mapper['z']='s'

        words=[]
        with open('data.txt','r') as fd:
                lines=fd.readlines()
                paragraph=lines[0]
                
        for j in range(len(paragraph)):
                c=paragraph[j]
                if c in mapper:
                        paragraph=paragraph[:j]+str(mapper[c])+paragraph[j+1:]
        
        print("="*30,"decrypted paragraph","="*30)
        print()
        print(paragraph)
        print()

        

                        

def getUnique(list=[]):
        ret=[]
        for c in list:
                if c not in ret:
                        ret.append(c)

        return ret

def getWordFrequency(freq={},word=""):
        if word in freq:
                freq[word]=freq[word]+1
        else:
                freq[word]=1
        return freq

def printFreq(freq={},header="a"):
        print('\n',"="*30,header,"="*30)
        print()
        for key in sorted(freq.keys()):
                print(key," :",freq[key],end=" ")
        print('\n\n',"-"*80)




def analysis():
        words=[]
        oneLetterFreq={}
        twoLetterFreq={}
        threeLetterFreq={}



        with open('data.txt','r') as fd:
                lines=fd.readlines()
                
                line=lines[0]
                line=re.sub(","," ",line)
                line=re.sub("\.+"," ",line)
                line=re.sub("\!+"," ",line)
                line=re.sub(" +"," ",line)
                words=line.split(" ")



        for word in words:
                if len(word)==1:
                        oneLetterFreq=getWordFrequency(oneLetterFreq,word)

                if len(word)==2:
                        twoLetterFreq=getWordFrequency(twoLetterFreq,word)
                if len(word)==3:
                        threeLetterFreq=getWordFrequency(threeLetterFreq,word)
                        
        printFreq(oneLetterFreq,'one leter freq')
        printFreq(twoLetterFreq,'two leter freq')
        printFreq(threeLetterFreq,'three leter freq')


        freq={}
        for c in line:
                if c not in freq:
                        freq[c]=1
                else :
                        freq[c]=freq[c]+1
        
        print("="*30,"Character frequency","="*30)
        print()
        for c in sorted(freq.keys()):
                print(c," : ",freq[c],end=" ")
        print("\n","-"*80) 




analysis()
decrypt()