#!/Python27/python
from PIL import Image
import pytesseract
import cgitb
import cgi
import difflib
import csv
import sys
import os
import json
import re
import cv2, numpy
from pytesseract import image_to_string

cgitb.enable(display=0, logdir="/path/to/logdir")

"Content-type: text/html"
print
print "<html><head>"
print ""
print "</head><body>"
temp=sys.argv[1]
filepath=os.path.join("upload/",temp)
filename, file_extension = os.path.splitext(temp)
col = Image.open(filepath)
gray = col.convert('L')
bw = gray.point(lambda x: 0 if x<128 else 255, '1')
bw.save("result_bw.png")
#for driving licence number
image=Image.open("result_bw.png")
w,h=image.size
w2=w/2
w1=int(.1*w)
h1=int(.1*h)
h2=int(.23*h)
image.crop((w1,h1,w2,h2)).save('no_crop.png')


import pytesseract
temp="no_crop.png"
img = Image.open(temp)

img.load()
i = pytesseract.image_to_string(img)
#print i

count=0
k=list(i)
#print k
while(count<len(k)):
    if(k[count]=='M'):
        #print count
        break
    count=count+1

count2=count+16
dl_no=i[count:count2]
#print dl_no
dl_no1=dl_no.split()
#print dl_no1
dl_no2=[dl_no1[0]+dl_no1[1]]
#print dl_no2

# for other details
w11=0
h11=int(.5*h)
w22=int(.6*w)
h22=int(0.9*h)
image.crop((w11,h11,w22,h22)).save('otherdet_crop.png')

#import pytesseract
temp="otherdet_crop.png"
img = Image.open(temp)

img.load()
l = pytesseract.image_to_string(img)
l=filter(lambda x: ord(x)<128,l)
#print l

count=0
p=l.split()
while(count<len(p)):
    if(p[count]=="'"):
        p.remove("'")
        count=count-1
    if(p[count]=='.'):
        p.remove('.')
        count=count-1
    if(p[count]==".'"):
        p.remove(".'")
        count=count-1
    if(p[count]=="'."):
        p.remove("'.")
        count=count-1
    if(p[count]==' '):
        p.remove(' ')
        count=count-1
    
    count=count+1
#print p
wor1=difflib.get_close_matches("DOB", p)

#print wor1
flag=0
count1=0
count2=0
ind=0
while(count1<len(wor1) & flag==0):
    while(count2<len(p) & flag==0):
        if(p[count2]==wor1[count1]):
            ind=count2
            flag=1
        count2=coun2+1

    count1=count1+1
#print ind
#for printing dob
#print p[ind]
#print p[ind+1]
dob=p[ind+1]
dob1=dob.split()

count=0
line=l.split('\n')
while(count<len(line)):
    if(line[count]==''):
        line.remove('')
        count=count-1
    count=count+1

#print line
count=0

name=0
names_xl=[]
while(count<len(line)):
     list=line[count].split()
     #print list
     wor2=difflib.get_close_matches('Name', list)
     #print wor2
     if(len(wor2)>0):
         name=count
         #print name
         #print line[name]
         z=line[name].split()
         f=line[name+1].split()
         z.pop(0)
         f.pop(0)
         #print z
         #print f
         d=' '.join(z)
         e=' '.join(f)
         #for printing name of holder
         #print d
         #for printing name of father
         #print e
        
     count=count+1
     

with open('license.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        names_xl.append(row['NAMES'])

#print names_xl


  
with open('license.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
       names=difflib.get_close_matches(d,names_xl)
    #print names

heading=['Name','FatherName','DOB','licence_number']
temp=names+dob1+dl_no2
final=dict(zip(heading,temp))
#print final

helo=json.dumps(final)
print helo


with open('json_file/'+filename + '.json', 'w') as fp:
	json.dump(helo, fp)

print "</body></html>"

