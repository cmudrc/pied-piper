from load import model


""" Run model """
model.set_step_size(10)
#model.update(save=True)
model.run(n=140, save=True)