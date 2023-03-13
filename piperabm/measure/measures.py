class Measures:

    def __init__(self):
        self.measures = []

    def add_measure(self, measure):
        self.measures.append(measure)

    def add_measures(self, measures: list):
        for measure in measures:
            self.add_measure(measure)

    def measure_add_data(self, society, start_date, end_date):
        for measure in self.measures:
            measure.add_data(society, start_date, end_date)
    
    def show(self):
        for measure in self.measures:
            measure.show()