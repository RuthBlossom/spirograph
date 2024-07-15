# Turtle Spirograph Program

This Python program utilizes the Turtle module to create colorful spirograph patterns. Spirographs are complex geometric patterns created by tracing the path of a point as it revolves around a fixed point.

![Uploading spiral.JPG…]()


## Features

- **Colorful Spirographs**: The program generates spirograph patterns with randomly selected colors.
- **Customizable Patterns**: You can adjust the size of the gap between each revolution to create different patterns.
- **Fast Drawing Speed**: The program uses the "fastest" speed setting to draw spirographs quickly.
- **Random Colors**: Colors are randomly selected using RGB values to create visually appealing patterns.

## How It Works

The program uses the Turtle module to create a turtle object (`tim`) that draws the spirograph pattern. Here's how it works:

1. **Turtle Initialization**: The program initializes a Turtle object (`tim`) and sets up the drawing environment.
2. **Color Mode**: It sets the color mode to 255 (RGB) to allow for a wider range of colors.
3. **Random Color Generation**: The `random_color()` function generates random RGB colors for drawing.
4. **Drawing Spirograph**: The `draw_spirograph()` function draws the spirograph pattern by looping through a series of drawing commands.
5. **Drawing Loop**: The program loops through a range of angles, drawing circles and rotating the turtle's heading to create the spirograph pattern.
6. **Main Loop**: The program keeps the Turtle graphics window open until closed by the user.

## Usage

1. Run the program using a Python interpreter.
2. A Turtle graphics window will open, displaying the drawn spirograph pattern.
3. Close the window when you're done viewing the pattern.

## Customization

You can customize the program in the following ways:

- **Gap Size**: Adjust the size of the gap between each revolution by changing the argument passed to the `draw_spirograph()` function.
- **Pen Size**: Modify the pen size used for drawing circles by adjusting the value passed to the `pensize()` method.
- **Colors**: Customize the color selection logic to use specific colors or color palettes.

## Prerequisites

Before running the program, ensure you have Python installed on your system. The Turtle module is included in the standard Python library, so no additional installation is required.

