class Plugins:

    def __init__(self):
        self.plugins = []

    def add_plugin(self, plugin):
        self.plugins.append(plugin)

    def plugins_add_data(self, society, start_date, end_date):
        for plugin in self.plugins:
            plugin.read(society, start_date, end_date)