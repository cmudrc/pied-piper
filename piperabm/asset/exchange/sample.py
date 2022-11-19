try:
    from .exchange import Exchange
except:
    from exchange import Exchange


exchange = Exchange()
exchange.add('food', 'wealth', 10)
exchange.add('water', 'wealth', 2)
exchange.add('energy', 'wealth', 5)