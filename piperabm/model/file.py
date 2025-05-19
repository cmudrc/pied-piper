import os
import csv
import keepdelta as kd

from piperabm.tools.json_file import JsonFile


class File:
    """
    Manages file handling methods of model
    """

    @property
    def result_directory(self):
        """
        Return result directory
        """
        if self.path is None:
            raise ValueError("Define path to continue.")
        result = os.path.join(self.path, 'result')
        if self.name != '':
            result = os.path.join(result, self.name)
        return result

    def save(self, name: str) -> None:
        """
        Save model to file
        """
        path = self.result_directory
        if not os.path.exists(path): # Create result directory if doesn't exist
            os.makedirs(path)
        data = self.serialize()
        file = JsonFile(path=path, filename=name)
        file.save(data)

    def save_initial(self) -> None:
        """
        Save initial state of model to file
        """
        self.save(name='initial')

    def save_final(self) -> None:
        """
        Save final state of model to file
        """
        self.save(name='final')

    def load(self, name: str) -> None:
        """
        Load model from file
        """
        file = JsonFile(path=self.result_directory, filename=name)
        if file.exists() is False:
            raise ValueError(f"File {name} doesn't exist in {self.result_directory}")
        data = file.load()
        self.deserialize(data)

    def load_initial(self) -> None:
        """
        Load initial state of model from file
        """
        self.load(name='initial')

    def load_final(self) -> None:
        """
        Load final state of model from file
        """
        self.load(name='final')

    def load_deltas(
            self,
            _from: int = None,
            _to: int = None
        ) -> list:
        """
        Load all detlas from file
        """
        deltas_file = JsonFile(path=self.result_directory, filename='simulation')
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
        deltas_file = JsonFile(path=self.result_directory, filename='simulation')
        if deltas_file.exists() is False:
            deltas_file.save(data=[])
        deltas_file.append(delta)

    def apply_delta(self, delta) -> None:
        """
        Update model by applying a delta
        """
        self.deserialize(
            kd.apply(
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

    def append_transactions(self, transactions) -> None:
        """
        Append the new delta to file
        """
        name = 'transactions' + '.' + 'csv'
        filepath = os.path.join(self.result_directory, name)
        headers = ['from', 'to', 'amount', 'resource', 'time']
        if not os.path.exists(filepath):
            # Create it with headers only
            with open(filepath, mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(headers)
        with open(filepath, mode='a', newline='') as file:
            writer = csv.writer(file)
            for transaction in transactions:
                writer.writerow(transaction)


if __name__ == "__main__":

    from piperabm.infrastructure.samples.infrastructure_0 import model

    model.path = os.path.dirname(os.path.realpath(__file__))
    model.save_initial()
    model.load_initial()