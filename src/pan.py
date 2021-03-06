#!/Python27/python
from PIL import Image
import pytesseract
import cgitb
import cgi
import sys
import os
import json
import re
import cv2, numpy
import csv
import difflib
from pytesseract import image_to_string

cgitb.enable(display=0, logdir="/path/to/logdir")

"Content-type: text/html"
print
print "<html><head>"
print ""
print "</head><body>"



def hasNumbers(inputString):
    return any(char.isdigit() for char in inputString)

#converting image to black and white
temp=sys.argv[1]
filepath=os.path.join("upload/",temp)
filename, file_extension = os.path.splitext(temp)
original = Image.open(filepath)
gray = original.convert('L')
bw = gray.point(lambda x: 0 if x<128 else 245, '1')
bw.save("result.png")

#croping image
image=Image.open("result.png")
w,h=image.size
e=w/2
f=int(.15*h)
g=int(.15*h)
image.crop((0,g,e,h-f)).save('result_crop.png')

#reading text from image
temp="result_crop.png"
img = Image.open(temp)
#print "Hello world"
img.load()
i = pytesseract.image_to_string(img)
#print i
j=i.split('\n')
#print j

#removing garbage
k=filter(lambda x: ord(x)<128,i)
#print k
final_list=k.split('\n')
#print final_list

#comparing names with database
names=[]
count=0
names_xl=[]
wanted=[]
numbers1=[]
other=[]
with open('pan.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        if not names:
            names=difflib.get_close_matches(row['Names'],final_list)
    #print names
        #if wor1:
        #    wor2=wor1

with open('pan.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        names_xl.append(row['Names'])
    #print names_xl

for letters in names:
    correct_names=difflib.get_close_matches(letters,names_xl)
#print correct_names.reverse()

numbers=list(set(final_list)-set(names))
#print "numbers"
#print numbers
 

for letters in numbers:
    if(hasNumbers(letters)):
        wanted.append(letters)
#print wanted

for letters in wanted:
    if(len(letters)==10):
        numbers1.append(letters)
#print numbers1

#for letters in numbers1:
 #   if((re.match('[\d/-]+$', letters))):
 #       print letters
#(re.match('[\d/-]+$', '2015-07-01')



#merging all the four fields
dummy=['20/01/1996','ASDFG567YH']
list1=correct_names+numbers1
#print list1
headings=['Name','FatherName','DOB','PanNo']
dicti=dict(zip(headings,list1))
#print dicti

#converting to json
helo=json.dumps(dicti)
print helo


with open('json_file/'+filename + '.json', 'w') as fp:
	json.dump(helo, fp)


print "</body></html>"




