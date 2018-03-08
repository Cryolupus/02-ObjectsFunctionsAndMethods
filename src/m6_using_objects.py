"""
This module lets you practice  ** using objects **, including:
  -- CONSTRUCTING objects,
  -- applying METHODS to them, and
  -- accessing their DATA via INSTANCE VARIABLES

Authors: David Mutchler, Dave Fisher, Valerie Galluzzi, Amanda Stouder,
         their colleagues and Kevin Chou.
"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.

import rosegraphics as rg


def main():
    """ Calls the other functions to demonstrate and/or test them. """
    # Test your functions by putting calls to them here:
    two_circles()
    circle_and_rectangle()
    lines()


def two_circles():
    """
    -- Constructs an rg.RoseWindow.
    -- Constructs and draws two rg.Circle objects on the window
         such that:
           -- They fit in the window and are easily visible.
           -- They have different radii.
           -- One is filled with some color and one is not filled.
    -- Waits for the user to press the mouse, then closes the window.
    """
    # -------------------------------------------------------------------------
    # DONE: 2. Implement this function, per its doc-string above.
    #    -- ANY two rg.Circle objects that meet the criteria are fine.
    #    -- File  COLORS.txt  lists all legal color-names.
    # Put a statement in   main   to test this function
    #    (by calling this function).
    # -------------------------------------------------------------------------
    window = rg.RoseWindow(400, 300)
    center1 = rg.Point(200, 150)
    center2 = rg.Point(100, 200)
    circle1 = rg.Circle(center1, 20)
    circle2 = rg.Circle(center2, 45)
    circle2.fill_color = 'blue'
    circle1.attach_to(window)
    circle2.attach_to(window)

    window.render()
    window.close_on_mouse_click()


def circle_and_rectangle():
    """
    -- Constructs an rg.RoseWindow.
    -- Constructs and draws a rg.Circle and rg.Rectangle
       on the window such that:
          -- They fit in the window and are easily visible.
          -- The rg.Circle is filled with 'blue'
    -- Prints (on the console, on SEPARATE lines) the following data
         associated with your rg.Circle:
          -- Its outline thickness.
          -- Its fill color.
          -- Its center.
          -- Its center's x coordinate.
          -- Its center's y coordinate.
    -- Prints (on the console, on SEPARATE lines) the same data
         but for your rg.Rectangle.
    -- Waits for the user to press the mouse, then closes the window.

    Here is an example of the output on the console,
    for one particular circle and rectangle:
           1
           blue
           Point(180.0, 115.0)
           180
           115
           1
           None
           Point(75.0, 150.0)
           75.0
           150.0
    """
    window2 = rg.RoseWindow(800, 600)
    center = rg.Point(150, 150)
    circle2 = rg.Circle(center, 50)
    circle2.fill_color = 'blue'
    corner1 = rg.Point(300, 400)
    corner2 = rg.Point(400, 500)
    rectangle = rg.Rectangle(corner1, corner2)
    rectangle.attach_to(window2)
    circle2.attach_to(window2)

    window2.render()
    print(circle2.outline_thickness)
    print(circle2.fill_color)
    print(circle2.center)
    print(center.x)
    print(center.y)
    print(rectangle.outline_thickness)
    print(rectangle.fill_color)
    print(rectangle.get_center())
    rectangle_x = rectangle.get_center().x
    print(rectangle_x)
    rectangle_y = rectangle.get_center().y
    print(rectangle_y)

    window2.close_on_mouse_click()
    # -------------------------------------------------------------------------
    # DONE: 3. Implement this function, per its doc-string above.
    #   -- ANY objects that meet the criteria are fine.
    # Put a statement in   main   to test this function
    #    (by calling this function).
    #
    # IMPORTANT: Use the DOT TRICK to guess the names of the relevant
    #       instance variables for outline thickness, etc.
    # -------------------------------------------------------------------------


def lines():
    window3 = rg.RoseWindow(800, 800)
    start = rg.Point(200, 200)
    end = rg.Point(400, 400)
    line1 = rg.Line(start, end)
    start2 = rg.Point(500, 300)
    end2 = rg.Point(700, 500)
    line2 = rg.Line(start2, end2)
    line2.thickness = 10
    line1.attach_to(window3)
    line2.attach_to(window3)
    window3.render()
    midpoint = line2.get_midpoint()
    midx = line2.get_midpoint().x
    midy = line2.get_midpoint().y
    print(midpoint)
    print(midx)
    print(midy)
    window3.close_on_mouse_click()

    """
    -- Constructs a rg.RoseWindow.
    -- Constructs and draws on the window two rg.Lines such that:
          -- They both fit in the window and are easily visible.
          -- One rg.Line has the default thickness.
          -- The other rg.Line is thicker (i.e., has a bigger width).
    -- Uses a rg.Line method to get the midpoint (center) of the
         thicker rg.Line.
    -- Then prints (on the console, on SEPARATE lines):
         -- the midpoint itself
         -- the x-coordinate of the midpoint
         -- the y-coordinate of the midpoint

       Here is an example of the output on the console, if the two
       endpoints of the thicker line are at (100, 100) and (121, 200):
            Point(110.5, 150.0)
            110.5
            150.0

    -- Waits for the user to press the mouse, then closes the window.
    """
    # -------------------------------------------------------------------------
    # DONE: 4. Implement and test this function.
    # -------------------------------------------------------------------------


# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()
