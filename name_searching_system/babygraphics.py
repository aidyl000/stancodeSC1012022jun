"""
File: babygraphics.py
Name: Lydia
--------------------------------
SC101 Baby Names Project
Adapted from Nick Parlante's Baby Names assignment by
Jerry Liao.
"""

import tkinter
import babynames
import babygraphicsgui as gui

FILENAMES = [
    'data/full/baby-1900.txt', 'data/full/baby-1910.txt',
    'data/full/baby-1920.txt', 'data/full/baby-1930.txt',
    'data/full/baby-1940.txt', 'data/full/baby-1950.txt',
    'data/full/baby-1960.txt', 'data/full/baby-1970.txt',
    'data/full/baby-1980.txt', 'data/full/baby-1990.txt',
    'data/full/baby-2000.txt', 'data/full/baby-2010.txt'
]
CANVAS_WIDTH = 1000
CANVAS_HEIGHT = 600
YEARS = [1900, 1910, 1920, 1930, 1940, 1950,
         1960, 1970, 1980, 1990, 2000, 2010]
GRAPH_MARGIN_SIZE = 20
COLORS = ['red', 'purple', 'green', 'blue']
TEXT_DX = 2
LINE_WIDTH = 2
MAX_RANK = 1000


def get_x_coordinate(width, year_index):
    """
    Given the width of the canvas and the index of the current year
    in the YEARS list, returns the x coordinate of the vertical
    line associated with that year.

    Input:
        width (int): The width of the canvas
        year_index (int): The index where the current year is in the YEARS list
    Returns:
        x_coordinate (int): The x coordinate of the vertical line associated
                            with the current year.
    """
    gap = (width - 2 * GRAPH_MARGIN_SIZE) / len(YEARS)  # to get the distance between each vertical line
    x_coordinate = GRAPH_MARGIN_SIZE + year_index * gap  # to get x position at each vertical line
    return x_coordinate


def draw_fixed_lines(canvas):
    """
    Draws the fixed background lines on the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
    """
    canvas.delete('all')            # delete all existing lines from the canvas

    # ----- Write your code below this line ----- #
    canvas.create_line(GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE, CANVAS_WIDTH-GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE)  # draw the top line
    canvas.create_line(GRAPH_MARGIN_SIZE, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE, CANVAS_WIDTH - GRAPH_MARGIN_SIZE, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE)  # draw the bottom line

    for year_index in range(len(YEARS)):
        x_coordinate = get_x_coordinate(CANVAS_WIDTH, year_index)  # to get x position at each vertical line
        canvas.create_line(x_coordinate, 0, x_coordinate, CANVAS_HEIGHT)  # to draw vertical line at each x position
        canvas.create_text(x_coordinate+TEXT_DX, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE, text=YEARS[year_index], anchor=tkinter.NW)


def draw_names(canvas, name_data, lookup_names):
    """
    Given a dict of baby name data and a list of name, plots
    the historical trend of those names onto the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
        name_data (dict): Dictionary holding baby name data
        lookup_names (List[str]): A list of names whose data you want to plot

    Returns:
        This function does not return any value.
    """
    draw_fixed_lines(canvas)        # draw the fixed background grid

    # ----- Write your code below this line ----- #
    gap = (CANVAS_WIDTH - 2 * GRAPH_MARGIN_SIZE) / len(YEARS)  # to get the distance between each vertical line
    # y_proportion = (CANVAS_HEIGHT-GRAPH_MARGIN_SIZE*2)/MAX_RANK
    for i in range(len(lookup_names)):  # to get each name in lookup_names(list)
        name = lookup_names[i]
        for j in range(len(YEARS)):
            x_coordinate = get_x_coordinate(CANVAS_WIDTH, j)  # to get x position at each year
            color = COLORS[i % len(COLORS)]
            if str(YEARS[j]) not in name_data[name]:  # to check if the rank of the name in that year is among top 1000
                canvas.create_text(x_coordinate + TEXT_DX, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE,
                                   text=name+'*', anchor=tkinter.SW, fill=color)
                if j+1 < len(YEARS) and str(YEARS[j+1]) not in name_data[name]:  # to check if next rank is not among top 1000
                    canvas.create_line(x_coordinate, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE, x_coordinate+gap, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE, width=LINE_WIDTH, fill=color)
                else:
                    if j+1 < len(YEARS):  # to check if next rank is among top 1000
                        y2 = transfer_y_position(name_data[name][str(YEARS[j + 1])])
                        canvas.create_line(x_coordinate, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE, x_coordinate+gap, y2, width=LINE_WIDTH, fill=color)
            else:
                y = transfer_y_position(name_data[name][str(YEARS[j])])
                canvas.create_text(x_coordinate + TEXT_DX, y, text=name + '' + name_data[name][str(YEARS[j])], anchor=tkinter.SW, fill=color)
                if j+1 < len(YEARS) and str(YEARS[j+1]) not in name_data[name]:  # to check if next rank is not among top 1000
                    y1 = transfer_y_position(name_data[name][str(YEARS[j])])
                    canvas.create_line(x_coordinate, y1, x_coordinate+gap, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE, width=LINE_WIDTH, fill=color)
                else:
                    if j+1 < len(YEARS):  # to check if next rank is among top 1000
                        y1 = transfer_y_position(name_data[name][str(YEARS[j])])
                        y2 = transfer_y_position(name_data[name][str(YEARS[j + 1])])
                        canvas.create_line(x_coordinate, y1, x_coordinate+gap, y2, width=LINE_WIDTH, fill=color)


def transfer_y_position(rank):  # to get a adjusted y position between top and bottom line
    rank = int(rank)
    return rank*((CANVAS_HEIGHT-2*GRAPH_MARGIN_SIZE)/MAX_RANK)+GRAPH_MARGIN_SIZE


# main() code is provided, feel free to read through it but DO NOT MODIFY
def main():
    # Load data
    name_data = babynames.read_files(FILENAMES)

    # Create the window and the canvas
    top = tkinter.Tk()
    top.wm_title('Baby Names')
    canvas = gui.make_gui(top, CANVAS_WIDTH, CANVAS_HEIGHT, name_data, draw_names, babynames.search_names)

    # Call draw_fixed_lines() once at startup so we have the lines
    # even before the user types anything.
    draw_fixed_lines(canvas)

    # This line starts the graphical loop that is responsible for
    # processing user interactions and plotting data
    top.mainloop()


if __name__ == '__main__':
    main()
