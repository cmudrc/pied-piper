from load_final import model


""" Run model """
model.set_step_size(10)
model.run(n=500, save=True)