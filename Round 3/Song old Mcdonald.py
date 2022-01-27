"""
COMP.CS.101 Programming 1
Template Song: Old MacDonald
"""

def print_verse(animal, sound):
    """If we want to do multiple animals, it's easier just to wrap the function call into a loop:"""
    print("Old MACDONALD had a farm")
    print("E-I-E-I-O")
    print("And on his farm he had a %s" % (animal))
    print("E-I-E-I-O")
    print("With a %s %s here" % (sound, sound))
    print("And a %s %s there" % (sound, sound))
    print("Here a %s, there a %s" % (sound, sound))
    print("Everywhere a %s %s" % (sound, sound))
    print("Old MacDonald had a farm")
    print("E-I-E-I-O")

def main():
        animals = ["cow", "pig", "duck", "horse", "lamb"]
        sounds = ["moo", "oink", "quack", "neigh", "baa"]
        for i in range(len(animals)):
            print_verse(animals[i], sounds[i])
            if i < len(animals)-1:
                print()

if __name__ == "__main__":
        main()
