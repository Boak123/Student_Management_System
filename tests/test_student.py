import unittest
from models.student import Student


class TestStudent(unittest.TestCase):

    def setUp(self):
        self.student = Student(
            "Boluwatife",
            "Ilorin",
            "08012345678",
            "ST001",
            "Cybersecurity",
            "100L",
            85
        )

    def test_student_name(self):
        self.assertEqual(
            self.student.name,
            "Boluwatife"
        )

    def test_student_score(self):
        self.assertEqual(
            self.student.get_score(),
            85
        )

    def test_student_grade(self):
        self.assertEqual(
            self.student.calculate_grade(),
            "A"
        )

    def test_invalid_score(self):
        with self.assertRaises(ValueError):
            self.student.set_score(150)


if __name__ == "__main__":
    unittest.main()