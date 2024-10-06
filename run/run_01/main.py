from datetime import datetime

from create import main as create
from run import main as run
from impact import main as impact
from run_impacted import main as run_impacted
from measure import main as measure
from plot import main as plot
from animate import main as animate
from result_save import main as result_save


def main():
    start_time = datetime.now()
    print("start time: ", start_time)

    create()
    run()
    impact()
    run_impacted()
    measure()
    plot()
    animate()
    result_save()

    end_time = datetime.now()
    print("end time: ", end_time)
    duration = end_time - start_time
    print("duration: ", duration)


if __name__ == "__main__":
    main()