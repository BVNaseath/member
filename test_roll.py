from unittest import TestCase
from roll import Roll
from datetime import date
from club import Club, Member

class TestRoll(TestCase):

    def setUp(self):

        test_members = {"John Smith": "y", "Johnny Doe": "", "Jane Doey": "y"}
        self.roll = Roll(test_members)

    def test_indicate_roll(self):
        test_members = {"John Smith": "", "Johnny Doe": "", "Jane Doey": ""}
        x = ["y", "", "Y"]
        self.assertEqual(3, len(self.roll.members))

    def test_create_roll(self):
        test_members = {"John Smith": "y", "Johnny Doe": "", "Jane Doey": "y"}
        x = {"John Smith", "Johnny Doe", "Jane Doey"}
        self.assertIsNotNone(self.roll.create_roll(x, test_members))
        self.assertEqual(3, len(self.roll.members))

    def test_present_list(self):
        test_members = {"John Smith": "Present", "Johnny Doe": "absent", "Jane Doey": "Present"}
        self.assertIsNotNone(self.roll.present_list(test_members))
        self.assertEqual(2, len(self.roll.present_list(test_members)))

    def test_absent_list(self):
        test_members = {"John Smith": "Present", "Johnny Doe": "Absent", "Jane Doey": "Present"}
        self.assertIsNotNone(self.roll.absent_list(test_members))
        self.assertEqual(2, len(self.roll.present_list(test_members)))
