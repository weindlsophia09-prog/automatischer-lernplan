class Lesson:
    def __init__(self, title, description, duration):
        self.title = title
        self.description = description
        self.duration = duration

    def __str__(self):
        return f"{self.title} ({self.duration} min): {self.description}"

class LessonManager:
    def __init__(self):
        self.lessons = []

    def add_lesson(self, lesson):
        self.lessons.append(lesson)

    def remove_lesson(self, title):
        self.lessons = [lesson for lesson in self.lessons if lesson.title != title]

    def get_lessons(self):
        return self.lessons

    def find_lesson(self, title):
        for lesson in self.lessons:
            if lesson.title == title:
                return lesson
        return None

# Example usage:
if __name__ == '__main__':
    manager = LessonManager()
    lesson1 = Lesson("Math", "Algebra and Geometry", 60)
    lesson2 = Lesson("English", "Grammar and Writing", 45)
    manager.add_lesson(lesson1)
    manager.add_lesson(lesson2)
    for lesson in manager.get_lessons():
        print(lesson)