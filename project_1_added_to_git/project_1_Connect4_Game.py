# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 16:08:42 2020

@author: tizit

Project #1: A Simple Game


Details:
 
Have you ever played "Connect 4"? It's a popular kid's game by the Hasbro company. 
In this project, your task is create a Connect 4 game in Python. Before you get started, 
please watch this video on the rules of Connect 4:

https://youtu.be/utXzIFEVPjA

Once you've got the rules down, your assignment should be fairly straightforward. 
You'll want to draw the board, and allow two players to take turns placing their pieces 
on the board (but as you learned above, they can only do so by choosing a column, not a row).
 The first player to get 4 across or diagonal should win!

Normally the pieces would be red and black, but you can use X and O instead.
"""
# import sys
# from termcolor import colored, cprint

def drawField(field):     
    for row in range(11): # 0 - 10
        if row % 2 == 0: 
            newRow = int(row/2) # 0, 1, 2, 3, 4, 5
            for column in range(13): # 0 - 12
                if column % 2 == 0:
                    newColumn = int(column/2) # 0, 1, 4, 3, 4, 5, 6
                    if column != 12:                      
                        print(connect_list[newRow][newColumn], end="")
                    else:
                        print(connect_list[newRow][newColumn])
                else:
                    print("|", end="")
        else:
            print("-------------")        
        

connect_list = [[" "," "," "," "," "," "," "],[" "," "," "," "," "," "," "],[" "," "," "," "," "," "," "],
                [" "," "," "," "," "," "," "],[" "," "," "," "," "," "," "],[" "," "," "," "," "," "," "]]


player = 1
count = 0
print(connect_list)
drawField(connect_list)

while True:   
    print("Player turn:", player)
    columnInput = int(input("Please enter the column number (0-6): "))
 
    for rowin in range(5, -1, -1):   # start, stop, step -> 5 - 0     
        if player == 1:
            if connect_list[rowin][columnInput] == " ":
                connect_list[rowin][columnInput] = "X"
                #connect_list[rowin][columnInput] = u'\u2B24'
                #connect_list[rowin][columnInput] = cprint(u'\u2B24', 'red')
                count += 1
# =============================================================================
#                 u'\u2B24'
#                 cprint(u'\u2B24', 'green', 'on_red')
# =============================================================================
                #player = 2               
                break
        else:
            if connect_list[rowin][columnInput] == " ":
                connect_list[rowin][columnInput] = "O"
                #connect_list[rowin][columnInput] = cprint(u'\u2B24', 'green')
                count += 1
                #player = 1
                break
    
    print("count =",count)
    won = False
    if count >= 7:
            #Horizontal
        for row in range(5,-1,-1):
            for col in range(4):  
                #if col <= 3:
                if connect_list[row][col] == connect_list[row][col+1] == connect_list[row][col+2] == connect_list[row][col+3] !=' ':
                    drawField(connect_list) #draws the field only when there is a winner
                    print("Game Over")
                    print("Player", player, "won!")
                    won = True
                    break
            #vertical
        for col in range(7):
            for row in range(5,2,-1):
                if connect_list[row][col] == connect_list[row-1][col] == connect_list[row-2][col] == connect_list[row-3][col] != ' ':
                    drawField(connect_list) 
                    print("Game Over")
                    print("Player", player, "won!")
                    won = True
                    break
            #diagonal 
        for row in range(3,6):
            if row == 3:
                if connect_list[row][0] == connect_list[row-1][1] == connect_list[row-2][2] == connect_list[row-3][3] != ' ':
                    drawField(connect_list) 
                    print("Game Over")
                    print("Player", player, "won!")
                    won = True
                    break
            elif row == 4:
                for col in range(2):
                    if connect_list[row-col][col] == connect_list[row-(col+1)][col+1] == connect_list[row-(col+2)][col+2] == connect_list[row-(col+3)][col+3] != ' ':
                        drawField(connect_list) 
                        print("Game Over")
                        print("Player", player, "won!")
                        won = True
                        break
            elif row == 5:
                for col in range(3):
                    if connect_list[row-col][col] == connect_list[row-(col+1)][col+1] == connect_list[row-(col+2)][col+2] == connect_list[row-(col+3)][col+3] != ' ':
                        drawField(connect_list) 
                        print("Game Over")
                        print("Player", player, "won!")
                        won = True
                        break
                        #or
                for col in range(3):
                    if connect_list[row-col][col+1] == connect_list[row-(col+1)][col+2] == connect_list[row-(col+2)][col+3] == connect_list[row-(col+3)][col+4] != ' ':
                        drawField(connect_list) 
                        print("Game Over")
                        print("Player", player, "won!")
                        won = True
                        break
                        #or 
                for col in range(2):    
                    if connect_list[row-col][col+2] == connect_list[row-(col+1)][col+3] == connect_list[row-(col+2)][col+4] == connect_list[row-(col+3)][col+5] != ' ':
                        drawField(connect_list) 
                        print("Game Over")
                        print("Player", player, "won!")
                        won = True
                        break
                        #or
                    if connect_list[row-0][3] == connect_list[row-1][4] == connect_list[row-2][5] == connect_list[row-3][6] != ' ':
                        drawField(connect_list) 
                        print("Game Over")
                        print("Player", player, "won!")
                        won = True
                        break                    
    if won == True:
        break 
    else:
        if player == 1:
            player = 2
        else:
            player = 1
            
        print(connect_list)
        drawField(connect_list) # draws the field every time the players make a move.