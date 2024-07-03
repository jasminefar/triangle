import turtle

class SierpinskiTriangleDrawer:
    def __init__(self, initial_length=400, min_length=10, speed=1):
        """
        Initialize the SierpinskiTriangleDrawer with initial parameters.
        
        initial_length: The starting length of the sides of the triangle.
        min_length: The minimum length of a side before stopping recursion.
        speed: The drawing speed of the turtle.
        """
        self.initial_length = initial_length
        self.min_length = min_length
        self.speed = speed
        self.t = turtle.Turtle()
        self.t.speed(speed)
    
    def draw_triangle(self, length):
        """
        Draw an equilateral triangle with the given side length.
        
        length: The length of each side of the triangle.
        """
        for _ in range(3):
            self.t.forward(length)
            self.t.left(120)
    
    def draw_sierpinski(self, length):
        """
        Recursively draw the Sierpinski triangle.
        
        length: The current length of the sides of the triangle.
        """
        if length > self.min_length:
            for _ in range(3):
                self.draw_sierpinski(length / 2)
                self.t.forward(length)
                self.t.left(120)
        else:
            self.draw_triangle(length)
    
    def start_drawing(self):
        """Start the drawing process."""
        turtle.bgcolor("black")
        self.t.color("white")
        self.t.penup()
        self.t.goto(-self.initial_length / 2, -self.initial_length / 2)  # Position the turtle at the starting point
        self.t.pendown()
        self.draw_sierpinski(self.initial_length)
        turtle.done()
    
    def set_colors(self, background_color="black", triangle_color="white"):
        """
        Set the colors for the background and the triangle.
        
        background_color: The color of the background.
        triangle_color: The color of the triangle.
        """
        turtle.bgcolor(background_color)
        self.t.color(triangle_color)

    def start_drawing_with_colors(self, background_color="black", triangle_color="white"):
        """Start the drawing process with custom colors."""
        self.set_colors(background_color, triangle_color)
        self.t.penup()
        self.t.goto(-self.initial_length / 2, -self.initial_length / 2)  # Position the turtle at the starting point
        self.t.pendown()
        self.draw_sierpinski(self.initial_length)
        turtle.done()

# Create an instance of SierpinskiTriangleDrawer with parameters to extend drawing time and start drawing
triangle = SierpinskiTriangleDrawer(initial_length=600, min_length=5, speed=1)
triangle.start_drawing_with_colors(background_color="navy", triangle_color="cyan")
