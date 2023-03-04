### ---- Wordsearch generator ----#
#Randomly picks 7 words from a large txt file containing english words. 
#Program then generates an empty grid, fills the grid with the random words in randomly selected locations, then fills the remaining spaces with random letters
#Then the final wordsearch is outputted :)

import random

def generateWords ():
    allWords = []
    words = []
    count = 0
    file = open("EnglishWords.txt", 'r')

    #Fetching all words into an array
    for line in file:
        line = line.rstrip()
        allWords.append (line)

    while count < 7:
        length = 9                         #Arbitrary length setter to ensure the while loop runs
        while length > 8:                     #Set max word length to 10 since can't be larger than the grid size
            picked = random.choice (allWords)
            length = len(picked)
        words.append (picked)
        count += 1

    file.close()
    
    return words

#Creates a 10x10 empty grid as a 2d array
def generateGrid ():
    grid = []
    for x in range (10):                
        gridLine = []
        for y in range (10):
            gridLine.append (' ')
        grid.append (gridLine)

    return grid

#Placing our words on the grid
def placeOnGrid (words, grid):
    num = 0

    while num < len(words):     #Runs through all words generated
        clash = False
        while clash == False:           #Have this while loop to prevent index errors (i.e. if words overlap or if they don't fit)

            current = words [num]       #Holds the word we are placing 

            #Choosing vertical or horizontal
            placement = random.randint (1,2)

            #Placing word vertically (randomly generated its position)
            if placement == 1:
                x = random.randint (0,9)
                y = random.randint (0,9)

                temp = x

                #Checking if two words overlap or if they do not fit
                i = 0
                while i < len(current) and clash == False:
                    if grid [temp][y] == ' ':
                        temp += 1
                        if temp == 9 and i != len(current) - 1:         #If word isn't finished and doesn't fit in grid then clash = True
                            clash = True
                        elif temp > 9:
                            clash = True
                        i += 1
                    else:
                        clash = True
                
                #Places word into grid now that it is confirmed that the word can be placed there
                if clash == False:
                    for i in range (len(current)):
                        grid [x][y] = current[i]
                        x += 1
                    num += 1

            #Placing word horizontally (same process as vertically but increment y value instead)
            if placement == 2:
                x = random.randint (0,9)
                y = random.randint (0,9)
            
                temp = y 

                #Checking for any overlaps
                j = 0
                while j < len(current) and clash == False:
                    if grid [x][temp] == ' ':
                        temp += 1
                        if temp == 9 and j != len(current) - 1:
                            clash = True
                        elif temp > 9:
                            clash = True
                        j+= 1
                    else:
                        clash = True
                
                if clash == False:
                    for j in range (len(current)):
                        grid [x][y] = current[j]
                        y += 1
                    num += 1

            
            break #Breaks while loop to move onto next word once the whole word has been displayed


    return grid

#Fills the remaining spaces in the grid with random letters
def fill (grid):
    letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    for x in range (10):
        for y in range (10):
            if grid [x][y] == ' ':                      #If the index in the 2d array = empty, fill it with a random letter, otherwise skip
                grid[x][y] = random.choice (letters)

    return grid




def main ():
    words = generateWords ()

    grid = generateGrid ()

    grid = placeOnGrid (words, grid)

    grid = fill (grid)

    for x in range (10):
        print (grid[x])

    print ("Word choices: ", words)


main ()