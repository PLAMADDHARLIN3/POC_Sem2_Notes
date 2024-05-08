import tkinter as tk

class Game(tk.Frame):
    def __init__(self, master):
        super(Game, self).__init__(master)
        self.lives = 3
        self.width = 600
        self.height = 400
        self.bg = "#AAAAFF"
        self.canvas = tk.Canvas(self, width=self.width, height=self.height, bg=self.bg)        
        self.canvas.pack()
        self.pack()

class GameObject(object):
    def __init__(self, canvas, item):
        self.canvas = canvas
        self.item = item

    def get_position(self):
        return self.canvas.coords(self.item)
    
    def move(self, x, y):
        self.canvas.move(self.item, x, y)

    def delete(self):
        self.canvas.delete(self.item)

class Ball(GameObject):
    def __init__(self, canvas, x, y):  #(x, y) is the center of the ball
        #YOUDO-01: create a radius variable for self and set to 10
        #YOUDO-02: create a direction variable for self and set to [1, -1]
        #This represents the speed of the ball in the x and y direction.  Example:  [xspeed, yspeed]  
        #YOUDO-03:  create a speed variable for self and set to 10
        #YOUDO-04:  create an x1 variable and set to x - self's radius
        #YOUDO-05:  create an y1 variable and set to y - self's radius
        #YOUDO-06:  create an x2 variable and set to x + self's radius
        #YOUDO-07:  create an y2 variable and set to y + self's radius  
        #YOUDO-08:  create a color variable and set to "white"
        item = canvas.create_oval(x1, y1, x2, y2, fill=color)
        super(Ball, self).__init__(canvas, item)

class Paddle(GameObject):
    def __init__(self, canvas, x, y):  #(x, y) is the center of the paddle
        #YOUDO-09:  create a width variable for self and set to 80
        #YOUDO-10:  create a height variable for self and set to 10
        #YOUDO-11:  create a ball variable for self and set to None
        #YOUDO-12:  create an x1 variable and set to x - self's width / 2
        #YOUDO-13:  create an y1 variable and set to y - self's height / 2
        #YOUDO-14:  create an x2 variable and set to x + self's width / 2
        #YOUDO-15:  create an y2 variable and set to y + self's height / 2
        #YOUDO-16:  create a color variable and set to "blue"
        #YOUDO-17:  use create_rectangle on canvas to create an item variable with x1, y1, x2, y2, color
        super(Paddle, self).__init__(canvas, item)
        

    def set_ball(self, ball):
        self.ball = ball

    def move(self, offset):
        coords = self.get_position()
        width = self.canvas.winfo.width()
        x1 = coords[0]
        y1 = coords[1]
        x2 = coords[2]
        y2 = coords[3]
        if x1 + offset >= 0 and x2 + offset <= width:
            super(Paddle, self).move(offset, 0)
        if self.ball is not None:
            self.ball.move(offset, 0)

class Brick(GameObject):
    COLORS = {1 : "#999999", 2 : "#555555", 3 : "#222222"}

    def __init__(self, canvas, x, y, hits):
        #YOUDO-18:  create a width variable for self and initialize to 75
        #YOUDO-19:  create a height variable for self and initialize to 20
        #YOUDO-20:  create a hits variable for self and initialize to hits 
        color = Brick.COLORS[hits]
        #YOUDO-21:  create an x1 variable and set to x - self's width / 2
        #YOUDO-22:  create an y1 variable and set to y - self's height / 2
        #YOUDO-23:  create an x2 variable and set to x + self's width / 2
        #YOUDO-24:  create an y2 variable and set to y + self's height / 2
        #YOUDO-25:  use create_rectangle on canvas to create an item variable with x1, y1, x2, y2, color, tags="brick"        
        super(Brick, self).__init__(canvas, item)

    def hit(self):
        #YOUDO-26:  subtract one from self.hits
        #YOUDO-27:  check if self.hits is equal to 0.  If it is call self.delete().  If not 
        #YOUDO-27-part2:  call self.canvas.itemconfig(self.item, fill=Brick.COLORS[self.hits])
        pass #YOUDO-28:  Remove this pass


if __name__ == "__main__":    
    root = tk.Tk()
    game = Game(root)
    root.title("BREAKOUT")
    root.mainloop()