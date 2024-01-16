from piperabm.matter import DeltaMatters
from piperabm.matter.delta_matter.samples import delta_matter_3, delta_matter_4, delta_matter_5


delta_matters = DeltaMatters(delta_matter_3, delta_matter_4, delta_matter_5)


if __name__ == '__main__':
    delta_matters.print