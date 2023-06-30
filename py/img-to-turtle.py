import turtle
import os
from PIL import Image

fileExtension = ""

def clear():
    if os.name == "nt":
        _ = os.system('cls')
    else:
        _ = os.system('clear')
    
def replaceStringIndex(text,index=0,replacement=""):
    return f"{text[:index]}{replacement}{text[index+1:]}"

def getFileExtension(path):
    global fileExtension # yes bad practice, sue me

    for char in range(len(path)):
        if path[char] == ".":
            for exChar in range(abs(char - len(path))):
                fileExtension += path[char + exChar]

def turtlePixel(x,y,color):
    r,g,b = color[0],color[1],color[2]

    parryPicture = turtle.Turtle(visible=False)
    parryPicture.pencolor((r,g,b))
    parryPicture.fillcolor((r,g,b))
    parryPicture.penup()
    parryPicture.goto(x,y)
    parryPicture.pendown()
    parryPicture.begin_fill()
    for sides in range(4):
        parryPicture.forward(1)
        parryPicture.right(-90)
    parryPicture.end_fill()

    print(f"pixel ({x + 1},{y + 1}) with rgb ({r},{g},{b})")

def main():
    print("img-to-turtle Image Recreator")
    print("Type help for some information.")
    print("Please enter the path to the photo you want to recreate.")
    filePath = input()

    if filePath == "help":
        clear()
        print("The higher resolution of the photo, the longer each pixel will take. I would recommend changing the image resolution to a fraction of its original value.")
        print("Images will appear smooshed, this is because of the unreliablility of the required turtle.setworldcoordinates() method.")
        print("You cannot open the turtle graphics window until the picture is complete, the console will inform you when it is.")
        print("The image can be a PNG, but the turtle does not support transparency. If the picture has transparency, transparent pixels will turn black.")
        print("~~~~~~~~~~~~~~~~~")
        main()

    for letter in range(len(filePath) - 1): # i don't really know if this is required since it seems to work fine without it, but i'm keeping it because why not.
        if filePath[letter] == "\\":
            filePath = replaceStringIndex(filePath,letter,"/")

    try:
        im = Image.open(filePath,"r")
    except:
        clear()
        print("Invalid directory.")
        main()
            
    imX = im.width
    imY = im.height

    clear()
    print("Is this information correct? (y/n)")
    getFileExtension(filePath)
    print("File extension: " + fileExtension)
    print("Dimensions: " + str(im.size))
    isCorrect = input()
    if isCorrect.lower() == "y" or isCorrect.lower() == "yes":
        clear()
    elif isCorrect.lower() == "n" or isCorrect.lower() == "no":
        clear()
        main()
    else:
        clear()
        print("Invalid parameter.")
        main()

    turtle.title("img-to-turtle")
    turtle.setworldcoordinates(0,imX,imY,0)
    turtle.colormode(255) # allow RGB color values
    turtle.speed(0)
    turtle.tracer(0,0) # turn off updating the window so it doesn't move painfully slow

    for yPixel in range(imY):
        for xPixel in range(imX):
            pixelColor = im.getpixel((xPixel,yPixel))
            turtlePixel(xPixel,yPixel,pixelColor)
    print("Processing...")
    turtle.update()
    print("Completed!")
    print("Press enter to exit.")
    exitInput = input()

main()