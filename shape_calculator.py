class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.n = ""
    def set_width(self, width):
        self.width = width
    def set_height(self, height):
        self.height = height
    def get_area(self):
        area = self.width * self.height
        return area
    def get_perimeter(self):
        perimeter = 2 * (self.width + self.height)
        return perimeter
    def get_diagonal(self):
        diagonal = (self.width ** 2 + self.height ** 2) ** .5
        return diagonal
    def get_picture(self):
        if self.height > 50 or self.width > 50:
            return "Too big for picture."
        picture = ""
        for _ in range(self.height):
            picture += "*" * self.width + "\n"
        return picture
    def get_amount_inside(self, shape):
        if isinstance(shape, Rectangle):
            return self.width // shape.width * self.height // shape.height
        elif isinstance(shape, Square):
            return self.width // shape.width * self.height // shape.height
        else:
            return 0
        
    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"
    

class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)
    
    def set_side(self, side):
        self.width = side
        self.height = side
        
    def __str__(self):
        return f"Square(side={self.width})"
    

