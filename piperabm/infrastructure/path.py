import networkx as nx


class Path:
    """
    Path finding algorythm
    """

    def path(self, id_start: int, id_end: int) -> list:
        """
        Path finding algorythm using A_star
        """
        result = None
        if nx.has_path(
            self.G,
            source=id_start,
            target=id_end
        ):
            result = nx.astar_path(
                self.G,
                source=id_start,
                target=id_end,
                heuristic=self.heuristic_paths.estimated_distance,
                weight="adjusted_length"
            )
        return result


if __name__ == "__main__":

    from piperabm.infrastructure.samples import model_1 as model

    path = model.infrastructure.path(id_start=1, id_end=2)
    print(path)