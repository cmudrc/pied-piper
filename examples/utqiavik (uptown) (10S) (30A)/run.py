from load_final import model


""" Run model """
model.set_step_size(10)
model.run(n=400, save=True)