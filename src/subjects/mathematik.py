class MathematikFragen:
    def __init__(self):
        # Dictionary to hold questions categorized by school level and difficulty
        self.fragen = {
            'grundschule': {
                'einfach': [
                    'Was ist 2 + 2?',
                    'Was ist 5 - 3?'
                ],
                'mittel': [
                    'Was ist 7 + 8?',
                    'Was ist 12 - 5?'
                ],
                'schwer': [
                    'Was ist 15 + 27?',
                    'Was ist 30 - 12?'
                ]
            },
            'realschule': {
                'einfach': [
                    'Was ist 10 * 2?',
                    'Was ist 56 / 7?'
                ],
                'mittel': [
                    'Was ist 14 * 6?',
                    'Was ist 81 / 9?'
                ],
                'schwer': [
                    'Was ist 25 * 25?',
                    'Was ist die Quadratwurzel von 144?'
                ]
            },
            'gymnasium': {
                'einfach': [
                    'Was ist 2^3?',
                    'Was ist der Wert von pi?'
                ],
                'mittel': [
                    'Was ist die Ableitung von x^2?',
                    'Was ist das Integral von 1/x?'
                ],
                'schwer': [
                    'Was ist die Lösung der Gleichung x^2 - 4 = 0?',
                    'Was ist die Differentialgleichung von e^x?'
                ]
            }
        }

    def get_fragen(self, level, difficulty):
        return self.fragen.get(level, {}).get(difficulty, [])

# Example usage:
if __name__ == '__main__':
    fragen = MathematikFragen()
    print(fragen.get_fragen('grundschule', 'einfach'))
    print(fragen.get_fragen('realschule', 'mittel'))
    print(fragen.get_fragen('gymnasium', 'schwer'))