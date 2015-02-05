__author__ = 'garvit'

class person:

    def __init__(self, firstName, lastName, dob):
        self.firstName = firstName
        self.lastName = lastName
        self.dob = dob

    def __str__(self):
        return "I am " + str(self.firstName) + " " + str(self.lastName);

class employ(person):

    ids = [0]

    def __init__(self, firstName, lastName, dob, job):
        person.__init__(self, firstName, lastName, dob)
        self.job = job
        self.id = self.ids[-1] + 1
        self.ids.append(self.id)

    def __str__(self):
        return person.__str__(self) + " I am a " + self.job + " My employ id is " + str(self.id)