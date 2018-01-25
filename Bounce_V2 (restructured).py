from tkinter import *
import time
import random


class Item:
   def __init__(self, board, width, height, color):
      self.board  = board
      self.Tbound = 3
      self.Bbound = self.board.winfo_height() - 3
      self.Lbound = 3
      self.Rbound = self.board.winfo_width() - 3
      self.width  = width
      self.height = height
      self.Xpos   = random.randint(0, self.Rbound - width)
      self.Ypos   = random.randint(0, self.Bbound - height)
      self.Xvel   = 1
      self.Yvel   = 2
      self.color  = color

   def move(self):
      if self.Xpos < self.Lbound or self.Xpos + self.width  > self.Rbound: self.Xvel *= -1
      if self.Ypos < self.Tbound or self.Ypos + self.height > self.Bbound: self.Yvel *= -1         
      self.board.move(self.ID, self.Xvel, self.Yvel)
      self.Xpos = self.board.coords(self.ID)[0]
      self.Ypos = self.board.coords(self.ID)[1]
      
      

class Ball(Item):
   def __init__(self, board, width, height, color):
      super().__init__(board, width, height, color)
      self.ID   = board.create_oval(self.Xpos, self.Ypos, (self.Xpos + width), (self.Ypos + height), fill = color)


      

#Initial setup of window--------------------------------------------------------
#Create Window----------------
root = Tk()
root.title("Bounce!")            
root.geometry("510x320")        
root.resizable(False,False)

#Put canvas in window--------
board = Canvas(root, width = 300, height = 300, bd = 0, highlightthickness = 3,
                highlightbackground = "#2d3536", bg = "grey")
board.pack(side = "right", padx = 10, pady = 10,)
root.update()

ball = Ball(board, 10, 10, "orange")
while True:
   ball.move()
   
   root.update_idletasks()
   root.update()
   time.sleep(0.01)

root.mainloop()























