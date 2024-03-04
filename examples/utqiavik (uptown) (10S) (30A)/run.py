from load import model


""" Run model """
model.set_step_size(10)
model.run(n=50, save=True)