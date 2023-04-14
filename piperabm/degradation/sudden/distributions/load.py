from piperabm.degradation.sudden.distributions import Eternal, DiracDelta, Gaussian

'''
def load_sudden_degradation_distribution(dictionary: dict):
    #sudden_degradation_dict = dictionary['sudden_degradation']
    sudden_degradation_dict = dictionary
    if sudden_degradation_dict['type'] == 'eternal':
        sudden_degradation = Eternal()
    elif sudden_degradation_dict['type'] == 'dirac_delta':
        sudden_degradation = DiracDelta()
    elif sudden_degradation_dict['type'] == 'gaussian':
        sudden_degradation = Gaussian()
    sudden_degradation.from_dict(sudden_degradation_dict)
    return sudden_degradation
'''

def load_sudden_degradation_distribution(dictionary: dict):
    type = dictionary['type']
    if type == 'eternal':
        sudden_degradation = Eternal()
    elif type == 'dirac delta':
        sudden_degradation = DiracDelta()
    elif type == 'gaussian':
        sudden_degradation = Gaussian()
    sudden_degradation.from_dict(dictionary)
    return sudden_degradation