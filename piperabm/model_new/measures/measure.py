class Measures:

    def __init__(self, model):
        self.model = model
        self.library = {}

    def add(self, measure):
        measure.measures = self  # Binding
        self.library[measure.name] = measure

    def read(self):
        for measure in self.library:
            measure.read()
    

if __name__ == "__main__":
    from piperabm.model.samples import model_3 as model

    measure = Measures(model)

