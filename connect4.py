"""
Daisuke & Kunyu Li (Leo)
CS111, W20
By Leyla Oesper
Final Project
Deadline: March, 16th, 2020

This program runs the game "Connect 4."
"""

import numpy 
#We did not discuss this in class. We use this module to create 
#a two dimentional array. Here is what we used as a refence.
#https://docs.python.org/3/library/multiprocessing.shared_memory.html?highlight=numpy
import graphics
import time 
#We did not discuss this in class. We use this module to stop the function 
#from being executed. Here is a link of the reference.
#https://docs.python.org/3/library/time.html?highlight=time#module-time
import random
import math

class Menu:
    """
    Menu class creates an object for the introduction screen of Connect 4
    """
    
    def __init__(self):
        """
        The constructor creates an instance variable for a window: self.win
        """
        
        self.win = graphics.GraphWin("Connect4 Menu", 680, 500)
        self.win.setCoords(0, 0, 680, 500)
        self.win.setBackground("light green")
    
    
    def introScreen(self):
        """
        This method creates graphics for the function intro()
        """
        
        self.title = graphics.Text(graphics.Point(340, 380), "Connect 4")
        self.title.setSize(36)
        self.title.setStyle("bold")
        self.title.draw(self.win)
        
        self.playButton = graphics.Rectangle(graphics.Point(260, 260),\
                                          graphics.Point(420, 300))
        self.playButton.setFill("pink")
        self.playButton.draw(self.win)
        self.playText = graphics.Text(graphics.Point(340, 280), "Play!")
        self.playText.setSize(20)
        self.playText.setStyle("bold")
        self.playText.draw(self.win)

        self.instructionButton = graphics.Rectangle(graphics.Point(260, 230),\
                                          graphics.Point(420, 190))
        self.instructionButton.setFill("pink")
        self.instructionButton.draw(self.win)
        self.instructionText = graphics.Text(graphics.Point(340, 210), "Instructions")
        self.instructionText.setSize(20)
        self.instructionText.setStyle("bold")
        self.instructionText.draw(self.win)

        
    def intro(self):
        """
        This method uses introScreen() to display the graphics for the introduction page.
        Then, it gets a mouse click from player and leads to the next page depends on where 
        the player clicks. If the player clicks "instructions" it leads the player to 
        the instruction pages by using instructions(), and if the player clicks "instructions" 
        it leads the player to the chooseDifficulty page by using chooseDifficulty().
        
        Returns:
        It returns self.chooseDifficulty(), which simotaniously returns a dictionary object 
        that contains information about the difficulty and disc colors.
        """
        
        self.introScreen()
        
        while True:
            click = self.win.getMouse()
            xCor = click.getX()
            yCor = click.getY()
            
            if (260 <= xCor <= 420) and (190 <= yCor <= 230):
                for item in self.win.items[:]:
                    item.undraw()
                    self.win.update()
                self.instructions()
                self.introScreen()
                
            elif (260 <= xCor <= 420) and (260 <= yCor <= 300):
                for item in self.win.items[:]:
                    item.undraw()
                    self.win.update()
                return self.chooseDifficulty()
            
    def instructionPage1(self):
        """
        This methods create the first page of the instruction pages. It reads player's 
        mouse click and ends itself. 
        """
        
        self.page1 = graphics.Rectangle(graphics.Point(160, 230),\
                                          graphics.Point(500, 375))
        self.page1.setFill("brown")
        self.page1.draw(self.win)
        
        self.rec1 = graphics.Rectangle(graphics.Point(315, 230),\
                                          graphics.Point(345, 0))
        self.rec1.setFill("brown")
        self.rec1.draw(self.win)
        
        word = "Welcome to Connect 4!"
        
        page1Text = graphics.Text(graphics.Point(330, 305), word)
        page1Text.setSize(28)
        page1Text.setTextColor("white")
        page1Text.setStyle("bold")
        page1Text.draw(self.win)
        
        nextButton = graphics.Rectangle(graphics.Point(580,20),\
                                         graphics.Point(630,50))
        nextButton.setFill("Black")
        nextButton.draw(self.win)
        nextText = graphics.Text(graphics.Point(605,35), "Next")
        nextText.setStyle("bold")
        nextText.setTextColor("white")
        nextText.setSize(15)
        nextText.draw(self.win)
        
        while True:
            click = self.win.getMouse()
            xCor = click.getX()
            yCor = click.getY()
            if (580 <= xCor <630) and (20 <= yCor <= 50):
                for item in self.win.items[:]:
                    item.undraw()
                    self.win.update()
                break
       
    
    def instructionPage2(self):
        """
        This methods create the second page of the instruction pages. It reads player's 
        mouse click and ends itself. 
        """
        
        self.page2 = graphics.Rectangle(graphics.Point(90, 240),\
                                          graphics.Point(590, 370))
        self.page2.setFill("brown")
        self.page2.draw(self.win)
        
        self.rec2 = graphics.Rectangle(graphics.Point(330, 240),\
                                          graphics.Point(350, 0))
        self.rec2.setFill("brown")
        self.rec2.draw(self.win)
        
        word = "     You play against Computer. Drop a\n\
            disc and make four discs lined up either\n\
        vertically, horizontally, or diagonally."
        
        
        page2Text = graphics.Text(graphics.Point(300, 305), word)
        page2Text.setSize(25)
        page2Text.setStyle("bold")
        page2Text.setTextColor("white")
        page2Text.draw(self.win)
        
        nextButton = graphics.Rectangle(graphics.Point(580,20),\
                                         graphics.Point(630,50))
        nextButton.setFill("Black")
        nextButton.draw(self.win)
        nextText = graphics.Text(graphics.Point(605,35), "Next")
        nextText.setStyle("bold")
        nextText.setTextColor("white")
        nextText.setSize(15)
        nextText.draw(self.win)
        
        while True:
            click = self.win.getMouse()
            xCor = click.getX()
            yCor = click.getY()
            if (580 <= xCor <630) and (20 <= yCor <= 50):
                for item in self.win.items[:]:
                    item.undraw()
                    self.win.update()
                break
       
        
    def instructionPage3(self):
        """
        This methods create the last page of the instruction pages. It reads player's 
        mouse click and ends itself. 
        """
        
        self.page3 = graphics.Rectangle(graphics.Point(230, 280),\
                                          graphics.Point(450, 380))
        self.page3.setFill("brown")
        self.page3.draw(self.win)
        
        self.rec3 = graphics.Rectangle(graphics.Point(330, 280),\
                                          graphics.Point(350, 0))
        self.rec3.setFill("brown")
        self.rec3.draw(self.win)
        
        word = "Let's play!!"
        
        page3Text = graphics.Text(graphics.Point(340, 330), word)
        page3Text.setSize(36)
        page3Text.setStyle("bold")
        page3Text.setTextColor("white")
        page3Text.draw(self.win)
        
        nextButton = graphics.Rectangle(graphics.Point(580,20),\
                                         graphics.Point(630,50))
        nextButton.setFill("Black")
        nextButton.draw(self.win)
        backText = graphics.Text(graphics.Point(605,35), "Back")
        backText.setStyle("bold")
        backText.setTextColor("white")
        backText.setSize(15)
        backText.draw(self.win)
        
        while True:
            click = self.win.getMouse()
            xCor = click.getX()
            yCor = click.getY()
            if (580 <= xCor <630) and (20 <= yCor <= 50):
                for item in self.win.items[:]:
                    item.undraw()
                    self.win.update()
                break
             
            
    def instructions(self):
        """
        This method creates the instruction pages by calling three functions: instructionPage1()
        instructionPage2(), and instructionPage3(). It returns nothing.
        """
        
        Title = graphics.Text(graphics.Point(340, 450), "Instructions")
        Title.setSize(30)
        Title.setStyle("bold")
        Title.draw(self.win)
        
        self.instructionPage1()
        self.instructionPage2()
        self.instructionPage3()
       

    def chooseDifficulty(self):
        """
        This method is called in intro(). This function creates graphics for the page and 
        allows player to choose their difficulty by clicking two buttons: 
        "Easy" or "Hard". Based on which button they click, the method stores 
        a different value to the dictionary. The method gets access to the dictionary when 
        it calls chooseDifficulty() function. 
        
        Returns:
        aDict - a dictionary object that stores disc colors and the difficulty
        """
    
        difficultyText = graphics.Text(graphics.Point(340, 330), \
                                        "Choose a difficulty")
        difficultyText.setTextColor("black")
        difficultyText.setSize(30)
        difficultyText.setStyle("bold")
        difficultyText.draw(self.win)
        
        easyButton = graphics.Rectangle(graphics.Point(240, 230), \
                                     graphics.Point(310, 280))
        easyButton.setFill("pink")
        easyButton.draw(self.win)
        easyText = graphics.Text(graphics.Point(275, 255), "Easy")
        easyText.setTextColor("black")
        easyText.setStyle("bold")
        easyText.setSize(20)
        easyText.draw(self.win)
        
        hardButton = graphics.Rectangle(graphics.Point(440, 230), \
                                     graphics.Point(370, 280))
        hardButton.setFill("red")
        hardButton.draw(self.win)
        hardText = graphics.Text(graphics.Point(405, 255), "Hard")
        hardText.setTextColor("black")
        hardText.setStyle("bold")
        hardText.setSize(20)
        hardText.draw(self.win)
        
        difficulty = 0
        
        while True:
            click = self.win.getMouse()
            xCor = click.getX()
            yCor = click.getY()
            if (240 <= xCor <310) and (230 <= yCor <= 280):
                for item in self.win.items[:]:
                    item.undraw()
                    self.win.update()
                difficulty = 0
                aDict = self.chooseColor()
                aDict["Difficulty"] = difficulty
                return aDict 
            
            elif (370 <= xCor <440) and (230 <= yCor <= 280):
                for item in self.win.items[:]:
                    item.undraw()
                    self.win.update()
                difficulty = 1
                aDict = self.chooseColor()
                aDict["Difficulty"] = difficulty
                return aDict 
                
        
    def chooseColor(self):
        """
        This method first creates graphics for the choose color page. It then 
        gets a user click and creates a dictionary obejct that contains what
        color the player is going to use in Connect 4 and what color the compueter 
        is going to be. "Light blue" is 2.0 and "pink" is 1.0.
        
        Returns:
        aDict - a dictionary object that contains player's color(as an integer)
        and computer's color (as an integer)
        """
        
        colorText = graphics.Text(graphics.Point(340, 330), \
                                        "Choose your disc")
        colorText.setTextColor("black")
        colorText.setSize(30)
        colorText.setStyle("bold")
        colorText.draw(self.win)
        
        circle1Center = graphics.Point(275, 255)
        radius1 = 30
        circle1 = graphics.Circle(circle1Center, radius1)
        circle1.setFill("pink")
        circle1.draw(self.win)
        
        circle2Center = graphics.Point(405, 255)
        radius2 = 30
        circle2 = graphics.Circle(circle2Center, radius2)
        circle2.setFill("light blue")
        circle2.draw(self.win)
        
        aDict = {}
        
        while True:
            click = self.win.getMouse()
            xCor = click.getX()
            yCor = click.getY()
            c1LengthX = xCor - circle1Center.getX()
            c1LengthY = yCor - circle1Center.getY()
            c1Distance = math.sqrt(c1LengthX ** 2 + c1LengthY ** 2)
            c2LengthX = xCor - circle2Center.getX()
            c2LengthY = yCor - circle2Center.getY()
            c2Distance = math.sqrt(c2LengthX ** 2 + c2LengthY ** 2)
            
            if c1Distance <= radius1:
                for item in self.win.items[:]:
                    item.undraw()
                    self.win.update()
                aDict["Player"] = 1.0
                aDict["Computer"] = 2.0
                
            elif c2Distance <= radius2:
                for item in self.win.items[:]:
                    item.undraw()
                    self.win.update()
                aDict["Player"] = 2.0
                aDict["Computer"] = 1.0
            
            return aDict
                  
    
class Board:
    """
    Board class creates the game board graphics for Connect 4.
    """
    
    def __init__(self):
        """
        The constructor creates an instances vaiable, self.win. It will also creates
        some figures that are displayed on the game board: some buttons and the 6 by 7 
        grip where discs will be dropped. 
        """ 
        
        self.win = graphics.GraphWin("Connect4 Board", 680, 500)
        self.win.setCoords(0, 0, 680, 500)
        self.win.setBackground("light green")
        
        backrectangle = graphics.Rectangle(graphics.Point(662, 400),\
                                       graphics.Point(18, 5))
        backrectangle.setFill("dark green")
        backrectangle.draw(self.win)
        
        turnText = graphics.Text(graphics.Point(70, 450), "Turn: ")
        turnText.setSize(32)
        turnText.setStyle("italic")
        turnText.draw(self.win)
        
        insturuction = graphics.Rectangle(graphics.Point(540, 405), \
                                        graphics.Point(662, 445))
        insturuction.setFill("red")
        insturuction.draw(self.win)
        instuructionText = graphics.Text(graphics.Point(600, 425), "Insuruction")
        instuructionText.setSize(18)
        instuructionText.setStyle("bold")
        instuructionText.draw(self.win)
        
        quit = graphics.Rectangle(graphics.Point(540, 453), \
                                        graphics.Point(662, 493))
        quit.setFill("red")
        quit.draw(self.win)
        quitText = graphics.Text(graphics.Point(595, 473), "Quit")
        quitText.setSize(18)
        quitText.setStyle("bold")
        quitText.draw(self.win)
        
        #The holes on the board
        for row in range(6):
            for col in range(7):
                circleCenter = graphics.Point(64 + col * 92, 50 + row * 60)
                circle = graphics.Circle(circleCenter, 27)
                circle.setFill("light green")
                circle.draw(self.win)
    
    
    def getClick(self):
        """
        This method first gets a mouse click from player. Based on where 
        the player clicks, it determines which column the player wants to drop his disc 
        or if he wants to "quit" or look at "instructions".
        
        Returns:
        columnNumber - an integer indicating which column the player wants to drop his disc
        "q" - a string indicating that the player wants to go back to the intro page
        "i" - a string indicating that the player wants to go back to the instruction pages
        """
        
        while True:
            click = self.win.getMouse()
            xCor = click.getX()
            yCor = click.getY()
            columnNumber = 0
            
            if 5 <= yCor <= 400:
                if 18 < xCor < 110:
                    columnNumber = 0 
                elif 110 < xCor < 570:
                    columnNumber = ((xCor - 18) // 92) 
                elif 570 < xCor < 662:
                    columnNumber = 6
                return columnNumber
            
            elif (540 < xCor < 662) and (453 < yCor < 493):
                return "q"
            
            elif (540 < xCor < 662) and (405 < yCor < 445):
                return "i"
               
    def close(self):
        """
        This method closes the window when the user clicks it
        This is not actually used for the game but useful when we test things out.
        """
        
        self.win.getMouse()
        self.win.close()
    
    def getPoint(self):
        """
        This method prints the coordinate point that player clicks.
        This is not actually used for the game but useful when we test things out.
        """
        
        click = self.win.getMouse()
        print(click.getX(), click.getY())
        
        
    def winScreen(self):
        """
        This method displays the graphics for when the player wins the game. 
        """
        
        oval = graphics.Oval(graphics.Point(240, 215), graphics.Point(440, 285))
        oval.setFill("white")
        oval.draw(self.win)
        
        winMessage = graphics.Text(graphics.Point(340, 250),\
                                        "You Win!!!")
        winMessage.setSize(36)
        winMessage.setStyle("bold")
        winMessage.setTextColor("red")
        winMessage.draw(self.win)
        
            
    def loseScreen(self):
        """
        This method displays the graphics for when the player loses the game. 
        """
        
        oval = graphics.Oval(graphics.Point(235, 215), graphics.Point(445, 285))
        oval.setFill("white")
        oval.draw(self.win)
          
        loseMessage = graphics.Text(graphics.Point(340, 250),\
                                        "You Lose!!")
        loseMessage.setSize(36)
        loseMessage.setStyle("bold")
        loseMessage.setTextColor("red")
        loseMessage.draw(self.win)
        
        
    def tieGameScreen(self):
        """
        This method displays the graphics for when it's a tie game. 
        """
        
        oval = graphics.Oval(graphics.Point(240, 215), graphics.Point(440, 285))
        oval.setFill("white")
        oval.draw(self.win)
        
        filled = graphics.Text(graphics.Point(340, 250),\
                                        "Tie game!!!")
        filled.setSize(34)
        filled.setStyle("bold")
        filled.setTextColor("red")
        filled.draw(self.win)
        
        
class Disc:
    """
    Disc class creates a disc object used in the game
    """
    
    def __init__(self, screen, xCor, yCor, color):
        """
        The constructor creates several instances variables.
        It takes four parameters, and creates a disc based on those parameters.
        
        Parameters:
        screen - a window object where the graphics will take place
        xCor - an integer indicating x-value where the circle's center will locate
        yCor - an integer indicating y-value where the circle will be dropped
        color - a string indicating the disc's color
        """
        
        self.win = screen
        self.xCor = xCor
        self.yCor = yCor
        self.color = color
        self.circle = graphics.Circle(graphics.Point(self.xCor, 430), 27)
        self.circle.draw(self.win)
        self.circle.setFill(self.color)
        self.inMotion = True
        
        
    def dropAnimation(self):
        """
        This method creates an animation that a disc is dropping
        """
        
        currentYCor = 440
        
        while self.inMotion:
            time.sleep(0.05)
            
            if currentYCor - 40  > int(self.yCor):
                self.inMotion = True
            else:
                self.inMotion = False
            
            self.circle.move(0, -20)
            currentYCor -= 20 
               
                
class Game:
    """
    Game class sets up how the game works
    """
    
    def __init__(self, difficulty):
        """
        The constructor takes in one parameter "difficulty" that determines what algorithm 
        the computer player will use. It assigns the parameter to an instance variable 
        self.difficulty. The instance variable "self.board" creates the board screen of the 
        game by using Board class object. The two instnace variables "self.xCor" and "self.yCor"
        are initialized as Nonetype objects but will be updated while the game is pregressing. 
        They indicate what coordinate point in the screen the disc should be located. 
        The last instance variable "self.boardStatus" uses numpy module to create a list of 
        6 lists with 7 entries, that will be used as the coordinate system corresponding to
        the holes of the game board. Each entry is initially filled with 0, and that means 
        the board is empty. 
        
        Parameters:
        difficulty - an integer indicating the difficulty of the game
        """
        
        self.board = Board()
        self.xCor = None
        self.yCor = None
        self.difficulty = difficulty
        self.boardStatus = numpy.zeros((6, 7)) 
    
    def close(self): 
        """
        This method gets user's mouse click and then close the window. 
        """
        
        self.board.win.getMouse()
        self.board.win.close()

        
    def chooseEndOrNew(self):
        """
        This method creates graphics for the ending screen. It reads the player's mouse
        click and determines whether he wants to play a new game or quit the game. It returns 
        "n" if the player wants to play another game. To quit the game, the player just needs to click the window. 
        
        Returns:
        "n" - a string indicating that the player wants to play a new game
        """
        
        newButton = graphics.Rectangle(graphics.Point(305, 430),\
                                       graphics.Point(375, 470))
        newButton.setFill("white")
        newButton.draw(self.board.win)
        
        self.new = graphics.Text(graphics.Point(340, 450), "New")
        self.new.setSize(22)
        self.new.setStyle("bold")
        self.new.draw(self.board.win)
        
        click = self.board.win.getMouse()
        xCor = click.getX()
        yCor = click.getY()
        
        if (305 <= xCor <= 375) and (430 <= yCor <= 470):
            return "n"   
        
        
    def heightDiscStop(self, col):
        """
        This method takes one parameter col and returns the y value indicating how 
        far the disc can go down through the board by reading the self. board_status. 
        If the first entry of inputted column is empty, the loop checks the next entry 
        in the same column. It repeat this until it checks the bottom entry of that column. 
        If all entries in the column is full, it returns "Full" and it returns the y value
        otherwise. 
        
        Parameters:
        col - an integer indicating the column to be checked
        
        Returns:
        "Full" - a string to be called when all the entries in the "col" is full
        height - an integer indicating the y value that the disc should be placed
        """
        
        col = int(col)
        count = 5
        
        for row in range(6):
            status = self.boardStatus[row][col]
            if status == 0.0:
                count -= 1
            else:
                break
                
        if count >= 5:
            return "Full"
        
        height = 50 + 60 * (count + 1)
        return height
    
    
    def playerMove(self): #Fix later
        """
        This method calls getClick() function from Board class, which returns the
        col indicating the column the player drops his disc. If col is "q", it also 
        returns "q". If col is "i", it also return "i". Otherwise, it uses a while loop 
        to updates (self.xCorm self.yCor) that the player wants to drop his disc. It calls 
        heightDiscStop(col) function. 
        
        Returns:
        "q" - a string indicating that the player wants to go back to the menu screen
        "i" - a string indicating that the player wants to see the instructions
        """
        
        col = self.board.getClick()
        
        if col == "q":
            return "q"
        
        elif col == "i":
            return "i"
        
        else:
            while self.heightDiscStop(col) == "Full":
                self.xCor = 64 + col * 92
                col = self.board.getClick()
                self.yCor = self.heightDiscStop(col)
            else:
                self.xCor = 64 + col * 92
                self.yCor = self.heightDiscStop(col)

                
    def checkIfConnected(self, numDisc, color):
        """
        This method takes two parameters: numDisc and color. It 
        checks if "numDisc" number of "color" discs are in a line.
        
        Parameters:
        numDisc - an integer indicating the number of discs lining up
        color - an integer indicating the disc's color
        
        Returns: 
        True - a boolean type object to be returned when "numDisc" 
        number of discs with "color" are in a line
        False - a boolean type object to be returned when "numDisc" 
        number of discs with "color" are not in a line
        """
        
        #Horizontal
        for row in range(6):
            for col in range(8 - numDisc):          
                count = 0
                while self.boardStatus[row][col] == color:
                    col +=1
                    count += 1
                    if count == numDisc:
                        return True
                    
        #Vertical
        for col in range(7):          
            for row in range(7 - numDisc):
                count = 0
                while self.boardStatus[row][col] == color:
                    row += 1
                    count += 1
                    if count == numDisc:
                        return True 
                    
        #Diagonal: m = 1
        for col in range(numDisc - 1, 7):
            for row in range(7 - numDisc):
                if self.boardStatus[row][col] == color:
                    for count in range(1, numDisc):
                        if self.boardStatus[row + count][col - count] != color:
                            break
                        if count + 1 == numDisc:
                            return True
                    
        #This code below also works but we prefer the above
        """
        for col in range(numDisc - 1, 7):
            for row in range(7 - numDisc):
                count = 0
                while self.boardStatus[row][col] == color:
                    count += 1
                    if count == numDisc:
                        return True
                    col -=1
                    row +=1
                    if col < 0:
                        break
        """
                
        #Diagonal: m = -1         
        for col in range(8 - numDisc):          
            for row in range(7 - numDisc):
                if self.boardStatus[row][col] == color:
                    for count in range(1, numDisc):
                        if self.boardStatus[row + count][col + count] != color:
                            break
                        if count + 1 == numDisc:
                            return True
                
        #We decided to use the above one
        """
        for col in range(numDisc - 1, 7):
            for row in range(7 - numDisc):
                count = 0
                while self.boardStatus[row][col] == color:
                    count += 1
                    if count == numDisc:
                        return True
                    col +=1
                    row +=1
                    if col > 6:
                        break
        """
                 
        
        return False
    
    
    def computerEasyMove(self):
        """
        This method randomly chooses the position that the computer wants to
        drop its disc and upadtes self.xCor and self.yCor. It uses 
        heightDiscStop(col) functuon. 
        """
        
        col = random.randint(0,6)
        
        while self.heightDiscStop(col) == "Full":
            self.xCor = 64 + col * 92
            col = random.randint(0,6)
            self.yCor = self.heightDiscStop(col)
        else:
            self.xCor = 64 + col * 92
            self.yCor = self.heightDiscStop(col)
    
    
    def checkReach(self, color):
        """
        This method takes in one parameter color. This methods 
        checks whether either color of  4 discs can be in a line 
        by adding one more disc. It tries to drop a disc into every possible position and 
        see if the disc can make a line or not. This methos uses heightDiscStop(col)
        and checkIfConnected(numDisc, color).
        
        Parameters:
        color - an integer indicating the disc's color
        
        Returns:
        xCor - an integer indicating x position that makes four discs in a line
        by adding a disc 
        None - Nonetype object to be returned when there is no such xCor existing
        """
        
        for col in range(7):
            if self.heightDiscStop(col) != "Full":
                row = 5 - ((self.heightDiscStop(col) - 50) // 60)
                self.boardStatus[row][col] = color
                if self.checkIfConnected(4, color) == True:
                    xCor = 64 + col * 92
                    self.boardStatus[row][col] = 0.0
                    return xCor
                else:
                    self.boardStatus[row][col] = 0.0         
        return None
    
    
    def computerHardMove(self, computerColor, playerColor):
        """
        This method sets up how computer will play if the difficulty of the game
        is "Hard." It takes in two parameters: computerColor and playerColor. 
        It first checks whether the computer can win by adding one more disc, and returns the 
        x value if so. If not, then it checks whether the player can win within one more move, and 
        returns the x value if so. Finally, if none of the above happens, it returns None. 
        
        Parameters: 
        computerColor - an integer indicating the computer's disc color
        playerColor - an integer indicating the player's disc color
        
        Returns:
        self.checkReach(playerColor) - a function that returns the x value that computer should
        drop the disc
        None - None type object 
        """
        
        if self.checkReach(computerColor) == None:
            if self.checkReach(playerColor) == None:
                return None
            else:
                return self.checkReach(playerColor)
        else:
            return self.checkReach(computerColor)
    
    
    def computerAlgorithm(self, computerColor, playerColor):
        """
        This method creates the computer intelligence and sets up how the
        computer will play the game. First, if the difficulty is "Easy,"
        it randomly updates the position where a disc should be dropped. 
        If the difficulty is "Hard", it calls the 
        computerHardMove(computerColor, playerColor). If the 
        computerHardMove(computerColor, playerColor) returns an x value
        it will upadate x value to that column. If 
        computerHardMove(computerColor, playerColor) returns None, then it will
        randomly updates the position. It uses self.heightDiscStop(col)
        to update the y-value as well. 
        
        Parameters: 
        computerColor - an integer indicating the computer's disc color
        playerColor - an integer indicating the player's disc color
        """
        
        if self.difficulty == 0:
            self.computerEasyMove()
        elif self.difficulty == 1:
            if self.computerHardMove(computerColor, playerColor) != None:
                self.xCor = self.computerHardMove(computerColor, playerColor)
                col = (self.xCor - 64) // 92
                self.yCor = self.heightDiscStop(col)
            else:
                self.computerEasyMove()
        
        
    def checkIfFull(self):
        """
        This method checks whether the board is full. 
        
        Returns:
        True - True if the board is full
        False - False if not
        """
        
        discNum = 0
        
        for row in range(6):
            for col in range(7):
                if self.boardStatus[row][col] != 0.0:
                    discNum += 1
        
        if discNum >= 42:
            return True
        
        else:
            return False
        
        
    def dropDisc(self, color): #How do i convert this to color
        """
        This method takes in one parameter color. It calls 
        the Disc class to create a disc object. Then, it drops the 
        colored disc into the poisiton and change the board status. 
        
        Parameters:
        color - an integer indicating the disc color
        """
        
        if color == 1.0:
            color1 = "pink"
        elif color == 2.0:
            color1 = "light blue"
        
        disc = Disc(self.board.win, self.xCor, self.yCor, color1)
        disc.dropAnimation()
        row = 5 - int((self.yCor - 50) // 60)
        col = int((self.xCor - 64) // 92)
        self.boardStatus[row][col] = color
        
        
    def turn(self, computerColor, playerColor):
        """
        This methods calls many functions and determines
        how the player and computer take turns in the game. 
        Depending on the results of the game, it shows either
        winScreen(), loseScreen(), or tieGameScreen() from the Board class. 
        Then, it calls chooseEndorNew() to let decide player if he wants 
        to play a new game or quit (To quit the player can click anywhere on 
        the screen).
        
        Parameters: 
        computerColor - an integer indicating the computer's disc color
        playerColor - an integer indicating the player's disc color
        
        Returns:
        "q" - a string and will lead the player to the main menu
        "i" - a string and will lead the player to the instructions
        self.chooseEndOrNew() - it will either return "n", which updates
        the board and start a new game, or close the window
        """
        
        count = 1
        
        while True:
            
            self.turn = graphics.Text(graphics.Point(125, 450), count)
            self.turn.setSize(30)
            self.turn.setStyle("bold")
            self.turn.draw(self.board.win)
            
            #Player's turn
            playersTurn = self.playerMove()
            
            if playersTurn == "q": 
                return "q"
            elif playersTurn == "i":
                return "i"
            
            self.dropDisc(playerColor)
            
            if self.checkIfConnected(4, playerColor) == True:
                time.sleep(1.0)
                self.board.winScreen()
                return self.chooseEndOrNew()
                
            if self.checkIfFull() == True:
                time.sleep(1.0)
                self.board.tieGameScreen()
                return self.chooseEndOrNew()
            
            #Computer's turn
            self.computerAlgorithm(computerColor, playerColor)
            
            self.dropDisc(computerColor)
            
            if self.checkIfConnected(4, computerColor) == True:
                time.sleep(1.0)
                self.board.loseScreen()
                return self.chooseEndOrNew()
                
            if self.checkIfFull() == True:
                time.sleep(1.0)
                self.board.tieGameScreen()
                return self.chooseEndOrNew()
                
            count += 1
            self.turn.undraw()
            
    
def gamePlay():
    """
    This function calls intro() from Menu class and turn()
    from Game to actually play the whole game. If the situation is 
    "i" it leads player to the instruction pages. If the situation is 
    "n" it lets player begin a new game. If the situation is 
    "q" it leads player to the main menu. The player may click anywhere 
    to close the window when he finishes the game 
    """
    
    menu = Menu()
    aDict = menu.intro()
    difficulty = aDict["Difficulty"]
    player = aDict["Player"]
    computer = aDict["Computer"]
    menu.win.close()
    game = Game(difficulty)
    situation = game.turn(computer, player)
    
    while (situation == "i") or (situation == "q") or (situation == "n"):
        
        if situation == "i":
            game.board.win.close()
            menu = Menu()
            menu.instructions()
            menu.win.close()
            game = Game(difficulty)
            situation = game.turn(computer, player)    
    
        if situation == "q":
            game.board.win.close()
            menu = Menu()
            aDict = menu.intro()
            difficulty = aDict["Difficulty"]
            player = aDict["Player"]
            computer = aDict["Computer"]
            menu.win.close()
            game = Game(difficulty)
            situation = game.turn(computer, player)
        
        if situation == "n":
            game.board.win.close()
            menu = Menu()
            menu.win.close()
            game = Game(difficulty)
            situation = game.turn(computer, player)
        

def main():
    """
    The main function calls gamePlay() to play the game. 
    """
    
    gamePlay()

if __name__ == '__main__':
    main()