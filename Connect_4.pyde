def setup(): # Setup function where basis of game begins
    global homescreen, homeFont, gamemode, turn, holes, win, count
    gamemode = "MENU";
    background(0) # Sets colour of screen
    size(800,600) # Sets screen size
    turn = "2"    
    holes = [[0 for x in range (7)] for y in range (6)]
    win = False
    count = 42
    
   # add_library("minim")
   # minim=Minim(this)
   # sound = minim.loadFile("GameMusic.wav")
   # sound.loop()
    
def keyPressed():
    global gamemode
    if (gamemode == "MENU"):  #This key press function moves from screen to screen
        if (keyCode == LEFT): #For ex. From Menu to Instructions to the Actual Gamescreen
            gamemode = "INSTRUCTIONS";
            
    if (gamemode == "MENU"): 
        if (keyCode == RIGHT):
            gamemode = "GAMESCREEN";
    
    if (gamemode == "INSTRUCTIONS"):
        if (keyCode == DOWN):
            gamemode = "GAMESCREEN";

def draw():
    global gamemode, homeFont, instructionsText, gameboard, drawscreen, winscreen
    global turn,holes,win,count
    if gamemode == "MENU":        
            homescreen = loadImage("homescreen.jpg") #These two lines load an image as the background 
            image(homescreen,0,0,800,600)
    
            homeFont = createFont("Games.ttf",60) #Loads custom font and prints text onto screen
            fill(255)
            textFont(homeFont)
            text("Welcome to Connect 4!",45,250)
    
            homeFont = createFont("Games.ttf",30)
            textSize(20)
            text("Press LEFT for Instructions",55,280)
            text("Press RIGHT to Start",545,280)
            text("By Omer and Iman",20,590)
    
    if gamemode == "INSTRUCTIONS":
            background(0)  #Prints all the instructions onto the screen 
            textSize(50)
            text("HOW TO PLAY?",400,45)
            textSize(25)
            text("Press DOWN to Play",140,570)
            textAlign(CENTER, CENTER);
            instructionsText = createFont("InstructionsText.otf",30)
            textFont(instructionsText)
            textSize(20);
            text(" OBJECTIVE : To win Connect Four you must be the first player",350,125) 
            text("to get four of your colored checkers in a row either horizontally,",380,150)
            text("vertically or diagonally.",200,175)
            text("1. Decide who plays first. Players will alternate turns after",355,200)
            text("playing a checker.",170,225)
            text("2. On your turn, click on any one of the columns to drop the",355,250)
            text("checker onto the grid.",185,275)
            text("3. Players alternate until one players get 4 of their coulered",355,300) 
            text("checkers in a row which could be diagonall, vertically or",340,325)
            text("horizontally.",145,350)

    
    if gamemode == "GAMESCREEN":
            gameboard = loadImage("Board.png") #Loads an image as the board and draws all the game pieces onto the screen 
            image(gameboard,0,0,800,600)
             #Drawing the pieces
            for x in range (7):
                for y in range (6):
                    x1 = 57 + 115 * x
                    y1 = 550 - 100 * y
                    if holes [y][x] == "1":
                        fill (255,0,0)
                        ellipse (x1, y1, 90,75)
                    elif holes [y][x] == "2":
                        fill (255,255,0)
                        ellipse (x1, y1, 90,75)
                for y in range(6):
                    for x in range(4):                
                        if holes[y][x:x+4] == [holes[y][x]] * 4 and holes[y][x] != 0:
                            win = True
                            
        #Vertical win detection            
                for y in range(3):
                    for x in range(7):
                        if [holes[n][x] for n in range(y, y + 4)] == [holes[y][x]] * 4 and holes[y][x] != 0:
                            win = True
                    
        #Diagonal win detection            
                for x in range(4):
                    for y in range(3):
                        if [holes[y + n][x + n] for n in range(4)] == [holes[y][x]] * 4 and holes[y][x] != 0:
                            win = True
                    
                for x in range(4):
                    for y in range(5,2,-1):
                        if [holes[y - n][x + n] for n in range(4)] == [holes[y][x]] * 4 and holes[y][x] != 0:
                            win = True
            #Winner        
                if win == True:
                    winscreen = loadImage("Win.jpg")
                    image(winscreen,0,0,800,600)
                    textSize (50)
                    textAlign(CENTER)
                    fill(255)
                    text ("Player %s Wins!" % ("One" if turn == "1" else "Two"),403,425)
                    text ("Click to play again",403,480)
                    #text ("Player %s Wins!" % ("One" if turn == "1" else "Two"),400,350)
                    #text ("Click to play again",400,375)
            
            #Tie    
                elif count == 0:
                    fill (0)
                    drawscreen = loadImage("Tie.jpg")
                    image(drawscreen,0,0,800,600)
                    textSize (50)
                    textAlign(CENTER)
                    text ("It's a tie!",403,303)
                    text ("Click to play again",403,353)
                    #fill (255)
                    #text ("It's a tie!",400,300)
                    #text ("Click to play again",400,350)
    
def mousePressed():
    global turn,holes,win,count   #Mouse function for detecting a mouse click and drawing a piece in the designated area
    #Mouse Coordinates
    x = mouseX/113
    if win == False:
        #Game resets if there is a tie
        if count == 0:
            holes = [[0 for x in range (7)] for y in range (6)]   
            win = False
            count = 42
        #Turn Switch    
        else:
            for y in range(7):
                if y == 6:
                    break
                if not holes[y][x]:
                    break
            if y != 6:
                if turn == "1":
                    turn = "2"
                elif turn == "2":
                    turn = "1"
                holes [y][x] = turn
                count -= 1
    #Game Reset if there is a winner
    else:
        holes = [[0 for x in range (7)] for y in range (6)]   
        win = False 
        count = 42                                            
