from piperabm.infrastructure_new import Infrastructure, Home
    

infrastructure = Infrastructure(proximity_radius=1)
home = Home(name='Sample Settlement', pos=[0, 0])
infrastructure.add(home, id=1)
infrastructure.bake()


if __name__ == '__main__':
    #print(infrastructure)
    infrastructure.show()
