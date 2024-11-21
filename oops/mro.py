class Singer:
    def passion(self):
        print("Sing!")

class Painter:
    def passion(self):
        print("Paint")        

class Artist(Singer,Painter):
    pass

a =Artist()
a.passion()
print(Artist.mro())