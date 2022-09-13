import random

l=["RAEHTF","KABRE","CYROTNU","RENEG","OAERELANP",
  "EARLX","OKOB","IEMTR","DONONL","YORTS"]

l1=["father","green","aeroplane","bakre","",
   "relex","book","timer","london","story"]
i=0
count=0
while(i<=5):
    print("\nArrange the letters to form a valid word:")
    word=random.choice(l)
    print(word)
    ip=input()

     
    if ip.lower() in l1:
        count=count+1
        print("\nCorrect")
        
    else:
        count=count-1
        print("\nWrong")
        
    i=i+1
    if i==5:
        print("\nfinal Score = ",count)
        break



