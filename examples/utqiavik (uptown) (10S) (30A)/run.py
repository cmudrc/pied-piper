from load import model


""" Run model """
model.set_step_size(10)
model.run(n=40, save=True)