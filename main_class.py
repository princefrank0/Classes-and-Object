
class student():
    def __init__(self, name: str, age: int, tracks: str, score: float):
        self.name = name
        self.age = age
        self.tracks = tracks
        self.score = score
        print('Name:', name)
        print('Age:', age)
        print('Tracks:', tracks)
        print('Score:', score)

        

    def change_name(self):
        self.name = str (input('Enter New Name: '))
        print('Your New Details Are')
        print("Name:", self.name)
        print('Age:', self.age)
        print('Tracks:', self.tracks)
        print('Score:', self.score)

    def change_age(self):
        self.age = int (input('Enter New Age: '))
        print('Your New Details Are')
        print("Name:", self.name)
        print('Age:', self.age)
        print('Tracks:', self.tracks)
        print('Score:', self.score)

    def add_track(self):
        new_track = self.tracks.append(input('Enter new track: '))
        print('Your New Details Are')
        print("Name:", self.name)
        print('Age:', self.age)
        print('Tracks:', self.tracks)
        print('Score:', self.score)

    def get_score(self):
        print("The Student's Score is", self.score )
        

Bob = student(name="Bob", age=26, tracks=["FE","BE"],score=20.90)
Bob.change_name()
