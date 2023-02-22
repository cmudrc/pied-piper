from piperabm.economy import GiniGenerator, gini_coefficient


gini_index = 0.4
gdp_per_capita = 500
g = GiniGenerator(gini_index, gdp_per_capita)
sample = g.generate(1000)
g.show(sample)
print(gini_coefficient(sample))
print(g.mean(sample))
#g.show(sample)
#print(g.gini(sample), g.mean(sample))