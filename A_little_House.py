#using GraphWin create a house

from graphics import *
import random

#constants
COLOURS = ['SeaGreen1', 'tomato', 'goldenrod', 'turquoise2', 'RoyalBlue2','SeaGreen1', 'tomato', 'goldenrod', 'turquoise2']
WIN_W, WIN_H = 500, 400

# Main function
def main(): 
    win = GraphWin("A Little Program", WIN_W, WIN_H)
    info = info_create(win, 250, 30, "House title")
    quit_button = button_create(win, 400, 75, 75,35,"Quit")
    reset_button = button_create(win, 400, 135, 75,35,"Reset")
    house = create_house(win, main)
    house_colours(house)

    # while loop include: - quit and reset color button
    #                     - house color change
    #                     - get mouse click coordinate
    while True:
        try:
            pt = win.getMouse()
                
        except GraphicsError:
            return  
        
        if is_clicked(pt, quit_button):
            info.setText("Quitting the program")
            break
        elif is_clicked(pt, reset_button):
            info.setText("Reset House Colour")
            house_colours(house)      
            
        elif is_clicked(pt, house[1]):
            bg_colour = random.choice(COLOURS)
            string = "Left Window" + ": " + bg_colour
            info.setText(string)
            win.flush()
            house[1][0].setFill(bg_colour)
    
        elif is_clicked(pt, house[2]):
            bg_colour = random.choice(COLOURS)
            string = "Right Window" + ": " + bg_colour
            info.setText(string)
            win.flush()
            house[2][0].setFill(bg_colour)
    
        elif is_clicked(pt, house[4]):
            bg_colour = random.choice(COLOURS)
            string = "Door" + ": " + bg_colour
            info.setText(string)
            win.flush()
            house[4][0].setFill(bg_colour)
            
        elif is_clicked(pt, house[0]):
            bg_colour = random.choice(COLOURS)
            string = "Main Floor" + ": " + bg_colour
            info.setText(string)
            win.flush()
            house[0][0].setFill(bg_colour)        
        
        elif in_Triangle(pt, house[3]):
            bg_colour = random.choice(COLOURS)
            string = "Roof" + ": " + bg_colour
            info.setText(string)
            win.flush()
            house[3].setFill(bg_colour)            
            
        
        else:
            x = pt.getX()
            y = pt.getY()
            string = "MOUSE CLICK AT: (" + str(x) + ", " + str(y) + ")"
            info.setText(string)
    
    win.close()
    
# This creates and returns a text object with the text "Sophie’s House"
def info_create(win, x, y, text):
    title = Text(Point(x, y), "Wenwan's House")
    title.setSize(20)
    title.setTextColor("OliveDrab4")
    title.draw(win)
    
    return title

# This calls rect_create, creates a “button” object, drawing the “text” on
# the button. This function returns a "button", consisting of a list with a
# Rectangle and a Text.
def button_create(win, x, y, width, height, text):
    
    button = Rectangle(Point(x, y),\
                       Point(x + width, y + height))
    button.draw(win)
   
    label = Text(Point(x + width//2, y + height//2), text)
    label.setSize(18)
    label.setTextColor("DeepSkyBlue2")
    label.draw(win)
    
    return [button, label]

# This creates and returns a rectangle, consisting of a list with a Rectangle
# and an object name
def rect_create(win, x, y, width, height, text):
    rectangle = Rectangle(Point(x, y),\
                          Point(x + width, y + height))
    #rectangle.setFill('red')
    rectangle.draw(win)
    
    return [rectangle, Text]    

# This creates and returns a triangle
def draw_triangle(win, x, y, width, height):
    triangle = Polygon(Point(x, y),\
                       Point(x-width//2, y+height),\
                       Point(x+width//2, y+height))
    #triangle.setFill('green') 
    triangle.draw(win)    
    return triangle

# Returns True if pt.x and pt.y are within rectangle; else False
def in_Rectangle(pt, rectangle):
    top_left = rectangle[0].getP1()
    rectangle_right = rectangle[0].getP2()
    
    return (top_left.x <= pt.x <= rectangle_right.x and
            top_left.y <= pt.y <= rectangle_right.y)

# Returns True if pt.x and pt.y are within the Polygon triangle; else False
def in_Triangle(pt, triangle):
    position = triangle.getPoints()
    return (position[1].x <= pt.x <= position[2].x and
             position[0].y<= pt.y <= position[1].y) 

# This creates a house with Rectangle objects for main floor, door, left
# and right windows, a Polygon for the roof, and returns a list consisting
# of the objects just described
def create_house(win, main):
    
    main_floor = rect_create(win, 125, 140, 250, 140,"Main Floor")
    roof = draw_triangle(win, 250, 60, 250, 80) 
    left_window = rect_create(win, 140, 160, 60, 30, "Left Window")
    right_window = rect_create(win, 300, 160, 60, 30, "Right Window")
    door = rect_create(win, 235, 230, 25, 50, "Door")
    house = [main_floor, left_window, right_window, roof, door]
    
    return[main_floor, left_window, right_window, roof, door]

# set up house colors
house=[]
def house_colours(house):
    house[0][0].setFill('red')
    house[1][0].setFill('white')
    house[2][0].setFill('yellow')
    house[3].setFill('green')
    house[4][0].setFill('brown')    
    
# get mouse click point coordinate

def is_clicked(point, button):
    top_left = button[0].getP1()
    bottom_right = button[0].getP2()
    
    return (top_left.x <= point.x <= bottom_right.x and
            top_left.y <= point.y <= bottom_right.y)    
