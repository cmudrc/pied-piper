from piperabm.economy import Economy, Player, Exchange

 
p1 = Player(agent=1, source={'food': 8}, demand={'food': 6}, wallet=100)
p2 = Player(agent=2, source={'food': 8}, demand={'food': 8}, wallet=200)

exchange = Exchange()
exchange.add('food', 'wealth', 10)

econ = Economy(exchange)
econ.add([p1, p2])
econ.solve()
print(econ)