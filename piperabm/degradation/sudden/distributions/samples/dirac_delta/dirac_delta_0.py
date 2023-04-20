from piperabm.degradation.sudden.distributions import DiracDelta
from piperabm.unit import DT


dirac_delta = DiracDelta(main=DT(days=10))


if __name__ == "__main__":
    print(dirac_delta)