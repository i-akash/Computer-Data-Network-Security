from string import ascii_lowercase
import re

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