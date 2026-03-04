class Realschule:
    """
    This class represents the Realschule education level in Germany.
    It defines the learning goals for classes 5 to 10.
    """

    def __init__(self):
        self.goals = {
            5: "Introduction to basic subjects including German, Math, and English.",
            6: "In-depth exploration of subjects with a focus on practical applications.",
            7: "Development of critical thinking skills and subject-specific knowledge.",
            8: "Preparation for the Realschulabschluss with project work and exams.",
            9: "Emphasis on foreign languages and advanced math topics.",
            10: "Focus on preparing for vocational training or further education options."
        }

    def get_goals(self, class_number):
        """
        Returns the learning goals for the specified class.
        """
        return self.goals.get(class_number, "No goals defined for this class.")
