import random

# l=["RAEHTF","KABRE","CYROTNU","RENEG","OAERELANP",
#   "EARLX","OKOB","IEMTR","DONONL","YORTS"]

# l1=["father","green","aeroplane","bakre","cartoon",
#    "relex","book","timer","london","story"]

dict={"RAEHTF":"father","KABRE":"bakre","RENEG":"green","OKOB":"book","IEMTR":"timer",
      "EARLX":"relax","OAERELANP":"aeroplane","DONONL":"london","YORTS":"story","CYROTNU":"cartoon"}

i=0
count=0
while(i<=5):
    print("\nArrange the letters to form a valid word:")
    keys=list(dict.keys())
    val_list = list(dict.values())
    word=random.choice(keys)
    print(word)
    ip=input().lower()
    
   
    if ip in val_list and word is keys[val_list.index(ip)]:
        count=count+1
        print("\nCorrect")
        
    else:
        count=count-1
        print("\nWrong")
    
        
    i=i+1
    if i==5:
        print("\nfinal Score = ",count)
        break



