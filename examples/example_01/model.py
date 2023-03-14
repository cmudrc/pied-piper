from piperabm import Model
from piperabm.measure import Accessibility, TravelLength
from piperabm.unit import Date, DT

from society import soc


m = Model(
    society=soc,
    step_size=DT(hours=12),
    current_date=Date(2020, 1, 2)
)
m.measures.add([Accessibility(), TravelLength()])
m.run(n=5)
print(m.measures('accessibility').efficiency())
m.measures.show()