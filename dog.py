"""
This is an example demonstrating the differences between a class and its instances.
"""


class Dog:
    """
    This is a dog!

    See all the references to self? All of an object's methods have 'self' as the first argument. This is referring
    to the object itself, and by referencing self, you can access the attributes and methods of the object itself.

    E.g. self.name refers to the name of this dog specifically, rather than any other dog, or a variable called name
    that's somewhere else in your code.
    """
    # This is a characteristic that is the same for all Dogs.
    species = "Canis familiaris"

    def __init__(self, name, age, weight, height):
        # These characteristics can be different for each dog.
        # If I were a less terrible person, I would be more specific with these variable names, e.g.
        # by including the expected units that the variable should hold.
        self.name = name
        self.age = age
        self.weight = weight
        self.height = height

    # This is a series of things that all dogs can do. So, they are added into the definition of the Dog class.
    def move(self, distance_meters):
        time_to_move = distance_meters * self.height / self.weight * (self.age / 10)
        return time_to_move

    def bark(self):
        volume = (self.weight / 30) * (self.age / 10)
        # This is a series of conditions--when you have a block like this, with if... elif... else, the code will
        # evaluate each of the conditions until it finds one that passes. When that happens, it skips to the line after
        # the end of the else block.
        # So in this case, if volume > 25, then the code will skip to the bit after the else: statement, where it
        # returns the sound_text that it found.
        if volume > 25:
            sound_text = 'BARK!'
        elif volume > 15:
            sound_text = 'Bark!'
        else:
            sound_text = 'bark'
        return sound_text

    def bite(self):
        # Now, compare that to this situation. In this situation, this isn't an if... else block. So, each if statement
        # will get evaluated (and if they evaluate to True, the stuff inside the if block will be run).
        if self.weight > 150:
            print('OM NOM NOM')
        if self.weight > 200:
            print('NOM NOM')

    def wag_tail(self):
        print("Swish swish")
        return self.name

if __name__ == '__main__':  # This is explained in main.py, won't repeat it here.
    special_dog = Dog('Derpy', 7, 100, 12)
    how_long_to_move = special_dog.move(10)
    print(how_long_to_move)
    special_dog.bark()
    special_dog.bite()
    dog_name = special_dog.wag_tail()
    print(dog_name)

