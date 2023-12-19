from datetime import date
from club import Club

class Roll:
    def __init__(self, members):
        self.members = members
        #self.date = roll_date

    current_roll = {}

    def indicate_roll(self, members, current_roll, x):
        for member in members:
            if current_roll[member] == "":
                current_roll[member] = x

    def create_roll(self, x, current_roll):
        for x in current_roll:
            if current_roll[x] == "y":
                current_roll[x] = "Present"
            else:
                current_roll[x] = "Absent"
        return current_roll

    def present_list(self, current_roll):
        present_people = []
        for key in current_roll:
            if current_roll[key] == "Present":
                present_people.append(current_roll[key])
        return present_people

    def absent_list(self, current_roll):
        absent_people = []
        for key in current_roll:
            if current_roll[key] == "Absent":
                absent_people.append((current_roll[key]))
        return absent_people
