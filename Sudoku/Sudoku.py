from tkinter import *
from random import *
import math

#The 9 grids inside the overall grid, a 3x3, naming series 100
def threeByThree(u,x,y):
    u = str(u);
    print(u)
    u = Frame(gridFrame);
    u.grid(column = x, row = y);
    u.config(height = 210, width = 210, bg = "black", bd = 2, relief = "solid");
    print(u)


#Factors of 9 for maths in the cell function
factors = []
for i in range(1, 82):
    if (i % 9 == 0):
        factors.append(i)

#The "Main Numbers", the top left number in every square of the 3x3.
oneThreeFactors = []
for i in range(1, 62, 3):
    oneThreeFactors.append(i);
del oneThreeFactors[3:9];
del oneThreeFactors[6:12];


#All things cells
def cell(name,counter):
    x = None;
    y = None;
    i = counter

    #Making x and y correct values to put into column and row to make the grid.
    if (all(item in factors for item in str(i)) == False):
        i = i - 1;
        x = (i % 9);
    else:
        x = ((i % 9) - 1);
    y = math.floor((i / 9));


    #Creating frames for individual entries so each entry has a border
    if (all(item in oneThreeFactors for item in str(counter)) == False):#If the current value in counter is one of the Main Numbers.
        c = oneThreeFactors.index(counter);#Makes the value of c the index of counter's position in the list of Main Numbers.
        c += 101;#Add 101 because the 3x3 grid was named 101-109.
        c = str(c);

        counterRelevantNumbers = [counter, counter + 1, counter + 2, counter + 9, counter + 10, counter + 11, counter + 18, counter + 19, counter + 20];
        #List of numbers which are in the same quadrant as the Main Number

    cellFrame = counter + 200;#Naming the frame for the entries, 200 series
    cellFrame = Frame(c);
    cellFrame.grid(column = x, row = y)
    cellFrame.config(height = 70, width = 70, bg = "black", bd = 1, relief = "solid");
    
    #Creating the entries
    name = Entry(cellFrame);
    name.grid(column = 0, row = 0);
    name.place(height = 70, width = 70);
    name.config(bg = "grey", bd = 0);
    


    #Attempt 1:
    #name = 1;
    #check = True;
    #x = -1;
    #y = -1;
    #
    #removeCounter = 0;
    #
    #mainNumber = 1;
    #counter = 1;
    #counterRelevantNumbers = [counter, counter + 1, counter + 2, counter + 9, counter + 10, counter + 11, counter + 18, counter + 19, counter + 20];
    #
    #fullList = []
    #for i in range(82):
    #    fullList.append(i);
    #    i += 1;
    #
    #while (fullList != []):
    #    while (check == True):
    #        if ((len(counterRelevantNumbers % 3) == 0)):
    #            x += 1;
    #        y += 1;
    #        if (x > 2):
    #            x = 0;
    #        if (y > 2):
    #            y = 0;
    #
    #        name = int(name);
    #        name = (name + (len(fullList) - 81));
    #        name = str(name)
    #        name = Entry(counter + 100)
    #        name.grid(column = x, row = y)
    #
    #        check = all(item in fullList for item in counterRelevantNumbers);
    #
    #        fullList.remove(counterRelevantNumbers[removeCounter]);
    #        removeCounter += 1;
    #        if (removeCounter == 8):
    #            removeCounter = 0;
    #
    #        
    #    x = 0;
    #    y = 0;


        #Try counterRelevantNumbers[i]

    #n.grid(column = x, row = y);
    #n.config(height = 70, width = 70, bg = "grey", bd = 1, relief = "solid");




root = Tk();
root.title("Sudoku");
root.geometry("3820x2160");

randomNumber = None;
numberGrid = [];


#Creating overall grid
gridFrame = Frame(root);
gridFrame.config(height = 630, width = 630, bg = "black", bd = 4, relief = "solid");
gridFrame.grid(column = 0, row = 0);


#Creating cell containers
u = 101;
x = 0;
y = 0;

while (x < 3):
    threeByThree(u,x,y);
    x += 1;
    u += 1;
x = 0;
y = 1;
while (x < 3):
    threeByThree(u,x,y);
    x += 1;
    u += 1;
x = 0;
y = 2;
while (x < 3):
    threeByThree(u,x,y);
    x += 1;
    u += 1;


#Creating individual cells
name = 1;
x = 0;
y = 0;
increment = 1;

for i in range(1,82):
    cell(name,increment);
    name += 1;
    increment += 1;
    i += 1;











root.mainloop();
