from piperabm.economy import ExchangeRate


exchange_rate = ExchangeRate()
exchange_rate.add(source="food", target="currency", rate=10)
exchange_rate.add(source="water", target="currency", rate=2)
exchange_rate.add(source="energy", target="currency", rate=4)


if __name__ == "__main__":
    print(exchange_rate("food", "water"))