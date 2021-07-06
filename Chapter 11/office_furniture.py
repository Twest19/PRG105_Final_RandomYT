"""
    Classes for 11.1 Inheritance Practice PRG 105
"""


class OfficeFurniture:

    def __init__(self, type_of_furniture, material, length, width, height, price):
        self.__type = type_of_furniture
        self.__material = material
        self.__length = length
        self.__width = width
        self.__height = height
        self.__price = price

    def set_type(self, type_of_furniture):
        self.__type = type_of_furniture

    def set_material(self, material):
        self.__material = material

    def set_length(self, length):
        self.__length = length

    def set_width(self, width):
        self.__width = width

    def set_height(self, height):
        self.__height = height

    def set_price(self, price):
        self.__price = price

    def get_type(self):
        return self.__type

    def get_material(self):
        return self.__material

    def get_length(self):
        return self.__length

    def get_width(self):
        return self.__width

    def get_height(self):
        return self.__height

    def get_price(self):
        return self.__price

    def get_dimensions(self):
        dimension = self.__length, ' L x ', self.__width, ' W x ', self.__height, ' H'
        return "".join(dimension)

    def __str__(self):
        info = f"Type: {self.__type}\nPrice: ${int(self.__price):,.2f}\nMaterial: {self.__material}\n" \
               f"Dimension: {self.__length} L x {self.__width} W x {self.__height} H\n"
        return info


class Desk(OfficeFurniture):
    def __init__(self, type_of_furniture, material, length, width, height, price,
                 location_of_drawers, number_of_drawers):
        OfficeFurniture.__init__(self, type_of_furniture, material, length, width, height, price)
        self.__location_of_drawers = location_of_drawers
        self.__number_of_drawers = number_of_drawers

    def set_location_of_drawers(self, location_of_drawers):
        self.__location_of_drawers = location_of_drawers

    def set_number_of_drawers(self, number_of_drawers):
        self.__number_of_drawers = number_of_drawers

    def get_location_of_drawers(self):
        return self.__location_of_drawers

    def get_number_of_drawers(self):
        return self.__number_of_drawers

    def __str__(self):
        desk_info = f"Type: {self.get_type()}\nPrice: ${int(self.get_price()):,.2f}\n" \
                    f"Material: {self.get_material()}\n" \
                    f"Dimension: {self.get_length()} L x {self.get_width()} W x {self.get_height()} H\n" \
                    f"Drawers: {self.__number_of_drawers} drawers\n" \
                    f"Location on Desk: {self.__location_of_drawers} side(s)\n"
        return desk_info
