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
exists = os.path.exists




def chew(buggy, civil):
 global hunters, start, end

 rawDir=os.path.join(civil,'Raw')
 iniDir=os.path.join(civil,'INI')

 if not exists(civil):
    os.makedirs(civil)

 if not exists(rawDir):
    os.makedirs(rawDir)

 if not exists(iniDir):
    os.makedirs(iniDir)


 while hunters != 8:
   rawPath=os.path.join(rawDir, unicode(hunters)+'.txt')
   iniPath=os.path.join(iniDir, unicode(hunters)+'.ini')
   f=open(rawPath,'w')
   for pulsegun in range(start,end):
      f.write(buggy[pulsegun]+unicode('\n'))
   f.close()
   sch.writeSch(rawPath,iniPath)
   start+=13
   end+=14
   hunters+=1



def parse(headcrabs, dropship):
 global gravity, ammunition
 vance=re.sub(r'[Gg]roup [0-9]','', str(headcrabs), re.M|re.I)
 vance=vance.replace(' ','')
 gman=vance.replace('\n','')
 gman=gman.replace('\t','')
 while len(gordon)!=hevSuit:
      freeman = []
      zeroPoint=gravity+gun
      freeman.append(gman[gravity:zeroPoint])
      gravity+=gun
      gordon.append(freeman[0])
      ammunition+=1
      antlions.append(freeman)
      ammunition=0
      print gravity
 chew(gordon, dropship)



