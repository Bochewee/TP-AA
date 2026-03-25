class Student:
    def __init__(self, nom: str, note1: float, note2: float, note3: float):
        self.nom = nom
        self.notes = [note1, note2, note3]

    def moyenne(self) -> float:
        return sum(self.notes) / len(self.notes)


class SchoolClass:
    def __init__(self):
        self.etudiants = []

    def add_student(self, student: Student):
        self.etudiants.append(student)

    def rank_matter_1(self):
        return sorted(self.etudiants, key=lambda s: s.notes[0], reverse=True)

    def rank_matter_2(self):
        return sorted(self.etudiants, key=lambda s: s.notes[1], reverse=True)

    def rank_matter_3(self):
        return sorted(self.etudiants, key=lambda s: s.notes[2], reverse=True)


school_class = SchoolClass()
school_class.add_student(Student('J', 10, 12, 13))
school_class.add_student(Student('A', 8, 2, 17))
school_class.add_student(Student('V', 9, 14, 14))

for s in school_class.rank_matter_1():
    print(f"{s.nom} : {s.notes[0]}")

for s in school_class.rank_matter_2():
    print(f"{s.nom} : {s.notes[1]}")

for s in school_class.rank_matter_3():
    print(f"{s.nom} : {s.notes[2]}")
