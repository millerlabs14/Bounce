from tkinter import *
import time
import random

root = Tk()
root.title("Bounce!")
root.resizable(False,False)         #make window non-resizable
root.wm_attributes("-topmost", 1)    #place in front of other windows
canvas = Canvas(root, width = 500, height = 500, bd = 0,
                highlightthickness = 0, bg = "grey")
canvas.pack()
root.update()



class Ball:
   def __init__(self, canvas, color):
      self.color  = "purple"
      self.Xcoord = 132
      self.Ycoord = 478
      self.Xvel   = 1
      self.Yvel   = 1
      self.size   = 10
      self.canvas = canvas
      self.id = canvas.create_oval(self.Xcoord, self.Ycoord,
                                   self.Xcoord + self.size,
                                   self.Ycoord + self.size, fill = self.color)

   def move(self):
      Xboundry = self.canvas.winfo_width()
      Yboundry = self.canvas.winfo_height()

      if (self.Xcoord + self.size) > Xboundry or self.Xcoord < 0:
         self.Xvel *= -1
         self.color = random.choice(["blue", "red", "yellow", "purple", "black", "white", "orange"])
      if (self.Ycoord + self.size) > Yboundry or self.Ycoord < 0:
         self.Yvel *= -1
         self.color = random.choice(["blue", "red", "yellow", "purple", "black", "white", "orange"])

      self.canvas.itemconfig(self.id, fill = self.color)
      self.canvas.move(self.id, self.Xvel, self.Yvel)
      self.Xcoord = self.canvas.coords(self.id)[0]
      self.Ycoord = self.canvas.coords(self.id)[1]


ball = Ball(canvas, "blue")


while True:
   ball.move()
   root.update_idletasks()
   root.update()
   time.sleep(0.01)
