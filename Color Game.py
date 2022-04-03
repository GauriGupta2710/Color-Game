import tkinter
import random
from tkinter.font import BOLD
  
# list of possible colour.
colours = ['Red','Blue','Green','Pink','Black',
           'Yellow','Orange','White','Purple','Brown']
score = 0
  
# the game time left, initially 30 seconds.
timeleft = 30
  
# function that will start the game.
def startGame(event):
      
    if timeleft == 30:
          
        # start the countdown timer.
        countdown()
          
    # run the function to
    # choose the next colour.
    nextColour()
    if timeleft==0:
        display_result()
  
# Function to choose and
# display the next colour.
def nextColour():
  
    # use the globally declared 'score'
    # and 'play' variables above.
    global score
    global timeleft
  
    # if a game is currently in play
    if timeleft > 0:
  
        # make the text entry box active.
        e.focus_set()
  
        # if the colour typed is equal
        # to the colour of the text
        if e.get().lower() == colours[1].lower():
              
            score += 1
  
        # clear the text entry box.
        e.delete(0, tkinter.END)
          
        random.shuffle(colours)
          
        # change the colour to type, by changing the
        # text _and_ the colour to a random colour value
        label.config(fg = str(colours[1]), text = str(colours[0]))
          
        # update the score.
        scoreLabel.config(text = "Score: " + str(score))
        
  
  
# Countdown timer function 
def countdown():
  
    global timeleft
  
    # if a game is in play
    if timeleft > 0:
  
        # decrement the timer.
        timeleft -= 1
          
        # update the time left label
        timeLabel.config(text = "Time left: "
                               + str(timeleft))
                                 
        # run the function again after 1 second.
        timeLabel.after(1000, countdown)

def display_result():
    result.config(text = "\nGame Finished!!\n"+"Final Score: "+str(score))


root = tkinter.Tk()
root.title("Color Game")
root.geometry("375x300")
root['bg'] = '#49A'

instructions = tkinter.Label(root, text = "Type in the colour of the words,\n and not the word text!",font = ('Helvetica', 12,BOLD),background='#49A',foreground="#113c62")
instructions.pack() 

scoreLabel = tkinter.Label(root, text = "Press enter to start",
                                      font = ('Helvetica', 12,BOLD),background='#49A',foreground="#616161")
scoreLabel.pack()

timeLabel = tkinter.Label(root, text = "Time left: " +
              str(timeleft), font = ('Helvetica', 12,BOLD),background='#49A',foreground="#616161")
                
timeLabel.pack()
  
label = tkinter.Label(root, font = ('Helvetica', 60),background='#49A')
label.pack()

e = tkinter.Entry(root)

root.bind('<Return>', startGame)
e.pack()

e.focus_set()

result = tkinter.Label(root,font=('Helvetica', 14,BOLD),background='#49A')
result.pack()

root.mainloop()