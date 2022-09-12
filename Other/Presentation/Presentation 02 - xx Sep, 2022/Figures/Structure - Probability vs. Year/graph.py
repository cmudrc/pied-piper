'''
Copy and paste it in pied-pier/evironment directory
'''
from datetime import date
import matplotlib.pyplot as plt

from core.structure import Structure


s = Structure(
    name='sample infrastructure',
    active=True,
    cost=1000,
    project_start_date=date(2000, 1, 1),
    coeff=0.01,
    degree=2,
    seed=208
)

probability_per_time_list = list()
year_list = range(2000, 2011)
for year in year_list:
    new = s.probability_per_time(date(year, 1, 1))
    probability_per_time_list.append(new)

plt.plot(year_list, probability_per_time_list)
plt.title('Sample Structure')
plt.xlabel('Year')
plt.ylabel('Probability')
txt = 'coeff = ' + str(s.coeff) + '\n' + \
      'degree = ' + str(s.degree)
plt.text(2008, 0.8, txt)
plt.show()