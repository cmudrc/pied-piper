from piperabm.economy import ExchangeRate


exchange_rate = ExchangeRate()
exchange_rate.add(source="food", target="currency", rate=1)
exchange_rate.add(source="water", target="currency", rate=1)
exchange_rate.add(source="energy", target="currency", rate=1)


if __name__ == "__main__":
    print(exchange_rate("food", "water"))