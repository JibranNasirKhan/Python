# multiple inheritance : A class can inherit properties, attributes & methods from multiple classes
# Method resolution Order (MRO): Search is done first in current class, then the search is done in parent classes in depth,
# left-right fashion without searching the same class twice

class Movecharacter:
    def moveforward(self):
        print("Move 1 step forward")

    def movebackward(self):
        print("Move 1 step backward")

class Jumpcharacter:
    def jump_1_level(self):
        print("Jump 1 step")

    def jump_2_level(self):
        print("Jump 2 steps")

class Pokemon(Movecharacter, Jumpcharacter):
     pass

p = Pokemon()
p.moveforward()
p.movebackward()


class mickey(Movecharacter, Jumpcharacter):
    def Jump_3_level(self):
        print("Mickey Jump's 3 level")

m = mickey()
m.jump_1_level()
m.jump_2_level()
m.Jump_3_level()
print(mickey.mro())