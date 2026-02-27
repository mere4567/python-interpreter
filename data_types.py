# Custom Python Data Types Implementation

class Vector:
    """Class for representing a mathematical vector."""
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def magnitude(self):
        """Calculate the magnitude of the vector."""
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def __add__(self, other):
        """Add two vectors together."""
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        """Subtract one vector from another."""
        return Vector(self.x - other.x, self.y - other.y)

class Matrix:
    """Class for representing a mathematical matrix."""
    def __init__(self, data):
        self.data = data

    def transpose(self):
        """Transpose the matrix."""
        return Matrix([list(row) for row in zip(*self.data)])

    def __add__(self, other):
        """Add two matrices together element-wise."""
        return Matrix([[self.data[i][j] + other.data[i][j] for j in range(len(self.data[0]))] for i in range(len(self.data))])

    def __getitem__(self, index):
        """Get a row from the matrix by index."""
        return self.data[index]
