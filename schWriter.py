# schedulerTools.py
# This script/module contains functions for Generating, Extracting and compressing .ini schedules to or from a "Schedules archive (.sar)"

import zipfile,ConfigParser as c,codecs,os

dummy='c:\\dummy'
sch=c.ConfigParser()
root='c:\\scheduler'
j=os.path.join

getYear=2013
getMonth=1
getSvn=1


def writeSch(input,output):
 sch=c.ConfigParser()
 days=['Sun','Mon','Tue','Wed','Thu','Fri','Sat']
 t=codecs.open(input, 'r', "latin-1")
 l = t.readlines()
 ln=len(l)
 if ln<14:
   raise IndexError("Contains less than 14 lines. A schedule must have at least 14 lines")

 sch=c.ConfigParser()
 data=open(output,'w')
 time=['First','Second']
 add=0
 dayIndex=0
 for lines in range(14):

  if add==2:
    dayIndex+=1
    add=0
  sec=str(days[dayIndex])
  try:
    sch.add_section(sec)
  except:
    pass
  ext = l[lines]
  mp=ext.replace(u'\r\n', u'')
  mp=mp.replace(u'\n', u'')
  mp=mp.replace(u'\t', u'')
  sch.set(sec,str(time[add]),mp)
  add+=1
 sch.write(data)
 data.close()



def compress(sarDir,schFile):
   name=os.path.split(schFile)[1]
   zipath=os.path.join(sarDir,'schedule.sar')
   if not os.path.exists(zipath):
      modo='w'
   else:
      modo='a'
   sar = zipfile.ZipFile(os.path.join(sarDir,'schedule.sar'), modo)
   sar.write(schFile,name)
   sar.close()
   del name
   del sar

