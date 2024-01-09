import pprint

pp = pprint.PrettyPrinter(indent=4)

stuff = ['spam', 'eggs', 'lumberjack', 'knights', 'ni']
stuff.insert(0, stuff[:])

pp.pprint(stuff)