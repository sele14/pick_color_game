from graphics import *
from random import *
# A list of colors for later use
cnames = ["Green", "Blue", "Yellow", "Gray", "Pink", "Orange", "Purple", "Red", "Brown"]

# A function used to generate indecies for accompanying colors
def randomize():
    other_cnames = []
    while len(other_cnames) < 6:
        r1 = randint(0, len(cnames)-1) # Returns random index
        if r1 not in other_cnames:
            other_cnames.append(r1)
    color = other_cnames[randint(0, 5)]
    cname = other_cnames[randint(0, 5)]
    return(color, cname, other_cnames)

def intro(win): # The game's introduction window
    win.setBackground('white')

    # Drawing the interface with text boxes and input box
    txt1 = Text(Point(300, 150), "Select key assigned to the color not the word!")
    txt1.draw(win)

    txt2 = Text(Point(300, 220), "How many rounds do you want to play?")
    txt2.draw(win)

    txt3 = Text(Point(300, 400), "Click anywhere to start a game.")
    txt3.draw(win)

    input_box = Entry(Point(300, 300), 6)
    input_box.draw(win)
    
    win.getMouse()
    # Take the amount of times the user wants to play
    n = eval(input_box.getText())

    # Create a blank screen for the next section of the game
    txt1.undraw()
    txt2.undraw()
    txt3.undraw()
    input_box.undraw()
    
    return n
    
def draw_round(win): # The "game mechanics"
    result = False
    color, cname, other_cnames = randomize()
    win.setBackground('white')
 
    # The main text for colors and numbers
    rcname = cnames[cname]
    rcname = rcname[0].upper() + rcname[1:]
    target = Text(Point(300, 400), rcname)
    target.setOutline(cnames[color])
    target.setStyle("bold")
    target.setSize(24)
    target.draw(win)

    boxes = []
    a = 250
    b = 170
    k = 0
    
    # A loop to generate a list of colors and numbers for the boxes
    for i in range(3):
        for j in range(2):
            txt = Text(Point(a + j*110, b + i*60),str(k)+"/"+str(cnames[other_cnames[k]]))
            boxes.append(txt)
            txt.setSize(14)
            txt.draw(win)
            k = k + 1

    key = win.getKey()
    
    # Checking if the user is correct 
    if other_cnames[int(key)] == color:
        result = True    
    
    key = win.checkKey()
    target.undraw()
    for i in boxes:
        i.undraw()

    return result

def win1(win): # The "You Win" screen
    win.setBackground(color_rgb(16,253,16))

    txt1 = Text(Point(300, 300), "You win!")
    txt1.draw(win)
    txt1.setFace("arial")
    txt1.setSize(30)
    txt1.setStyle("bold")
    
    txt2 = Text(Point(300, 410), "Click anywhere to play again.")
    txt2.draw(win)

    box = Rectangle(Point(200, 430), Point(400, 450))
    box.draw(win)
    
    # A "close" button
    txt3 = Text(Point(300,440),"Close")
    txt3.draw(win)

    p = win.getMouse()
    x = p.getX()
    y = p.getY()

    if 200 < x < 400 and 430 < y < 450:
        return False
    else:
        win.getMouse()
        txt1.undraw()
        txt2.undraw()
        txt3.undraw()
        box.undraw()
        return True

def lose(win): # The "you lose" screen
    win.setBackground(color_rgb(255, 0, 0))

    txt1 = Text(Point(300, 300), "GAME OVER!!!")
    txt1.draw(win)
    txt1.setFace("arial")
    txt1.setSize(30)
    txt1.setStyle("bold")

    txt2 = Text(Point(300, 410), "Click anywhere to play again.")
    txt2.draw(win)

    box = Rectangle(Point(200, 430), Point(400, 450))
    box.draw(win)

    # A "close" button
    txt3 = Text(Point(300,440),"Close")
    txt3.draw(win)

    p = win.getMouse()
    x = p.getX()
    y = p.getY()

    if 200 < x < 400 and 430 < y < 450:
        return False
    else:
        win.getMouse()
        txt1.undraw()
        txt2.undraw()
        txt3.undraw()
        box.undraw()
        return True

# Our main function where we combine all the functions into our game.
def main():
    run = True
    win = GraphWin("New_game", 600, 600)
    while run:
        win.setBackground("white")
        n = intro(win)
        for i in range(n):
            result = draw_round(win)
            if result == False:
                break
        if result:
            run = win1(win)
        else:
            run = lose(win)

    win.close()

main()
