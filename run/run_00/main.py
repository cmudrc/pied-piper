from datetime import datetime
import csv
import os

from create import main as create
from run import main as run
from impact import main as impact
from run_impacted import main as run_impacted

from info import names, name_to_setup


def main():
    start_time = datetime.now()
    print("start time: ", start_time)

    # Save model setups to file
    headers = ['name', 'population', 'household_size', 'seed', 'impact_type', 'impact_level']
    path = os.path.dirname(os.path.realpath(__file__))
    filepath = os.path.join(path, 'result')
    filename = os.path.join(filepath, 'setups.csv')
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(headers)
    for name in names:
        setup = name_to_setup(name)
        if setup['impact'] is None:
            impact_info = ['none', 'none']
        else:
            impact_info = setup['impact']
        row = [name, setup['population'], setup['household_size'], setup['seed'], impact_info[0], impact_info[1]]
        with open(filename, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(row)
    
    create()
    run()
    impact()
    run_impacted()

    end_time = datetime.now()
    print("end time: ", end_time)
    duration = end_time - start_time
    print("duration: ", duration)


if __name__ == "__main__":
    main()