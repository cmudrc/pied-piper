from piperabm.economy import ExchangeRate


exchange_rate = ExchangeRate()
exchange_rate.add('food', 'wealth', 10)
exchange_rate.add('water', 'wealth', 2)
exchange_rate.add('energy', 'wealth', 4)


if __name__ == "__main__":
    print(exchange_rate('food', 'water'))