from piperabm.degradation.sudden.distributions import DiracDelta, Gaussian


def load_sudden_degradation(dictionary: dict):
    sudden_degradation_dict = dictionary['sudden_degradation']
    if sudden_degradation_dict['type'] == 'dirac_delta':
        sudden_degradation = DiracDelta()
    elif sudden_degradation_dict['type'] == 'gaussian':
        sudden_degradation = Gaussian()
    sudden_degradation.from_dict(sudden_degradation_dict)
    return sudden_degradation