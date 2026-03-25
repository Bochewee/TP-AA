class Note:
    def __init__(self, matiere: str, valeur: float):
        self.matiere = matiere
        self.valeur = valeur


class Etudiant:
    def __init__(self, nom: str, notes: list[Note]):
        self.nom = nom
        self.notes = notes

    def moyenne(self) -> float:
        return sum(note.valeur for note in self.notes) / len(self.notes)


class Classe:
    def __init__(self, etudiants: list[Etudiant]):
        self.etudiants = etudiants
