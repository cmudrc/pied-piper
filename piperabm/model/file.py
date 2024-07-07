from piperabm.tools.json_file import JsonFile
from piperabm.tools.delta import Delta


class File:
    """
    Manages file handling methods of model
    """

    def save(self, state: str = '') -> None:
        """
        Save model to file
        """
        name = self.name + '_' + state
        data = self.serialize()
        file = JsonFile(self.path, filename=name)
        file.save(data)

    def save_initial(self) -> None:
        """
        Save initial state of model to file
        """
        self.save(state='initial')

    def save_final(self) -> None:
        """
        Save final state of model to file
        """
        self.save(state='final')

    def load(self, state: str = '') -> None:
        """
        Load model from file
        """
        name = self.name + '_' + state
        file = JsonFile(self.path, filename=name)
        data = file.load()
        self.deserialize(data)

    def load_initial(self) -> None:
        """
        Load initial state of model from file
        """
        self.load(state='initial')

    def load_final(self) -> None:
        """
        Load final state of model from file
        """
        self.load(state='final')

    def load_deltas(self, _from: int = None, _to: int = None) -> list:
        """
        Load all detlas from file
        """
        name = self.name + '_' + 'simulation'
        deltas_file = JsonFile(self.path, filename=name)
        deltas = deltas_file.load()
        if _from is None:
            _from = 0
        if _to is None:
            _to = len(deltas)
        deltas = deltas[_from: _to]
        return deltas

    def append_delta(self, delta) -> None:
        """
        Append the new delta to file
        """
        name = self.name + '_' + 'simulation'
        deltas_file = JsonFile(self.path, filename=name)
        if deltas_file.exists() is False:
            deltas_file.save(data=[])
        deltas_file.append(delta)

    def apply_delta(self, delta) -> None:
        """
        Update model by applying a delta
        """
        self.deserialize(
            Delta.apply(
                old=self.serialize(),
                delta=delta
            )
        )

    def apply_deltas(self, deltas: list = None) -> None:
        """
        Update model by applying all deltas
        """
        if deltas is None:
            deltas = self.load_deltas()
        for delta in deltas:
            self.apply_delta(delta)

    def push(self, steps: int = 1) -> None:
        """
        Push model forward using deltas
        """
        current = self.step
        deltas = self.load_deltas(_from=current, _to=current+steps)
        self.apply_deltas(deltas=deltas)