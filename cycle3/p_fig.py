from Graphics import circle
from Graphics import rectangle
from Graphics.graphics_3D import sphere,cuboid
circle_radius=int(input("\nEnter the radius of the circle: "));
print("Area of the circle is:",circle.area(circle_radius))
print("Perimeter of the circle is:",circle.perimeter(circle_radius))
rect_length=int(input("Enter the length of the Rectangle:"))
rect_breadth=int(input("Enter the breadth of the Rectangle:"))
print("Area of the Rectangle is:",rectangle.area(rect_length,rect_breadth))
print("Perimeter of the Rectangle is:",rectangle.perimeter(rect_length,rect_breadth))
cuboid_width=int(input("Enter the width of the cuboid:"))
cuboid_height=int(input("Enter the height of the cuboid:"))
cuboid_length=int(input("Enter the length of the cuboid:"))
print("Area of the cuboid",cuboid.area(cuboid_width,cuboid_height,cuboid_length))
print("Perimeter of the cuboid",cuboid.perimeter(cuboid_width,cuboid_height,cuboid_length))
sphere_radius=int(input("Enter the radius of the sphere:"))
print("Area of the sphere is:",sphere.area(sphere_radius))
print("Perimeter of the sphere is:",sphere.perimeter(sphere_radius))

