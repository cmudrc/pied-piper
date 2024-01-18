from piperabm.matter import DeltaMatters
from piperabm.matter.delta_matter.samples import delta_matter_0 as delta_food
from piperabm.matter.delta_matter.samples import delta_matter_1 as delta_water
from piperabm.matter.delta_matter.samples import delta_matter_2 as delta_energy


delta_matters = DeltaMatters(delta_food, delta_water, delta_energy)


if __name__ == '__main__':
    delta_matters.print