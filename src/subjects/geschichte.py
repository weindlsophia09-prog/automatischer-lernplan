class GeschichteFragen:
    # Fragen für Grundschule
    grundschule_fragen = {
        'einfach': [
            "Was ist das Datum, an dem der Zweite Weltkrieg begann?",  
            "Wer war der erste Kaiser des Heiligen Römischen Reiches?"
        ],
        'mittel': [
            "Was waren die Ursachen der Französischen Revolution?",  
            "Nenne zwei wichtige Personen aus dem Mittelalter."
        ],
        'schwer': [
            "Erkläre die Auswirkungen des Zweiten Weltkriegs auf Deutschland.",  
            "Wie kam es zum Fall der Berliner Mauer?"
        ]
    }

    # Fragen für Realschule
    realschule_fragen = {
        'einfach': [
            "Was war die Bismarckzeit?",  
            "Nenne eine wichtige Erfindung im 19. Jahrhundert."
        ],
        'mittel': [
            "Was waren die Hauptursachen des Ersten Weltkriegs?",  
            "Erläutere den Begriff 'Nationalsozialismus'."
        ],
        'schwer': [
            "Wie war die Weimarer Republik aufgebaut?",  
            "Diskutiere die Rolle der Frauen im Weltkrieg."
        ]
    }

    # Fragen für Gymnasium
    gymnasium_fragen = {
        'einfach': [
            "Wer war Napoleon?",  
            "Was beschreibt das Konzept der Aufklärung?"
        ],
        'mittel': [
            "Vergleiche die Französische Revolution mit der Amerikanischen Revolution.",  
            "Was waren die Ziele der Aufklärung?"
        ],
        'schwer': [
            "Analysiere die politischen und gesellschaftlichen Veränderungen nach dem Zweiten Weltkrieg in Deutschland.",  
            "Erörtere die Bedeutung des Mittelalters für die europäische Geschichte."
        ]
    }

    def get_fragen(self, level, difficulty):
        if level == 'grundschule':
            return self.grundschule_fragen[difficulty]
        elif level == 'realschule':
            return self.realschule_fragen[difficulty]
        elif level == 'gymnasium':
            return self.gymnasium_fragen[difficulty]
        else:
            return []
