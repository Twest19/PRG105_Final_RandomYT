"""
    In the first step, you will create a parent class. Create a parent class for Office Furniture.
    Set the class variables to be a category (desk, chair, filing cabinet would be examples), material, length, width,
    height, and price. Include a method that returns a string about the object. Implement the __str__ method
    (refer to section 10.2 in your book for details).
"""
import office_furniture


def main():

    my_furniture = office_furniture.OfficeFurniture('desk', 'wood', '36 inch', '28 inch', '40 inch', '200')

    print(f"Furniture type: {my_furniture.get_type()}")
    print(f"Price: ${int(my_furniture.get_price()):,.2f}")
    print(f"Material: {my_furniture.get_material()}")
    print(f"Dimensions: {my_furniture.get_dimensions()}")


main()
