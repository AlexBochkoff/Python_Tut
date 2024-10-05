# from turtle import Turtle, Screen
#
# leo = Turtle() # Creating a new object from the class blueprint.
# print(leo)
# leo.shape("turtle")
# leo.color("cadetblue")
# leo.forward(100)
#
# my_screen = Screen() # An Object of the Class <<< when we create an object an instance of a screen appeared.
# print(my_screen.canvheight) # Object.Attribute
#
# my_screen.exitonclick() #when this method is called, the screen will be visible and it will be hidden after a click on it.


from prettytable import PrettyTable
table = PrettyTable()
table.add_column("Pokemon name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])

table.align = "l"

print(table)