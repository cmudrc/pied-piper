try:
    from .action import Action
except:
    from action import Action

from pr.tools import find_element


class Package:

    def __init__(self, from_name, to_name, resource_name, amount):
        self.resource_name = resource_name
        self.amount = amount
        self.from_name = from_name
        self.to_name = to_name


class Transaction(Action):

    def __init__(
        self,
        start_date,
        end_date,
        package: Package,
        instant=True
    ):
        super().__init__(
            start_date,
            end_date,
            instant
        )
        self.package = package

    def current_amount(self, time):
        progress = self.progress(time)
        return progress * self.package.amount

    def make(self, time, all_agents):
        amount = self.current_amount(time)
        from_agent = find_element(self.package.from_name, all_elements=all_agents)
        to_agent = find_element(self.package.to_name, all_elements=all_agents)
        print('before: ')
        print(from_agent.asset.resources[self.package.resource_name])
        print(to_agent.asset.resources[self.package.resource_name])
        
        print('sub from "from_name"')
        from_remaining = from_agent.asset.resources[self.package.resource_name].sub(amount)
        #amount_remaining = 
        print('amount: ', amount, 'remaining: ', remaining)
        # the amount of possible subtraction
        print('add to "to_name"')
        amount -= remaining
        remaining = to_agent.asset.resources[self.package.resource_name].add(amount)
        print('amount: ', amount, 'remaining: ', remaining)

        print('return to "from_name"')
        amount -= remaining
        remaining = from_agent.asset.resources[self.package.resource_name].add(remaining)
        print('amount: ', amount, 'remaining: ', remaining)

        print(from_agent.asset.resources[self.package.resource_name])
        print(to_agent.asset.resources[self.package.resource_name])
        return remaining
        

if __name__ == "__main__":
    from pr.agent import Agent
    from pr.asset import Asset, Resource, Storage
    from pr.tools import date

    a_1_asset = Asset(resources=[
        Resource(
            name='food',
            storage=Storage(current_amount=5, max_amount=10))
    ])
    a_1 = Agent(name='a_1', asset=a_1_asset)
    a_2_asset = Asset(resources=[
        Resource(
            name='food',
            storage=Storage(current_amount=0, max_amount=20))
    ])
    a_2 = Agent(name='a_2', asset=a_2_asset)
    all_agents = [a_1, a_2,]
    
    package = Package(from_name='a_1', to_name='a_2', resource_name='food', amount=10)

    transaction = Transaction(start_date=date(2020,1,1), end_date=date(2020,1,3), package=package, instant=False)
    r = transaction.make(time=date(2020,1,2), all_agents=all_agents)
    print(r)