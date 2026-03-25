from collections.abc import Iterable, Iterator


def add_matter_4(cls):
    original_init = cls.__init__

    def new_init(self, nom: str, note1: float, note2: float, note3: float, note4: float = 0):
        original_init(self, nom, note1, note2, note3)
        self.notes.append(note4)

    cls.__init__ = new_init
    return cls


@add_matter_4
class Student:
    def __init__(self, nom: str, note1: float, note2: float, note3: float):
        self.nom = nom
        self.notes = [note1, note2, note3]

    def moyenne(self) -> float:
        return sum(self.notes) / len(self.notes)


class Matter1Iterator(Iterator):
    def __init__(self, etudiants):
        self._sorted = sorted(etudiants, key=lambda s: s.notes[0], reverse=True)
        self._index = 0

    def __next__(self):
        if self._index >= len(self._sorted):
            raise StopIteration
        student = self._sorted[self._index]
        self._index += 1
        return student


class Matter2Iterator(Iterator):
    def __init__(self, etudiants):
        self._sorted = sorted(etudiants, key=lambda s: s.notes[1], reverse=True)
        self._index = 0

    def __next__(self):
        if self._index >= len(self._sorted):
            raise StopIteration
        student = self._sorted[self._index]
        self._index += 1
        return student


class Matter3Iterator(Iterator):
    def __init__(self, etudiants):
        self._sorted = sorted(etudiants, key=lambda s: s.notes[2], reverse=True)
        self._index = 0

    def __next__(self):
        if self._index >= len(self._sorted):
            raise StopIteration
        student = self._sorted[self._index]
        self._index += 1
        return student


class Matter4Iterator(Iterator):
    def __init__(self, etudiants):
        self._sorted = sorted(etudiants, key=lambda s: s.notes[3], reverse=True)
        self._index = 0

    def __next__(self):
        if self._index >= len(self._sorted):
            raise StopIteration
        student = self._sorted[self._index]
        self._index += 1
        return student


class SchoolClass(Iterable):
    def __init__(self):
        self.etudiants = []

    def add_student(self, student: Student):
        self.etudiants.append(student)

    def __iter__(self):
        return Matter1Iterator(self.etudiants)

    def rank_matter_1(self):
        return sorted(self.etudiants, key=lambda s: s.notes[0], reverse=True)

    def rank_matter_2(self):
        return sorted(self.etudiants, key=lambda s: s.notes[1], reverse=True)

    def rank_matter_3(self):
        return sorted(self.etudiants, key=lambda s: s.notes[2], reverse=True)


school_class = SchoolClass()
school_class.add_student(Student('J', 10, 12, 13, 15))
school_class.add_student(Student('A', 8, 2, 17, 11))
school_class.add_student(Student('V', 9, 14, 14, 7))

for s in school_class.rank_matter_1():
    print(f"{s.nom} : {s.notes[0]}")

for s in school_class.rank_matter_2():
    print(f"{s.nom} : {s.notes[1]}")

for s in school_class.rank_matter_3():
    print(f"{s.nom} : {s.notes[2]}")

for s in school_class:
    print(f"{s.nom} : {s.notes[0]}")

for s in Matter2Iterator(school_class.etudiants):
    print(f"{s.nom} : {s.notes[1]}")

for s in Matter3Iterator(school_class.etudiants):
    print(f"{s.nom} : {s.notes[2]}")

for s in Matter4Iterator(school_class.etudiants):
    print(f"{s.nom} : {s.notes[3]}")
