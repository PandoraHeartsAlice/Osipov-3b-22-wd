class Geometric_figure:
    def __init__(self, area, perimeter):
        self.area = area
        self.perimeter = perimeter

    def print_info(self):
        print("area -", self.area, "perimeter -", self.perimeter)


geometric_figure = Geometric_figure(7, 3)
geometric_figure.print_info()
