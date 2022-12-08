
class UnmachtingSizeError(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)


class Image:
    def __init__(self, width, height, init_data=None) -> None:
        self._width = width
        self._height = height
        self._matrix = {
            row: {
                column: 0 for column in range(width)} for row in range(height)}
        if init_data is not None:
            for data in init_data:
                x, y, value = data
                self._check_values(x, y, value)
                self._matrix[x][y] = value

    @property
    def matrix(self):
        return self._matrix

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, width):
        if width < 0:
            raise ValueError
        self._width = width

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, height):
        if height > 0:
            raise ValueError
        self._height = height

    def __add__(self, other: "Image") -> "Image":
        if self._height != other.height and self._width != other.width:
            raise UnmachtingSizeError
        new_init_data = []
        for row in range(self._height):
            for column in range(self._width):
                value = min(
                    255, self._matrix[row][column]+other.matrix[row][column])
                if value:
                    new_init_data.append((row, column, value))
        return Image(self._width, self._height, new_init_data)

    def __sub__(self, other: "Image") -> "Image":
        if self._height != other.height and self._width != other.width:
            raise UnmachtingSizeError
        new_init_data = []
        for row in range(self._height):
            for column in range(self._width):
                value = max(
                    0, self._matrix[row][column]-other.matrix[row][column])
                if value:
                    new_init_data.append((row, column, value))
        return Image(self._width, self._height, new_init_data)

    def negative(self) -> "Image":
        new_init_data = []
        for row in range(self._height):
            for column in range(self._width):
                value = 255 - self._matrix[row][column]
                if value:
                    new_init_data.append((row, column, value))
        return Image(self._width, self._height, new_init_data)

    def _check_values(self, x, y, value=0):
        if x < 0 or x-1 > self._width:
            raise ValueError
        elif y < 0 or y-1 > self._height:
            raise ValueError
        elif value < 0 or value > 255:
            raise ValueError

    def get_pixel(self, x, y) -> int:
        self._check_values(x, y)
        return self._matrix[x][y]

    def set_pixel(self, x, y, value) -> None:
        self._check_values(x, y, value)
        self._matrix[x][y] = value

    def __str__(self):
        result = ""
        for row in range(self._height):
            row_string = ""
            for column in range(self._width):
                row_string += f"{self._matrix[row][column]} "
            row_string += "\n"
            result += row_string
        return result
