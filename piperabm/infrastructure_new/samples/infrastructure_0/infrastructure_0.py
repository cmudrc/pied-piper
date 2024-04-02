from piperabm.infrastructure_new import Infrastructure, Home
    

infrastructure = Infrastructure()
home = Home(name='home', pos=[0, 0])
infrastructure.add(home, id=0)
infrastructure.bake()


if __name__ == '__main__':
    #print(infrastructure)
    infrastructure.show()
