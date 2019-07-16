class School:
    def __init__(self,school_name=None,roster={}):
        self.name=school_name
        self.roster=roster
    def add_student(self,student_name,grade_level):
        if self.roster.get(grade_level)==None:
            self.roster.update({grade_level:[student_name]})
        else:
            self.roster[grade_level].append(student_name)
    def grade(self,grade_level):
        return self.roster.get(grade_level)
    def sort_roster(self):
        for grade in self.roster:
            list_of_students=self.roster.get(grade)
            list_of_students.sort()
            self.roster[grade]=list_of_students
        return self.roster