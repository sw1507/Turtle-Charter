# Define functions to count observations and max value from the data
def count_observations(filename):
    """
    By define function count_observations we can calculate observations from the input file 
    In the data file one name plus two numbers can be treated as one observation.
    """
    file = open(filename)
    count = 0
    for line in file:
        count = count + 1
    return(count / 3)

# Define functions to get the maximum value of features from the data
def get_max_value(filename, feature):
    """ 
    feature is a list of string and numbers (from the file input)
    feature 1 is the first group of data for all the observations, feature 2 is the second group of data for all observations
    By using this function we can get the maximum number in the data group.
    """
    file = open(filename)
    list_data = file.readlines()
    for i,line in enumerate(list_data):
        list_data[i] = line.strip()
    n = feature 
    maximum = list_data[n] 
    next_num = 0 
    list_len = int(len(list_data)/3) # list length
    for i in range(0, list_len): 
        next_num = list_data[n + 3*i]
        if int(next_num) > int(maximum):
            maximum = next_num
        
    return(maximum)


# draw axis using turtle
def draw_axes(alex, screen, w, h, border):
    """
    we define the function draw_axes to setup some basics and to draw axes.
    alex is the name of the turtle that I created, sceen is the 
    Input alex(turtle object), screen refers to the window that alex is drawing on, w = window width, h = window height and border is the border width.
    """
    screen.setworldcoordinates(-border, -border, w/2-border, h/2-border)
    screen.title(input("title for the chart:"))
    alex.speed(1)
    alex.penup()
    alex.goto(0, 0)
    alex.pendown()  
    alex.goto(0, h/2-2*border)
    alex.penup()
    alex.goto(0, 0)
    alex.pendown()  
    alex.goto(w/2-2*border, 0)
    alex.penup()  
    alex.goto(0, 0)
    alex.pendown()

def draw_y_tick_mark(alex, max_height):
    """
    The function draw_y_tick_mark here is used to draw tick marks on Y-axis.
    The value inputs include the turtle object, alex as well as the max_height. We assume that max_height/10 = 1 tick mark
    """
    print(C_BORDER)
    tickdistance = (C_HEIGHT / 2 - 2*C_BORDER)/ 10 
    alex.write(0, False, align = "right",font =("Arial",10,"normal"))
    
    for i in range(10):
        alex.forward(5) 
        alex.left(180)  
        alex.forward(5)
        alex.left(-90)  
        alex.forward(tickdistance)
        alex.write(round((max_height) / 10 * (i+1),1), False, align = "right",font =("Arial",10,"normal"))
        alex.left(-90)
 
def draw_rectangle(alex, height, i, color_plan):
    """
    The draw_rectangle can be used to draw a rectangle on the screen
    The inputs value included turtle object, height, index, color, and we can get output as a 
    rectangle according to these values.
    """
    alex.forward(5)
    alex.fillcolor(choose_color(color_plan, i))
    alex.begin_fill()
    alex.left(90)  
    alex.forward(height)  
    alex.left(-90)  
    alex.forward(BAR_WIDTH) 
    alex.left(-90)
    alex.forward(height) 
    alex.left(90)
    alex.end_fill()

def write_x_label(alex,label):
    """ 
    This function is defined to draw labels on x-axis.
    we input the data of object turtle and the lable
    we will get results as the turtle draw labels on x-axis
    """
    alex.penup()
    alex.left(-90)
    alex.forward(8)
    alex.write(label, False, align = "right",font =("Arial",10,"normal"))   
    alex.left(180)
    alex.forward(8)
    alex.left(-90)
    alex.pendown()
    
def draw_bars(alex, filename, feature, color_plan):
    """
    We create this function to draw histogram bars  
    We need to give value of turtle object alex, data file name, feature type, as well as color.
    """
    file = open(filename)
    list_d = file.readlines()
    for i,line in enumerate(list_d):
        list_d[i] = line.strip()
    list_l = NUM_BARS  #int(len(list_d)/3)
    n = feature # get the first value of feature n
    alex.penup()
    alex.goto(0,0)
    alex.pendown()
    for i in range(0, list_l):
        height = int(list_d[i*3 + 1])
        draw_rectangle(alex, height * ((C_HEIGHT / 2 - 2 * C_BORDER)/ M_HEIGHT) , i, color_plan)
        label = list_d[i*3 + 0]
        write_x_label(alex,label)

def choose_color(color_plan, index):
    """
    This function is used for choosing color, we input value of the index and color plan
    We will get color results.
    """
    dark = ['#e41a1c','#377eb8','#4daf4a','#984ea3','#ff7f00']
    light = ['#fbb4ae','#b3cde3','#ccebc5','#decbe4','#fed9a6']
    if color_plan == 'dark':
        color = dark[index % 5]
    else:
        color = light[index % 5]
    return(color)
  
def main():
    """Main function, steps include: 1) set up turtle screen and turtle object; 2)draw axes; 3)draw y axis ticks; 4)select color plan (prompt); 5)draw bar charts
    """
    turtle.setup(C_WIDTH,C_HEIGHT)
    alex= turtle.Turtle()
    wn = turtle.Screen()
    draw_axes(alex, wn, C_WIDTH, C_HEIGHT, C_BORDER)
    draw_y_tick_mark(alex, M_HEIGHT)
    colorplan = input("choose color theme: dark or light?")
    draw_bars(alex, filename, 1, colorplan)
    wn.mainloop()

if __name__ == "__main__":
    
    filename = input("open file (path):")
    import turtle
    C_WIDTH = 800 #global constant
    C_HEIGHT = 500 #global constant
    C_BORDER = 20 #global constant
    NUM_BARS = int(count_observations(filename))
    M_HEIGHT = int(get_max_value(filename,1))
    BAR_WIDTH = int((C_WIDTH /2 - 2 * C_BORDER) / NUM_BARS - 5)
    main()
    
    
    

