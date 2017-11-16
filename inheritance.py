class Parent():
    def __init__(self, last_name, eye_color):
        print("Parent Constructor Called")
        self.last_name = last_name
        self.eye_colour = eye_color

    def show_info(self):
        print("Last Name - "+self.last_name)
        print("Eye Colour - " + self.eye_colour)

class Child(Parent):
    def __init__(self, last_name, eye_color, number_of_toy):
        print("Child Constructor Called")
        Parent.__init__(self,last_name,eye_color)
        self.number_of_toy = number_of_toy

    def show_info(self):
        print("Last Name - " + self.last_name)
        print("Eye Colour - " + self.eye_colour)
        print("Number of Toys - " + str(self.number_of_toy))

billy_cyrus = Parent("Cyrus", "Blue")
miley_cyrus = Child("Cyrus", "Blue", 5)

# print(miley_cyrus.last_name)
# print(miley_cyrus.number_of_toy)

#billy_cyrus.show_info()
miley_cyrus.show_info()

#Method Overwriting: when there are the similar functions in the class, child will overwrites parents - but it can inherit the function and run