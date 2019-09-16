from math import log10

class FitnessTest:
    def __init__(self,trainFile,sep=' '):
        self.ngramsProbability={}
        self.Total=0

        for line in open(trainFile):
            key,count=line.split(sep)
            self.ngramsProbability[key]=int(count) 
            self.Total=self.Total+int(count)

        self.Length=len(key)
        for key in self.ngramsProbability.keys():
            self.ngramsProbability[key]=log10(float(self.ngramsProbability[key])/self.Total)
        
        self.minimumProbability=log10(0.01/self.Total)
    
    def getScore(self,text=""):
        score=0
        for pos in xrange(len(text)-self.Length+1):
            key=text[pos:pos+self.Length]
            key=key.upper()
            if key in self.ngramsProbability:
                score=score+self.ngramsProbability[key]
            else :
                score=score+self.minimumProbability
        return score
   
