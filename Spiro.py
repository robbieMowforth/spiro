#Spiro is a mixture of old code from 1st year and patches from my 3rd year uni

#Things to add:
#-general error handling for inputs
#-Add extra inputs such as:
  #-pen width
  #-pen colour
#-Implement the textfile maker into a main with this
#-Think about setting a new starting point: around centre or centre in shape

import turtle
import random
import copy
import time

#setting up the screen and turtle
screen = turtle.Screen()
Spiro = turtle.Turtle()
Spiro.hideturtle()
turtle.colormode(255)  

#Setting up the screen to be full screen no buttons on launch
screen.screensize()
screen.setup(width = 1.0, height = 1.0) #sets fullscreen
canvas = screen.getcanvas()
root = canvas.winfo_toplevel() #sets it to one whole screen
root.overrideredirect(1)

#constructor of the spiroObj, this basically holds the rules for the different Spiro configs
class SpiroObj:
  def __init__(self, num, repAng,
               centre, zoom, speed, offset,
               rPen, gPen, bPen,
               xPos, yPos):
    self.num = num
    self.repAng = repAng
    self.centre = centre
    self.zoom = zoom
    self.speed = speed
    self.offset = offset
    self.rPen = rPen
    self.gPen = gPen
    self.bPen = bPen
    self.xPos = xPos
    self.yPos = yPos
          
#function which draws out what the user requested
def Spirograph_Function(num,repAng,
                        centre,zoom,speed,offset,
                        rPen,gPen,bPen,
                        xPos,yPos):
    a=0
    b=1
    x=0
    
    #sets the refresh speed of the window to determine the draw speed
    if speed=='I':
        turtle.tracer(0,0)
    elif speed=='N':
        turtle.tracer(1,5)
    else:
        turtle.tracer(1,1)

    #puts in the user angle offest, centre, xPos, yPos
    Spiro.up()
    Spiro.forward(xPos)

    Spiro.left(90)
    Spiro.forward(yPos)
    Spiro.right(90)

    Spiro.left(offset)
    Spiro.forward(centre)
    Spiro.down()

    #set pen colour based on user input, does some error handling for values above
    #255 or below 0
    if rPen>255: rPen=255
    if rPen<0: rPen=0
    
    if gPen>255: gPen=255
    if gPen<0: gPen=0
    
    if bPen>255: bPen=255
    if bPen<0: bPen=0
      
    Spiro.pencolor(rPen,gPen,bPen)

    #sets the angles needed to draw the given shape
    #e.g a equalatrial triangle has 3 internal angles of 60
    #Let num=3, plug into equations below and you'll se 60 come one for Un_angle
    angle=(num-2)*180
    Un_angle=angle/num
    Fi_angle=(180-Un_angle)
    Finish=(360/repAng)

    #For a turning angle that doesn't divide 360 well (answer isn't an integer)
    #e.g repAng=359, 360/359 !% 1 (not integer)
    #b=2 SO now try (360*b) = 720. 720/359 !% 1.
    #keeping trying untill you get an integer answer
    #Fact: by mathmatical principle, Finish will never be higher than 360, think about it
    while Finish%1>0:
        b=b+1
        Finish=(360*b/repAng)

    print("Spiro is drawing",int(Finish),"just for you")

    #drwaing step, 'a' counts the number of iterations
    while a<Finish:
        Spiro.left(90)
        while x<=num:
            if x<1:
                Spiro.forward(25*zoom)
                Spiro.right(Fi_angle)
                x=x+1
            elif x>(num-1):
                Spiro.forward(25*zoom)
                Spiro.left(90)
                Spiro.up()
                Spiro.forward(centre)
                Spiro.left(180)
                Spiro.left(repAng)
                Spiro.forward(centre)
                Spiro.down()
                x=x+1
            else:
                Spiro.forward(50*zoom)
                Spiro.right(Fi_angle)
                x=x+1
        canvas = screen.getcanvas()
        filePath = '/Projects/SpiroProject/temp'
        canvas.postscript(file=filePath)
        x=0
        a=a+1
        
    #I believe this was to deal with some left over pixels from the drawing step
    Spiro.left(180)
    Spiro.up()
    Spiro.forward(centre)
    Spiro.left(180)
    Spiro.right(offset)
    Spiro.down()

    #reset the spiro back to startingPos
    Spiro.up()
    Spiro.forward(-xPos)

    Spiro.left(90)
    Spiro.forward(-yPos)
    Spiro.right(90)

    #needed if you wanted an instant draw, updates all turtle moves to the screen
    if speed=='I':
        turtle.update()
        time.sleep(0.1)

#error handling, had some common cases so made a function for it
def Y_N_Error(userInput):
    while userInput.upper() not in {'Y','N'}:
            userInput=input("Input wrong, please try again(Y/N): ")
    return userInput.upper()
    

#start of program, this first asks to check for a file to read Spiro configurations from
#objHold is if in-case the person wants to store the manual usage of the program to a file
objHold = []

#checks for the mode the user wants, manual or file read
fileCheck=input("Do you wish to read from a text file?(Y/N): ")
while fileCheck.upper() not in {'Y','N'}: #error handling
    fileCheck=input("Input wrong, please try again(Y/N): ")

#start of the file reading mode
if fileCheck.upper()=='Y':
    loop1=True
    while loop1:
        fileName=input("Please enter the name of the text file: ")

        #error handling for fileName
        nameCheck=True
        while nameCheck:
            try:
                f = open('FilesToRun/'+fileName+'.txt', 'r')
                nameCheck=False
            except:
                fileName=input("File not found, check the name and try again: ")
        
        for line in f:
            line=line.strip('\n')
            configs=line.split(',')

            #calls function from the read in lines
            Spirograph_Function(int(configs[0]), #num sides
                                float(configs[1]), #angle to rotate next copy
                                float(configs[2]), #radius of centre point
                                float(configs[3]), #size/magnification
                                configs[4], #speed of drawing
                                float(configs[5]), #starting pos offest angle
                                int(configs[6]), #Red value
                                int(configs[7]), #Green value
                                int(configs[8]), #Blue value
                                float(configs[9]), #xPosition
                                float(configs[10])) #yPosition
            
            #creates an object holding the spiro so it can then be printed to a file later
            oT = SpiroObj(int(configs[0]),
                            float(configs[1]), 
                            float(configs[2]), 
                            float(configs[3]), 
                            configs[4], 
                            float(configs[5]),
                            int(configs[6]),
                            int(configs[7]),
                            int(configs[8]),
                            float(configs[9]),
                            float(configs[10]))

            #appends the object to the list of Spiro's
            objHold.append(oT)
            
        f.close()

        #area to ask for another file read
        Multi=input("Do you wish to read another file?(Y/N): ")
        Multi=Y_N_Error(Multi) #error handling func, see above code       
        if Multi.upper()=='Y':
            print("continued")
        elif Multi.upper()=='N':
            loop1=False

#start of manual mode
if fileCheck.upper()=='N':
    loop2=True
    
    while loop2:
        #block of all manual inputs asked for
        num=int(input("how many sides does your regular polygon have?: "))
        repAng=float(input("enter how far you want it to turn after each complete polygon (degrees): "))
        centre=float(input("set the radius of the centre: "))
        zoom=float(input("What factor of magnification?(0.05 - tiny, 1 - normal, 20 - huge): "))
        speed=input("Normal, Fast or Instant drawing speed?(N/F/I): ")
        offset=float(input("How much do you want the spirograph to be offset by? (if nothing type 0): "))
        rPen=int(input("red colour value(0-255): "))
        gPen=int(input("green colour value(0-255): "))
        bPen=int(input("blue colour value(0-255): "))
        xPos=float(input("x starting cords: "))
        yPos=float(input("y starting cords: "))
        #function call
        Spirograph_Function(num,repAng,
                            centre,zoom,speed,offset,
                            rPen,gPen,bPen,
                            xPos,yPos)

        #stores config as an object for printing back to file
        oT = SpiroObj(int(num),
                        float(repAng), 
                        float(centre), 
                        float(zoom), 
                        speed, 
                        float(offset),
                        int(rPen),
                        int(gPen),
                        int(bPen),
                        float(xPos),
                        float(yPos))
            
        #appends the object to the list of Spiro's
        objHold.append(oT)
        
        Multi=input("Do you wish to draw another spirograph?(Y/N): ")
        Multi=Y_N_Error(Multi) #error handling        
        if Multi.upper()=='Y':
            print("continued")
        elif Multi.upper()=='N':
            loop2=False
            
#checks if the user wants to print the Spiros to a file
printSpiro=input("Do you wish to add your findings to a file?(Y/N): ")
printSpiro=Y_N_Error(printSpiro) #error handling

#beginning of printing to a txt file
if printSpiro.upper()=='Y':

    #custom name making
    fileNamePrint=input("Enter the file name: ")

    #error handling
    nameCheck=True
    while nameCheck:
        try:
            f = open('FilesToRun/'+fileNamePrint+'.txt', 'x')
            nameCheck=False
            f.close()
        except:
            fileNamePrint=input("File already exists, try new name: ")
                        
    #opens the newly made file and writes to it
    f = open('FilesToRun/'+fileNamePrint+'.txt', 'w')
    for i in objHold:
        f.write(str(i.num)+','+
            str(i.repAng)+','+
            str(i.centre)+','+
            str(i.zoom)+','+
            i.speed+','+
            str(i.offset)+','+
            str(i.rPen)+','+
            str(i.gPen)+','+
            str(i.bPen)+','+
            str(i.xPos)+','+
            str(i.yPos)+'\n')

    f.close()
    print('File stored as '+fileNamePrint+', thanks for using Spiro!')

elif printSpiro.upper()=='N':
    print('thanks for using Spiro!')
    #end of program                
                    
                





            
