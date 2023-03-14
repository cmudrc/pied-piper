class Measures:
    """
    Manage measure objects that calculate the result of the simulation
    """
    
    def __init__(self):
        self.measures = []

    def _add_measure(self, measure):
        """
        Add a single measure
        """
        self.measures.append(measure)

    def _add_measures(self, measures: list):
        """
        Add measures in batch
        """
        for measure in measures:
            self._add_measure(measure)

    def add(self, measures):
        """
        Add measures
        """
        if isinstance(measures, list):
            self._add_measures(measures)
        else:
            self._add_measure(measures)

    def read_data(self, society, start_date, end_date):
        """
        Add new data point to the measures
        """
        for measure in self.measures:
            measure.read_data(society, start_date, end_date)
    
    def show(self):
        """
        Show all measure results in sequence
        """
        for measure in self.measures:
            measure.show()