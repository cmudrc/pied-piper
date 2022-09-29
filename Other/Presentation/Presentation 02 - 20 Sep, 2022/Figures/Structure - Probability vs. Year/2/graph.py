from datetime import date
import random
import matplotlib.pyplot as plt
import numpy as np


seed = 200


class Probability():
    def __init__(self, ps, ts, t0, degree):
        self.ps = ps
        self.ts = ts
        self.t0 = t0
        self.degree = degree

        self.a = self.a_calc()

    def a_calc(self):
        element_1 = self.ps - 1
        element_2 = 1 - np.exp(self.degree * (self.ts - self.t0))
        return element_1 / element_2

    def b_calc(self, t):
        return 1 - np.exp(self.degree * (t - self.t0))

    def p(self, t):
        return 1 + self.a * self.b_calc(t)

    def t_end(self):
        return (np.log(1 + (1 / self.a)) / self.degree) + self.t0


t0 = 0
ps, ts = 0.5, 20

degree = 0.2
pro_1 = Probability(ps, ts, t0, degree)
t_list_1 = np.arange(t0, t0 + pro_1.t_end())
p_list_1 = list()
for t in t_list_1:
    p = pro_1.p(t)
    if p < 0: p = 0
    p_list_1.append(p)

degree = 0.7
pro_2 = Probability(ps, ts, t0, degree)
t_list_2 = np.arange(t0, t0 + pro_2.t_end())
p_list_2 = list()
for t in t_list_1:
    p = pro_2.p(t)
    if p < 0: p = 0
    p_list_2.append(p)

degree = 2
pro_3 = Probability(ps, ts, t0, degree)
t_list_3 = np.arange(t0, t0 + pro_3.t_end())
p_list_3 = list()
for t in t_list_1:
    p = pro_3.p(t)
    print(p)
    if p < 0: p = 0
    p_list_3.append(p)

plt.plot(t_list_1, p_list_1)
plt.plot(t_list_1, p_list_2)
plt.plot(t_list_1, p_list_3)
plt.title('Sample Structure')
plt.xlabel('Year')
plt.ylabel('Probability')
#txt = 'coeff = ' + str(s.coeff) + '\n' + \
#      'degree = ' + str(s.degree)
#plt.text(2008, 0.8, txt)
plt.show()