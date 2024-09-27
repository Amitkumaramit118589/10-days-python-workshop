class color:
    def __init__(self, blue, red, yellow, pink):
        self.brand = "camel"
        self.type = "water_color"
        self.quantity = 10

    def accelerate(self):
        print("which color you want:", self.quantity)

Color = color("blue", "red", "yellow", "pink")
