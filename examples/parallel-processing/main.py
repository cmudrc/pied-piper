"""
When working with multiple scenarios, meaning dealing with multiple instances of the `Model` class, it is a good practice to run them in parallel.
This speeds up the progress significantly.
"""
import os
import multiprocessing
import piperabm as pa


path = os.path.dirname(os.path.realpath(__file__))
populations = [9, 15]
household_sizes = [3, 5]

def create_model(path, population, household_size):
    """
    Create model instance
    """
    model = pa.Model(
        path=path,
        seed=2,
        name=f"{population}_{household_size}"
    )
    homes_num = round(population/household_size)
    model.infrastructure.generate(
        homes_num=homes_num,
        grid_num=[3,4],
        grid_size=[200,100],
        imperfection_percentage=10
    )
    model.bake()
    model.society.generate(
        num=population,
        gini_index=0.4
    )
    return model

# Create multiple models
models = []
for population in populations:
    for household_size in household_sizes:
        model = create_model(
            path=path,
            population=population,
            household_size=household_size
        )
        models.append(model)
    
def run(model):
    model.run(
        n=100,
        step_size=3600*2,
        save=True,
        save_transactions=True,
        report=True
    )

def main():    
    # Run them on multiple processors
    num_processors = os.cpu_count() - 1  # Better to keep one core
    with multiprocessing.Pool(processes=num_processors) as pool:
        # Map the models to the processes
        pool.map(run, models)
    print("Simulations completed.")


if __name__ == "__main__":
    main()
