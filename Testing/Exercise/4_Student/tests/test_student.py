from unittest import TestCase, main
from project.student import Student



class TestStudent(TestCase):
    def setUp(self):
        self.student = Student("Test Student")

    def test_init_properties(self):
        self.assertEqual(self.student.name, "Test Student")
        self.assertEqual(self.student.courses, {})

    def test_enroll_new_course_with_default_notes(self):
        result = self.student.enroll("Math", ["Note 1"])
        self.assertEqual(result, "Course and course notes have been added.")
        self.assertEqual(self.student.courses["Math"], ["Note 1"])

    def test_enroll_new_course_with_notes_explicit_Y(self):
        result = self.student.enroll("Physics", ["Formula 1"], "Y")
        self.assertEqual(result, "Course and course notes have been added.")
        self.assertEqual(self.student.courses["Physics"], ["Formula 1"])

    def test_enroll_new_course_without_notes(self):
        result = self.student.enroll("Chemistry", ["Reaction 1"], "N")
        self.assertEqual(result, "Course has been added.")
        self.assertEqual(self.student.courses["Chemistry"], [])

    def test_enroll_existing_course_updates_notes(self):
        self.student.enroll("Math", ["Note 1"])
        result = self.student.enroll("Math", ["Note 2"])
        self.assertEqual(result, "Course already added. Notes have been updated.")
        self.assertEqual(self.student.courses["Math"], ["Note 1", "Note 2"])

    def test_add_notes_to_existing_course(self):
        self.student.enroll("Math", [])
        result = self.student.add_notes("Math", "New note")
        self.assertEqual(result, "Notes have been updated")
        self.assertEqual(self.student.courses["Math"], ["New note"])

    def test_add_notes_to_nonexistent_course_raises_error(self):
        with self.assertRaises(Exception) as context:
            self.student.add_notes("Non-existent", "Note")
        self.assertEqual(str(context.exception), "Cannot add notes. Course not found.")

    def test_leave_existing_course(self):
        self.student.enroll("Math", [])
        result = self.student.leave_course("Math")
        self.assertEqual(result, "Course has been removed")
        self.assertNotIn("Math", self.student.courses)

    def test_leave_nonexistent_course_raises_error(self):
        with self.assertRaises(Exception) as context:
            self.student.leave_course("Non-existent")
        self.assertEqual(str(context.exception), "Cannot remove course. Course not found.")


if __name__ == "__main__":
    main()