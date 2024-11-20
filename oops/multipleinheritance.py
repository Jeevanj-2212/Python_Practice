# possible to nherit from 2 or more classes 
class Singer:
    def sing(self):
        print("Sing a song")
class Painter:
    def paint(self):
        print("Paint a picture")
class Artist(Singer,Painter):
    pass
a = Artist()
a.sing()
a.paint()
