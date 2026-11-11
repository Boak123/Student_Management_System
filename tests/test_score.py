import unittest


class TestStudent(unittest.TestCase):

    def setUp(self):
        self.name = "Boluwatife"
        self.score = 85

    def test_student_name(self):
        self.assertEqual(self.name, "Boluwatife")

    def test_student_score(self):
        self.assertEqual(self.score, 85)

    def tearDown(self):
        print("Test completed.")

if __name__ == "__main__":
    unittest.main()