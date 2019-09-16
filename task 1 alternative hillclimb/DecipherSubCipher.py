from string import ascii_lowercase as lowletter
from math import log10 
from fitnessScore import FitnessTest
import random
import threading

class DecipherSubCipher:
    def __init__(self,fitnessfile="quadgrams.txt",cipherfile="data.txt"):
        self.cipherfile=cipherfile
        self.fitnessfile=fitnessfile
        self.t1=threading.Thread(target=self.readCipherText)
        self.t2=threading.Thread(target=self.initFitnessTest)
        self.t1.start()
        self.t2.start()

    def readCipherText(self):
        with open(self.cipherfile,'r') as fd:
            self.cipherText=fd.readlines()[0].lower()

    def initFitnessTest(self):
        self.fitnessTest=FitnessTest(self.fitnessfile)

    
    def decrypt(self,key=list(lowletter)):

        decipherText=list(self.cipherText)
        for j in range(len(decipherText)):
            c=decipherText[j]
            if c in lowletter:
                index=ord(c)-97
                decipherText[j]=key[index]
        return ''.join(decipherText)


    def climb(self):
        score=-99e9
        key=list(lowletter)
        parentScore,parentKey=score,key
        i=0
        self.t1.join()
        self.t2.join()
        
        while True:
            i=i+1
            random.shuffle(parentKey)
            decryptText=self.decrypt(parentKey)
            parentScore=self.fitnessTest.getScore(decryptText)
            count=0
            while count<1000:
                childkey=parentKey[:]
                a=random.randint(0,25)
                b=random.randint(0,25)

                childkey[a],childkey[b]=childkey[b],childkey[a]
                decryptText=self.decrypt(childkey)
                childScore=self.fitnessTest.getScore(decryptText)

                if childScore>parentScore:
                    parentScore=childScore
                    parentKey=childkey[:]
                    count=0
                count=count+1
                if parentScore>score:
                    score=parentScore
                    key=parentKey[:]

                    print '\nbest score so far:',score,'on iteration',i
                    print '    best key: '+''.join(key)
                    print '    Text: '+self.decrypt(key)




decipher=DecipherSubCipher()
decipher.climb()