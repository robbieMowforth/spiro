#file makes text files which can be run on the Spiro porgram
import math

#MAKE THE COLOUR ITER work over 2 rows
#e.g row1: 0
    #row2: 0
    #row3: 1 e.t.c

fileName = input("Please enter desired fileName: ")

#error handling
nameCheck=True
while nameCheck:
    try:
        f = open('FilesToRun/'+fileName+'.txt', 'x')
        nameCheck=False
        f.close()
    except:
        fileName=input("File already exists, try new name: ")

#Big bulk of user input to get started, error handling is needed but fuck that
sides=int(input("how many sides does your regular polygon have?: "))
iterSides=float(input("How many sides to add on per spiro?: "))

repAng=float(input("enter how far you want it to turn after each complete polygon (degrees): "))
iterRepAng=float(input("How many degress to add on per spiro?: "))

centre=float(input("set the radius of the centre: "))
iterCentre=float(input("How much length to add on to radius per spiro?: "))

zoom=float(input("What factor of magnification?(0.05 - tiny, 1 - normal, 20 - huge): "))
iterZoom=float(input("How much magnification to add on per spiro?: "))

speed=input("Normal, Fast or Instant drawing speed?(N/F/I): ")

offset=float(input("How much do you want the spirograph to be offset by? (if nothing type 0): "))
iterOffset=float(input("How much offset to add on per spiro?: "))

rPen=int(input("red colour value(0-255): "))
iterRPen=float(input("red colour iter: "))

gPen=int(input("green colour value(0-255): "))
iterGPen=float(input("green colour iter: "))

bPen=int(input("blue colour value(0-255): "))
iterBPen=float(input("blue colour iter: "))

xPos=float(input("input starting xPos: "))
iterXPos=float(input("iterative xPos each loop: "))

yPos=float(input("input starting yPos: "))
iterYPos=float(input("iterative yPos each loop: "))

loops=int(input("How many loops do you want?: "))

##IDEA
#Make a function that can name the file automatically from the user inputs


#opens the text file for writing
f = open('FilesToRun/'+fileName+'.txt', 'w')

#creation of file, math.floor allows for integer values to be further spread
#across rows e.g every two rows, sides goes up by 1.
looper=0.0
while looper<loops+1:
    #450*(math.sin(looper*(math.pi/180)))
    #(looper*iterYPos)


    
    f.write(str(sides+math.floor(looper*iterSides))+','+
    str(repAng+(looper*iterRepAng))+','+
    str(centre+(looper*iterCentre))+','+
    str(zoom+(looper*iterZoom))+','+
    speed+','+
    str(offset+(looper*iterOffset))+','+
    str(rPen+math.floor(looper*iterRPen))+','+
    str(gPen+math.floor(looper*iterGPen))+','+
    str(bPen+math.floor(looper*iterBPen))+','+
    str(xPos+(looper*iterXPos))+','+
    str(yPos+(looper*iterYPos))+'\n')
    looper+=1

f.close()
    
    
        
