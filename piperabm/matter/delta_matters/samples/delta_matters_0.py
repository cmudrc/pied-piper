from piperabm.matter import DeltaMatters
from piperabm.matter.delta_matter.samples import delta_matter_0, delta_matter_1, delta_matter_2


delta_matters = DeltaMatters(delta_matter_0, delta_matter_1, delta_matter_2)


if __name__ == '__main__':
    delta_matters.print