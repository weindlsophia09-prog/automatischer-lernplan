class Grundschule:
    """Grundschule Level - Klassen 1-4"""
    
    def __init__(self):
        self.name = "Grundschule"
        self.klassen = ["1", "2", "3", "4"]
        self.fokus_faecher = ["Mathematik", "Deutsch", "Sachkunde"]
        self.lernziele = {
            "1": {
                "mathematik": ["Zahlen 0-20", "Einfaches Addieren und Subtrahieren"],
                "deutsch": ["Lesen und Schreiben lernen", "Grundwortschatz"],
                "sachkunde": ["Umwelt und Natur kennenlernen", "Grundkonzepte"]
            },
            "2": {
                "mathematik": ["Zahlen 0-100", "Addieren und Subtrahieren", "Einführung Multiplikation"],
                "deutsch": ["Flüssiges Lesen", "Einfache Texte schreiben"],
                "sachkunde": ["Gesellschaft", "Wissenschaftliche Grundlagen"]
            },
            "3": {
                "mathematik": ["Zahlen bis 1000", "Multiplikation und Division", "Bruchrechnung Basics"],
                "deutsch": ["Komplexere Texte", "Satzstruktur"],
                "sachkunde": ["Geschichte und Kultur", "Naturwissenschaften"]
            },
            "4": {
                "mathematik": ["Große Zahlen", "Dezimalzahlen", "Geometrie"],
                "deutsch": ["Aufsätze", "Textverständnis"],
                "sachkunde": ["Vorbereitung auf Sekundarstufe"]
            }
        }
    
    def get_lernziele(self, klasse):
        return self.lernziele.get(klasse, {})
    
    def get_klassen(self):
        return self.klassen
    
    def get_schwierigkeitsgrad(self):
        return ["einfach", "mittel"]