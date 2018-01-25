from tkinter import *
import time
import random

root = Tk()
root.title("Bounce!")
root.geometry("510x320")
root.resizable(False,False)         #make window non-resizable
canvas = Canvas(root, width = 300, height = 300, bd = 0, highlightthickness = 3,
                highlightbackground = "#2d3536", bg = "grey")
canvas.pack(side = "right", padx = 10, pady = 10,)
root.update()



class Ball:
   def __init__(self, canvas, color):
      self.canvas = canvas
      self.Xboundry = self.canvas.winfo_width() - 3
      self.Yboundry = self.canvas.winfo_height() - 3
      self.color  = "purple"
      self.Xcoord = random.randint(0,self.Xboundry)
      self.Ycoord = random.randint(0,self.Yboundry)
      self.Xvel   = 1
      self.Yvel   = 1
      self.size   = 10
      self.id = canvas.create_oval(self.Xcoord, self.Ycoord,
                                   self.Xcoord + self.size,
                                   self.Ycoord + self.size, fill = self.color)

   def move(self):
      if (self.Xcoord + self.size) > self.Xboundry or self.Xcoord < 3:
         self.Xvel *= -1
         self.color = random.choice(["blue", "red", "yellow", "purple", "orange", "green"])
      if (self.Ycoord + self.size) > self.Yboundry or self.Ycoord < 3:
         self.Yvel *= -1
         self.color = random.choice(["blue", "red", "yellow", "purple", "orange", "green"])

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
