from string import ascii_lowercase
import re


one=['a','i']
two=['of', 'to', 'in', 'it', 'is', 'be', 'as', 'at', 'so', 'we', 'he', 'by', 'or', 'on', 'do', 'if', 'me', 'my', 'up', 'an', 'go', 'no', 'us', 'am']
three=['the', 'and','for', 'are', 'but', 'not','you', 'all', 'any', 'can', 'had', 'her', 'was', 'one', 'our', 'out', 'day', 'get', 'has', 'him', 'his', 'how', 'new', 'now', 'old', 'see', 'two', 'way', 'who', 'boy', 'did','let', 'put', 'say', 'she', 'too']


def decrypt():
        key="bxicl yo dthngavukfwerm ps"

        words=[]
        ciphertext=""

        with open('data.txt','r') as fd:
                lines=fd.readlines()
                ciphertext=lines[0]

        for j in range(len(ciphertext)):
                c=ciphertext[j]
                if c in ascii_lowercase:
                        index=ord(c)-97
                        ciphertext=ciphertext[:j]+str(key[index])+ciphertext[j+1:]        
        
        print("="*30,"decrypted paragraph","="*30)
        print()
        print(ciphertext)
        print()
        
        

                        


decrypt()
