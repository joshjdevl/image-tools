import os, sys
import Image
import operator


image1="f_frame1.png"
image2="tframe_2.png"

im1 = Image.open(image1)
im2 = Image.open(image2)

width, height = im1.size
print width,height

im1 = im1.load()
im2 = im2.load()

countequal = 0

def convert_grayscale(r,g,b):
    grayscale = 0.2989 * r + 0.5870 * g + 0.1140 * b
    return grayscale


count5 = 0
count10 = 0
count25 = 0
count50 = 0

def count_gray_diff(grayscalediff):
    global count5, count10, count25, count50
    if grayscalediff >= 5:
        count5 = count5 + 1
    if grayscalediff >= 10:
        count10 = count10 + 1
    if grayscalediff >= 25:
        count25 = count25 + 1
    if grayscalediff >= 50:
        count50 = count50 + 1
        

i = 0
j = 0
while i<height:
    while j<width:
        isequal = ( im1[j,i] == im2[j,i] )
        if not isequal:
            countequal = countequal + 1
        tuple1 = im1[j,i]
        tuple2 = im2[j,i]
        r1,g1,b1 = tuple1
        r2,g2,b2 = tuple2
        grayscale1 = convert_grayscale(r1,g1,b1)
        grayscale2 = convert_grayscale(r2,g2,b2)
        grayscalediff = grayscale1 - grayscale2
        count_gray_diff(grayscalediff)
        print isequal,grayscalediff
        j = j+1
    i = i + 1

print "Number Different Pixels=",countequal
print "Number Grayscale Differences Larger than 5 =",count5
print "Number Grayscale Differences Larger than 10 =",count10
print "Number Grayscale Differences Larger than 25 =",count25
print "Number Grayscale Differences Larger than 50 =",count50

#diffvalue = tuple(map(operator.sub, tuple1, tuple2))
#sumvalue = zip(diffvalue) #map(sum,zip(diffvalue))
#sumvalue = [sum(x) for x in diffvalue]


#gray = 0.2989 * r + 0.5870 * g + 0.1140 * b
#brightness = int(round(0.299r + 0.587g + 0.114b)) 
