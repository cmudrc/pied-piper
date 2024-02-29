class Measure:

    def __init__(self, model):
        self.accessibilty = []
        self.model = model

    def read(self):
        self.agents = self.model.all_alive_agents
        self.exchange_rate = self.model.exchange_rate

    def calculate_accessibilty(self):
        agents_accessibilities = []
        for agent_index in self.agents:
            agent = self.model.get(agent_index)
            resources = agent.resources
            # current
            current_values = resources.value(self.exchange_rate)
            resources_value_current = current_values.sum
            # max
            resources_max = resources.max
            max_values = resources_max.value(self.exchange_rate)
            resources_value_max = max_values.sum
            # accessibility
            agent_accessibility = resources_value_current / resources_value_max
            agents_accessibilities.append(agent_accessibility)
        return sum(agents_accessibilities) / len(agents_accessibilities)
    

if __name__ == "__main__":
    from piperabm.model.samples import model_3 as model

    measure = Measure(model)
    measure.read()
    print(measure.calculate_accessibilty())
