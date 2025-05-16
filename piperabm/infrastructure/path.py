import networkx as nx


class Path:
    """
    Path finding algorythm
    """

    def has_path(self, id_start: int, id_end: int) -> bool:
        """
        Rapidly check if there is any path
        """
        return nx.has_path(
            self.G,
            source=id_start,
            target=id_end
        )

    def path(self, id_start: int, id_end: int) -> list:
        """
        Path finding algorythm using A_star
        """
        return nx.astar_path(
            self.G,
            source=id_start,
            target=id_end,
            heuristic=self.heuristic_paths.estimated_distance,
            weight="adjusted_length"
        )


if __name__ == "__main__":

    from piperabm.infrastructure.samples.infrastructure_1 import model

    has_path = model.infrastructure.has_path(id_start=1, id_end=2)
    print("has path? :", has_path)
    
    path = model.infrastructure.path(id_start=1, id_end=2)
    print("path: ", path)