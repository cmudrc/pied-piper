from piperabm.economy import GiniGenerator


def agent_generator(
    homes: list,
    gini: float,
    gdp_per_capita: float,
    n: int = 1,
):
    pass
        

if __name__ == "__main__":
    agents = agent_generator(
        homes=[0, 1, 2],
        gini=0.5,
        gdp_per_capita=200,
        n=5
    )
