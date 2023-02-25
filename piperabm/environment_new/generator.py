from piperabm.environment import Environment


class CityGenerator:
    def __init__(self, env_list=[]):
        self.env_list = env_list

    def add(self, env: Environment):
        """
        Add new environemnt to the data
        """
        self.env_list.append(env)

    def generate(self, x_size=None, y_size=None, n=None):
        """
        Generate new random environment
        """
        if x_size is None:
            x_size = self.env_average_size('x')
        elif isinstance(x_size, (int, float)):
            pass
        else:
            raise ValueError
        if y_size is None:
            y_size = self.env_average_size('y')
        elif isinstance(y_size, (int, float)):
            pass
        else:
            raise ValueError
        if n is None:
            n = self.node_average_n()
        elif isinstance(n, int):
            pass
        else:
            raise ValueError

    def calculate_average(number_list):
        n = len(number_list)
        total = sum(number_list)
        return total/n
    
    def node_average_n(self):
        number_list = []
        for env in self.env_list:
            n = env.G.number_of_nodes()
            number_list.append(n)
        return self.calculate_average(number_list)

    def env_average_size(self, axis):
        number_list = []
        for env in self.env_list:
            if axis == 'x' or axis == 'X':
                number_list.append(env.size[0])
            elif axis == 'y' or axis == 'Y':
                number_list.append(env.size[1])
            else:
                raise ValueError
        return self.calculate_average(number_list)

    def extract_env_info(self, env: Environment):
        x_list = []
        y_list = []
        node_type_list = []
        for index in env.index_list:
            node_type = env.node_type(index)
            node_type_list.append(node_type)
            node = env.G.nodes[index]
            pos = node['pos']
            x_list.append(pos[0])
            y_list.append(pos[1])
        return x_list, y_list, node_type_list


    def average_env_size(self, env, types=[]):    
        x_list, y_list, node_type_list = self.extract_env_info(env)
        allowed_x = []
        allowed_y = []
        for k in range(len(node_type_list)):
            if node_type_list[k] in types:
                allowed_x.append(x_list[k])
                allowed_y.append(y_list[k])
        return allowed_x, allowed_y
        
    def average_size(self, types=[]):
        pass
        #for env in self.env_list:


        
        #if axis == 'x' or axis == 'X' or axis == 0:
        #    number_list = []
            


    def generate_nodes_x(self):
        pass

    def generate_nodes_y(self):
        pass