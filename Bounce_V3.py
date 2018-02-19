from tkinter import *
import time
import random
import math


class Item:
   def __init__(self, board, width, height, color):
      self.board   = board
      self.bound = [3, self.board.winfo_width() - 3,  #[L, R, T, B]
                     3, self.board.winfo_height() - 3]
      self.width   = width
      self.height  = height
      self.x    = random.randint(10, self.bound[1] - width - 10)
      self.y    = random.randint(10, self.bound[3] - height - 10)
      self.angle   = random.randint(0,int(2*math.pi)) #radians
      self.speed   = random.randint(1,5)
      self.color   = color

   def move(self):
      self.x += math.sin(self.angle) * self.speed
      self.y += math.cos(self.angle) * self.speed
      
      if self.x < self.bound[0] or self.x + self.width  > self.bound[1]: self.angle *= -1
      if self.y < self.bound[2] or self.y + self.height > self.bound[3]: self.angle = math.pi - self.angle      
      self.board.coords(self.ID, self.x, self.y, (self.x + self.width), (self.y + self.height))
      
      

class Ball(Item):
   def __init__(self, board, width, height, color):
      super().__init__(board, width, height, color)
      self.ID   = board.create_oval(self.x, self.y, (self.x + width), (self.y + height), fill = color)


      

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

ball_list = []
for i in range(5):
   ball_list.append(Ball(board, 10, 10, "orange"))

while True:
   for i in ball_list:
      i.move()

   root.update_idletasks()
   root.update()
   time.sleep(0.01)

root.mainloop()























