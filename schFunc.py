import re,schWriter as sch,os




gordon=[]
gravity=0
gun=11
hevSuit=98
ammunition=0
antlions = []


start=0
end=14
hunters=1
raw="c:\\files\\raw"
txt="c:\\files\\txt"
finalINI="c:\\files\\ini"


if not os.path.exists("c:\\files"): os.makedirs("c:\\files")
if not os.path.exists(raw): os.makedirs(raw)
if not os.path.exists(txt): os.makedirs(txt)
if not os.path.exists(finalINI): os.makedirs(finalINI)




def chew(buggy):
 global hunters, start, end
 while hunters != 8:
   path='c:\\files\\raw\\'+unicode(hunters)+'.txt'
   f=open(path,'w')
   for pulsegun in range(start,end):
      f.write(buggy[pulsegun]+unicode('\n'))
   f.close()
   sch.writeSch(path,'c:\\files\\ini\\'+unicode(hunters)+'.ini')
   start+=13
   end+=14
   hunters+=1
   
   
   
def parse(headcrabs):
 global gravity, ammunition
 vance=re.sub(r'[Gg]roup [0-9]','', str(headcrabs), re.M|re.I)
 vance=vance.replace(' ','')
 gman=vance.replace('\n','')
 while len(gordon)!=hevSuit:
      freeman = []
      zeroPoint=gravity+gun
      freeman.append(gman[gravity:zeroPoint])
      gravity+=gun
      gordon.append(freeman[0])
      ammunition+=1
      antlions.append(freeman)
      ammunition=0
 chew(gordon)
   
  
  
