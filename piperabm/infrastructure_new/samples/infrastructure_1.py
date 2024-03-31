from piperabm.infrastructure_new import Infrastructure, Home, Street
    

infrastructure = Infrastructure(proximity_radius=0.1)
street = Street(pos_1=[0, 0], pos_2=[-60, 40], name="road")
home_1 = Home(pos=[5, 0], name="home 1")
home_2 = Home(pos=[-60, 45], name="home 1")
infrastructure.add(street, id=0)
infrastructure.add(home_1, id=1)
infrastructure.add(home_2, id=2)
infrastructure.bake(save=False)


if __name__ == '__main__':
    infrastructure.show()
