from graphics import *
import time
WIN_W, WIN_H = 500, 400
# Constants
BASE = WIN_H - WIN_H//4
POST_SP=WIN_W/4
POST_W=20
POST_H=180
# global variable
win = None
post = []
disks = []
msg_main = ""
N_entry = [3,None, None]
btn_Quit = None
btn_Reset = None

'''
Purpose: Main function: - access globals
                        - creates the main app
                        - create the main text object to display mouse click responses
                        - calls hanoi_create()
                        - engages in the main GUI loop to wait for mouse click and respond quit, reset, click on a post, anywhere else then display mouse click (x, y) coordinates
Parameter: None
Return value: none
'''
def main():
    global win, msg_main
    win = GraphWin("Hanoi Towers", WIN_W, WIN_H)
    msg_main = info_create(win, 240, 40, "WELCOME!")
    
    # Call function to create Quit and reset button
    Hanoi_create()
    while True:
        try:
            point = win.getMouse()
                
        except GraphicsError:
            return  
        # quit button and reset button feature
        if is_clicked(point, btn_Quit):
            msg_main.setText("BYE BYE")
            break
        
        elif is_clicked(point, btn_Reset):
            Hanoi_reset()
            
        else:
            clickedBox = False
            #if click inside post, change post color to yellow and reset back after 0.5 second.
            for p in posts:
                if is_clicked(point, p[1]):
                    p[1][0].setFill('yellow')
                    msg_main.setText(p[2])
                    clickedBox=True
                    time.sleep(0.5)
                    p[1][0].setFill('brown')
            if clickedBox==False:
                x = point.getX()
                y = point.getY()
                string = "MOUSE: (" + str(x) + ", " + str(y) + ")"
                msg_main.setText(string)                
                
    time.sleep(1)
    win.close()

    return

'''
Purpose: create a button function: Create a button object. Help function of Hanoi_create
Parameter: win, x, y, width, height, text
Return value: [button, label]
'''
def button_create(x, y, width, height, text):
    
    button = Rectangle(Point(x, y),\
                       Point(x + width, y + height))
    button.draw(win)
   
    label = Text(Point(x + width//2, y + height//2), text)
    label.setSize(14)
    label.draw(win)
    
    return [button, label]
'''
Purpose: This creates and returns a rectangle, consisting of a list with a Rectangle.Help function of Hanoi_create
Parameter: win, x, y, width, height, text
Return value: [rectangle, Text]
'''
def rect_create(win, x, y, width, height, text):
    rectangle = Rectangle(Point(x, y),\
                          Point(x + width, y + height))
    rectangle.draw(win)
    
    return [rectangle, Text]  

'''
Purpose: determine if mouse click is inside button. Helper function for main.
Parameter: point, button
Return value: top_left.x <= point.x <= bottom_right.x and
              top_left.y <= point.y <= bottom_right.y
'''
def is_clicked(point, button):
    top_left = button[0].getP1()
    bottom_right = button[0].getP2()
    
    return (top_left.x <= point.x <= bottom_right.x and
            top_left.y <= point.y <= bottom_right.y) 

'''
Purpose: Helper function for show_post_info.
Parameter: win, x, y, text
Return value: title
'''
def info_create(win, x, y, text):
    title = Text(Point(x, y), text)
    title.setSize(14)
    title.draw(win)
    return title

'''
Purpose: Create interface controls, button quit, button reset, base line, also call create_post() function to create posts
Parameter: None
Return value: btn_Quit, btn_Reset,base_line
'''
def Hanoi_create():
    global  btn_Quit, btn_Reset, N_entry
    btn_Quit = button_create(30, 25, 65,30,"Quit")
    btn_Reset = button_create(405, 25, 65,30,"Reset") 
    # draw base line
    base_line = Line(Point(0,BASE), Point(500,BASE))
    base_line.draw(win)
    # Call create_post function to draw three posts
    create_post()
    #set value for N_entry
    N_entry[1] = Text(Point(420, 70), "N:")
    N_entry[1].draw(win)
    N_entry[2] = Entry(Point(440,70), 1)
    N_entry[2].setText(N_entry[0])
    N_entry[2].draw(win)
    
    return [btn_Quit, btn_Reset,base_line]

'''
Purpose: Reset button click triggers this function to update lable with user inputed value
Parameter: None
Return value: None
''' 
def Hanoi_reset():
    global N_entry, posts
    inputValue = int(N_entry[2].getText())
    while inputValue>9:
        inputValue = int(inputValue%10)
    msg_main.setText("RESET"+'\n'+'N: '+str(inputValue))
    N_entry[0]=inputValue
'''
Purpose: Create three post assign values 
Parameter: None
Return value: None
'''
def create_post():
    global win, posts, post_A, post_B, post_C
    posts = [ ['A', None, None, []], ['B', None, None, []], ['C', None, None, []] ]    
    posts[0][1] = rect_create(win, 120, 120, POST_W, POST_H, "A")
    posts[1][1] = rect_create(win, 120+POST_SP, 120, POST_W, POST_H, "B")
    posts[2][1] = rect_create(win, 120+2*POST_SP, 120, POST_W, POST_H, "C")
    posts[0][1][0].setFill('brown')
    posts[1][1][0].setFill('brown')
    posts[2][1][0].setFill('brown')
    posts[0][2] ='Post: A'
    posts[1][2] ='Post: B'
    posts[2][2] ='Post: C'
    #call reset post function
    reset_posts()
    
'''
Purpose: Clear the disk list in each post
Parameter: None
Return value: None
'''
def reset_posts():
    global posts
    for p in posts:
        p[3]=[]
    show_post_info()
'''
Purpose: Show post infomation
Parameter: None
Return value: None
'''
def show_post_info():
    postA=info_create(win, 130, 310, posts[0][0])
    postB=info_create(win, 130+POST_SP, 310, posts[1][0])
    postC=info_create(win, 130+2*POST_SP, 310, posts[2][0])
    
    diskA=info_create(win, 131, 322, '[]')
    diskB=info_create(win, 131+POST_SP, 322, '[]')
    diskC=info_create(win, 131+2*POST_SP, 322, '[]')
    
    

    