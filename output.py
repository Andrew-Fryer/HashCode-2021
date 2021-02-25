
class Solution:
    def __init__(self, file_name):
        self.f = open(file_name, "w+")

    def add_intersection(self, intersection, number_of_streets_green, street_names, street_times):
        self.f.write(intersection)
        self.f.write(number_of_streets_green)
        for i in len(street_names):
            self.f.write(street_names[i] + " " + street_times[i])

    def close_file(self):
        self.f.close()
