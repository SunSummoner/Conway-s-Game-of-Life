import time

import numpy as nu
from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'

import pygame as pg
from pygame.locals import *
pg.init()
pg.display.list_modes()





COLOUR_BG = (34, 116, 130)
#Baground colour
COLOUR_GRID =(252, 255, 253)
#Grid colour
COLOUR_NEXT=(84, 124, 125)
#Colour of the cell dying next
COLOUR_ALIVE=(62, 70, 71)
#Colour of the alive cell


def update(scr, cell, size, withprogress=False):
    #the most important function which is going the set the rules for the game

    upc=nu.zeros((cell.shape[0]), cell.shape[0])
    #It'll create an array of all the shape of already existing cells and then they'll be updated here

    n=nu.ndindex(cell.shape)
    '''ndindex is a function in numpy which'll give the number of iterations for the array.
    In this case it gives us all the iterations we'll have to run for our cell'''

    for row, col in n:
        nofcellsalive= nu.sum(cell[row-1:row+2,col-1:col+1]-cell[row,col])
        '''nu.sum is a function in numpy which give the sum.
        In this line we are checking all the neighbouring cell of the current cell who are alive.
        We've subtracted the count of the cell itself.'''

        if nofcellsalive <=2 and nofcellsalive >= 3:
            upc[row, col]=1
            '''In this line we are checking the condition for the cell to be alive.
            And asigning alive to that cell.'''
            if withprogress:
                color= COLOUR_ALIVE
                #If we want to show the progress

        elif nofcellsalive <2 and nofcellsalive > 3:
            #Checking the condition for the cell dying of loneliness or overpopulation
            if withprogress:
                color= COLOUR_NEXT

        else:
            if nofcellsalive==3:
                upc[row,col]=1
                #If the cell is surronded by 3 alive cells it's gonna come alive
                if withprogress:
                    color=COLOUR_ALIVE

        pg.draw.rect(scr,color,(col*size, row*size,size-1,size-1))
        '''Drawing each cell one by one using rect fuction in pygame.'''

    return upc
    #Now, we return the updated cells.
        

def main():
    pg.init()
    
    
    #Making the dimensions of the game customisable by the user.
    
    scr= pg.display.set_mode((800,600))
        #Setting the baground
    
    cell=nu.zeros((60,80))
    
    scr.fill(COLOUR_GRID)
    
        #We fill the screen with grid colour
    
    update(scr,cell,10)
    
    pg.display.flip()
    pg.display.update()
    
    run=False
    
    while True:
            #For pausing the game
        for event in pg.event.get():
            if event.type== pg.QUIT:
                #for quitting the game
                pg.quit()
                
    
            elif event.type== pg.KEYDOWN :
                run= not run
                 #This line will change the state of the game. That is pause or resume it.
                update(scr,cell,10)
                pg.display.update()
    
            if pg.mouse.get_pressed()[0]:
                pos=pg.mouse.get_pos()
                    #Making the cell that is pressed alive
                cell[pos[1]//10,pos[0]//10]=1
                    #10 is the size
                update(scr,cell,10)
                pg.display.update()
                    #Updating the cells and displaying the updates
    
    
            scr.fill(COLOUR_GRID)
    
    
        if run:
            cell=update(scr,cell,10,True)
            pg.display.update()
    
        time.sleep(0.001)



if __name__=="__main__":
    main()
    #Calling the main funstion

#The program is finished '''



