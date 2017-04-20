#!/usr/bin/python


#Define functions to count observations and max value from the data
def count_observations(file_path): 
    """
    By define function count_observations we can calculate observations from the input file 
    In the data file one name plus two numbers can be treated as one observation.
    """
    num_observations = len(open(file_path).readlines())/3
    return num_observations


#Define functions to get the maximum value of features from the data
def get_max_value(feature):
    """ 
    A feature is defined as the list of string and numbers from the file input
    feature 1 is the first group of data for all the observations, feature 2 is the second group of data for all observations
    This function can be used to find the maximum number in the data group.
    """
    max_value = feature[0]
    i = 1
    while i < len(feature):
        if int(feature[i]) > int(max_value):
            max_value = feature[i]
        i = i + 1       
    return max_value  


#draw y-axis and ticks
def draw_y_axis(alex, yaxis_max):
    """
    The function draw_y_axis is created to draw y-axis of the histogram, by giving inputs of turtle object name and the maximun value on Y-axis for all groups of data 
    """
    i_y = 1
    alex.left(90)
    while i_y <= 10:
        alex.forward(ytick)
        yv1=float(int(yaxis_max) / 10 * i_y)
        yv = '%.1f' % yv1
        alex.write(yv, move=False, align="right", font=("Arial", 8, "normal"))
        alex.left(90)
        alex.forward(10)
        alex.right(180)
        alex.forward(10)
        alex.left(90)
        i_y = i_y + 1
    alex.right(180)
    alex.forward(10 * ytick)
    alex.left(90)
    return


#draw x-axis and lables
def draw_x_axis(alex, feature_3):
    """
    This function is created to draw x-axis and lables for the histogram. parameters include turtle object, and the list of data that contain information for x-axis observation names.
    """
    i_x = 0
    while i_x <= observation_number and i_x <= len(feature_3)-1:
        if i_x == 0:
            alex.forward(20 + 0.5 * WIDTH_BAR)
        else:
            alex.forward(20 + WIDTH_BAR)
        alex.up()
        alex.right(90)
        alex.forward(30)
        alex.left(90)
        alex.pendown()
        alex.write(feature_3[i_x], move=False, align="center", font=("Arial", 8, "normal"))
        alex.up()
        alex.left(90)
        alex.forward(30)
        alex.right(90)
        alex.pendown()
        i_x=i_x + 1
    alex.forward(20 + WIDTH_BAR)
    return


def draw_rectangle(alex, height, i, color_style):
    """
    The draw_rectangle can be used to draw a rectangle on the screen
    The inputs value included turtle object, height, index, color, and we can get output as a rectangle according to these values.
    """
    #alex.forward(20)
    alex.fillcolor(color_select(color_style, i))
    alex.begin_fill()
    alex.left(90)
    alex.forward(height)
    alex.right(90)
    alex.forward(WIDTH_BAR)
    alex.right(90)
    alex.forward(height)
    alex.left(90)
    alex.end_fill()
    return


def draw_bars(alex, file_path, feature, color_style):
    """
    This function is created to draw histogram bars  
    Value inputs include turtle object alex, data file name, feature type, as well as color.
    """
    alex.penup()
    alex.left(180)
    alex.forward(observation_number*(20+WIDTH_BAR)+20+0.5*WIDTH_BAR)
    alex.right(180)
    alex.pendown()
    i = 0
    while i <= observation_number and i < len(feature):
        height = feature[i]
        alex.forward(20)
        draw_rectangle(alex, int(height) * int(((HEIGHT_WINDOW - 2 * BORDER_WINDOW)/ int(yaxis_max))), i, color_style)
        i=i+1
    alex.forward(20+0.5*WIDTH_BAR)


def color_select(color_style, index):
    """
    This function is used for choosing color, if we input value of the index and color style choice
    We will get color filling results. 2 color styles are provided, i.e. color_1 and color_2, for each groups of color there are 6 colors in the list.
    """
    color_1 = ['#B22222','#FF4500','#FFD700','#32CD32','#4682B4','#9400D3']
    color_2 = ['#F08080','#FFDEAD','#EE82EE','#90EE90','#87CEEB','#808080']
    if color_style == 'color_1':
        color = color_1[index % 6]
    else:
        color = color_2[index % 6]
    return color


def main():
    """
    Call turtle to draw a histogram from data from txt file input, which will call functions to setup turtle, draw y axis, x axis, and bars.
    All the functions above are aggregated here to draw the chart. the variables have been defined and explained in all sub-functions.
    """
    alex= turtle.Turtle()
    wn = turtle.Screen()
    wn.screensize(WIDTH_WINDOW,HEIGHT_WINDOW)
    wn.title(chart_title) #give it the inputed title
    alex.speed(6) #turtle speed setup
    alex.up()
    alex.setpos(-(WIDTH_WINDOW / 2) + 100, -255)
    alex.pendown()
    draw_y_axis(alex, yaxis_max)
    draw_x_axis(alex, feature_3)
    colorstyle = input("what color do you want? color_1 or color_2? ")
    draw_bars(alex, file_path, feature_1, colorstyle)
    wn.mainloop()	


if __name__ == "__main__":
    #Prompt for imput
    import turtle
    file_path = input('Please enter the path to the file: ').strip()
    chart_title = input('Please create a title for the chart: ')
    file = open(file_path)
    data = file.readlines()
    data_list = [item.replace('\n', '') for item in data] #transform data input into a list
    feature_1 = data_list[1::3] # every 3rd items are added to a new list feature_1, start from the 2nd item.
    feature_2 = data_list[2::3] # every 3rd items are added to a new list feature_2, start from the 3nd item.
    feature_3 = data_list[::3]  # every 3rd items are added to a new list feature_3, start from the 1nd item.
    HEIGHT_WINDOW = 500 #global constant
    WIDTH_WINDOW = 900  #global constant
    BORDER_WINDOW = 30  #global constant
    observation_number = int(count_observations(file_path)) # Number of groups of data
    yaxis_max = get_max_value(feature_1) # maximun number in feature_1 list i.e. max number on y-axis
    ytick = (HEIGHT_WINDOW - 2*BORDER_WINDOW)/ 10 # y axis tick distance
    WIDTH_BAR = int((WIDTH_WINDOW /2 - 2 * BORDER_WINDOW) / observation_number - 5) # bar width 
    main()






