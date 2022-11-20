from piperabm.degradation import DegradationProperty, degradation_kwargs


class Track(DegradationProperty):

    def __init__(self):
        super().__init__(
            **degradation_kwargs
        )