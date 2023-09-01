# Import tkinter construct
from tkinter import *
import tkinter.messagebox

# Create a variable to set up calling of tkinter class methods
root = Tk()

# Create and define global variables to be used in this program
click = True
count = 0

# Create text variables (associated w/ widgets in tkinter)
# (Using strings to determines who wins via whatever string is stored
#   'X' or 'O' in text variable)
btn1 = StringVar()
btn2 = StringVar()
btn3 = StringVar()
btn4 = StringVar()
btn5 = StringVar()
btn6 = StringVar()
btn7 = StringVar()
btn8 = StringVar()
btn9 = StringVar()
xPhoto = PhotoImage(file = "X.png")
oPhoto = PhotoImage(file = "o.png")

# Change the icon of the GUI via iconbitmap method
root.iconbitmap("tic tac toe.ico")

# Change the title of the GUI via title method
root.title("Tic Tac Toe")

# Set the width and height of GUI to false 
root.resizable(False, False)

# Define a function called play
    # Allows user to play the game
def play():
    
    # Create button variables and place location of button on grid
    button1 = Button(root, height = 9, width = 19, relief = "ridge",
              borderwidth = 1, bg = "#f2d1fa",
              textvariable = btn1, command = lambda: press(1,0,0))
    button1.grid(row = 0, column = 0)
    
    button2 = Button(root, height = 9, width = 19, relief = "ridge",
              borderwidth = 1, bg = "#f2d1fa",
              textvariable = btn2, command = lambda: press(2,0,1))
    button2.grid(row = 0, column = 1)
    
    button3 = Button(root, height = 9, width = 19, relief = "ridge",
              borderwidth = 1, bg = "#f2d1fa",
              textvariable = btn3, command = lambda: press(3,0,2))
    button3.grid(row = 0, column = 2)
    
    button4 = Button(root, height = 9, width = 19, relief = "ridge",
              borderwidth = 1, bg = "#e6a4f4",
              textvariable = btn4, command = lambda: press(4,1,0))
    button4.grid(row = 1, column = 0)
    
    button5 = Button(root, height = 9, width = 19, relief = "ridge",
              borderwidth = 1, bg = "#e6a4f4",
              textvariable = btn5, command = lambda: press(5,1,1))
    button5.grid(row = 1, column = 1)
    
    button6 = Button(root, height = 9, width = 19, relief = "ridge",
              borderwidth = 1, bg = "#e6a4f4",
              textvariable = btn6, command = lambda: press(6,1,2))
    button6.grid(row = 1, column = 2)
    
    button7 = Button(root, height = 9, width = 19, relief = "ridge",
              borderwidth = 1, bg = "#d976ef",
              textvariable = btn7, command = lambda: press(7,2,0))
    button7.grid(row = 2, column = 0)
    
    button8 = Button(root, height = 9, width = 19, relief = "ridge",
              borderwidth = 1, bg = "#d976ef",
              textvariable = btn8, command = lambda: press(8,2,1))
    button8.grid(row = 2, column = 1)
    
    button9 = Button(root, height = 9, width = 19, relief = "ridge",
              borderwidth = 1, bg = "#d976ef",
              textvariable = btn9, command = lambda: press(9,2,2))
    button9.grid(row = 2, column = 2)
    

# Define a function called press
    # Allows user to check which button user presses
def press(num,r,c):
    
    # Get global variables
    global count, click

    # Create an if-else statement to determine which image will appear
    #   (x or o) based on a click
    if click == True:
        labelPhoto = Label(root, image = xPhoto)
        labelPhoto.grid(row = r, column = c)
        # Create nested multi-way if-else statements to set the pressed 
        #   button number to a text varaiable for that button number
        if num == 1:
            btn1.set("X")
        elif num == 2:
            btn2.set("X")
        elif num == 3:
            btn3.set("X")
        elif num == 4:
            btn4.set("X")
        elif num == 5:
            btn5.set("X")
        elif num == 6:
            btn6.set("X")
        elif num == 7:
            btn7.set("X")
        elif num == 8:
            btn8.set("X")
        else:
            btn9.set("X")
        count += 1
        click = False
        checkWin()
        
    else:
        labelPhoto = Label(root, image = oPhoto)
        labelPhoto.grid(row = r, column = c)
        if num == 1:
            btn1.set("O")
        elif num == 2:
            btn2.set("O")
        elif num == 3:
            btn3.set("O")
        elif num == 4:
            btn4.set("O")
        elif num == 5:
            btn5.set("O")
        elif num == 6:
            btn6.set("O")
        elif num == 7:
            btn7.set("O")
        elif num == 8:
            btn8.set("O")
        else:
            btn9.set("O")
        count += 1
        click = True
        checkWin()

play()     
# Define a function called checkWin
    # Checks if there is a winner for the game
def checkWin():
    # Get global variables
    global count, click
    
    # Possible ways to win game:
        # Across positions:(1 2 3) or (4 5 6) or (7 8 9)
        # Vertical positions: (1 4 7) or (2, 5, 8) or (3 6 9)
        # Diagonal positions (1 5 9) or (3 5 7)
    # Create if-else statements to determine the winning scenarios
    # Get the values stored in the text variable buttons
    if ((btn1.get() == "X" and btn2.get() == "X" and btn3.get() == "X") or
        (btn4.get() == "X" and btn5.get() == "X" and btn6.get() == "X") or
        (btn7.get() == "X" and btn8.get() == "X" and btn9.get() == "X") or
        (btn1.get() == "X" and btn4.get() == "X" and btn7.get() == "X") or
        (btn2.get() == "X" and btn5.get() == "X" and btn8.get() == "X") or
        (btn3.get() == "X" and btn6.get() == "X" and btn9.get() == "X") or
        (btn1.get() == "X" and btn5.get() == "X" and btn9.get() == "X") or
        (btn3.get() == "X" and btn5.get() == "X" and btn7.get() == "X")) :
        tkinter.messagebox.showinfo("Tic Tac Toe", "Player X Wins! :D")
        
        # Reset click to true (X) and count to 0 for restart of game
        click = True
        count = 0

        # Call clear and play functions to reset game
        clear()
        play()

    elif((btn1.get() == "O" and btn2.get() == "O" and btn3.get() == "O") or
         (btn4.get() == "O" and btn5.get() == "O" and btn6.get() == "O") or
         (btn7.get() == "O" and btn8.get() == "O" and btn9.get() == "O") or
         (btn1.get() == "O" and btn4.get() == "O" and btn7.get() == "O") or
         (btn2.get() == "O" and btn5.get() == "O" and btn8.get() == "O") or
         (btn3.get() == "O" and btn6.get() == "O" and btn9.get() == "O") or
         (btn1.get() == "O" and btn5.get() == "O" and btn9.get() == "O") or
         (btn3.get() == "O" and btn5.get() == "O" and btn7.get() == "O")) :
         tkinter.messagebox.showinfo("Tic Tac Toe", "Player O Wins! :D")

         count = 0
         clear()
         play()
         
    elif(count == 9):
        tkinter.messagebox.showinfo("Tic Tac Toe", "It's a tie!")
        click = True
        count = 0
        clear()
        play()
    
    
# Define a function called clear
    # Resets buttons for user to play game again
def clear():
    # Reset each of the text variables to an empty string
    btn1.set("")
    btn2.set("")
    btn3.set("")
    btn4.set("")
    btn5.set("")
    btn6.set("")
    btn7.set("")
    btn8.set("")
    btn9.set("")

    
# Call the main method for tkinter GUI to run
root.mainloop()










