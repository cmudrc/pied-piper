from piperabm.matter.matters.matters import Matters


def matters_sum(delta_matters_list: list):
    all_names = []
    for delta_matters in delta_matters_list:
        names = delta_matters.names
        for name in names:
            if name not in all_names:
                all_names.append(name)
    start = Matters()
    start.zeros(all_names)
    return sum(delta_matters_list, start)


if __name__ == '__main__':
    
    from piperabm.matter.matters.samples import delta_matters_0, delta_matters_1

    delta_matters_list = [delta_matters_0, delta_matters_1]
    result = matters_sum(delta_matters_list)
    result.print