from piperabm.economy import Exchange


exchange_rate = Exchange()
exchange_rate.add('food', 'wealth', 10)
exchange_rate.add('water', 'wealth', 2)
exchange_rate.add('energy', 'wealth', 4)


if __name__ == "__main__":
    print(exchange_rate.rate('food', 'water'))