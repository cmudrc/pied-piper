from piperabm.tools.json_file import JsonFile


class File:
    """
    Manages file handling methods of model
    """

    def save(self, state: str = ''):
        """
        Save model to file
        """
        name = self.name + '_' + state
        data = self.serialize()
        file = JsonFile(self.path, filename=name)
        file.save(data)

    def save_initial(self):
        """
        Save initial state of model to file
        """
        self.save(state='initial')

    def save_final(self):
        """
        Save final state of model to file
        """
        self.save(state='final')

    def load(self, state: str = ''):
        """
        Load model from file
        """
        name = self.name + '_' + state
        file = JsonFile(self.path, filename=name)
        data = file.load()
        self.deserialize(data)

    def load_initial(self):
        """
        Load initial state of model from file
        """
        self.load(state='initial')

    def load_final(self):
        """
        Load final state of model from file
        """
        self.load(state='final')

    def load_deltas(self, until=None):
        """
        Load all detlas from file
        """
        name = self.name + '_' + 'simulation'
        deltas_file = JsonFile(self.path, filename=name)
        deltas = deltas_file.load()
        if until is None:
            until = len(deltas)
        deltas = deltas[self.step: until]
        return deltas

    def append_delta(self, delta):
        """
        Append the new delta to file
        """
        name = self.name + '_' + 'simulation'
        deltas_file = JsonFile(self.path, filename=name)
        if deltas_file.exists() is False:
            deltas_file.save(data=[])
        deltas_file.append(delta)