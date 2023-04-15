from piperabm.degradation.sudden.distributions import Eternal, DiracDelta, Gaussian


def load_sudden_degradation_distribution(dictionary: dict):
    if dictionary is None:
        sudden_degradation = None
    else:
        type = dictionary['type']
        if type == 'eternal':
            sudden_degradation = Eternal()
        elif type == 'dirac delta':
            sudden_degradation = DiracDelta()
        elif type == 'gaussian':
            sudden_degradation = Gaussian()
        sudden_degradation.from_dict(dictionary)
    return sudden_degradation