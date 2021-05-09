def exercise_2(inputs): # DO NOT CHANGE THIS LINE
    """
    class Party:
    info_attendees = {}
    detailed_info_attendees = {}

    def add_attendees(self, family_name, number_of_attendees):
        self.family_name = family_name
        self.number_of_attendees = number_of_attendees
        self.info_attendees[self.family_name] = number_of_attendees
    def detailed_attendees(self, family_names, adult_attendees, child_attendees):
        self.detailed_info_attendees[family_names] = (adult_attendees, child_attendees)
    def check_and_resolve(self):
        value = {k: self.detailed_info_attendees[k] for k in set(self.detailed_info_attendees) - set(self.info_attendees)}
        if value == {}:
            print("no difference")
        else:
            print("there is difference")
    def display(self):
        return self.info_attendees
    def display_detailed(self):
        return self.detailed_info_attendees
    def get_total_attendees(self):
        number_of_attendees = [len(v) for v in self.detailed_info_attendees.values()]
        total = sum(number_of_attendees)
        print(total)
    def filter_attendees(self):
        if self.child_attendees == True:
            print(self.detailed_info_attendees[self.family_names],"has a child")
        elif self.child_attendees == False:
            print("no children")
    """
    output = inputs

    return output       # DO NOT CHANGE THIS LINE
