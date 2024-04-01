import os

from piperabm.infrastructure_new import Infrastructure
from piperabm.data.utqiavik.load import add_to_model


infrastructure = Infrastructure()
infrastructure.path = os.path.dirname(os.path.realpath(__file__))
infrastructure = add_to_model(
    model=infrastructure,
    streets=True,
    homes=True,
    markets=True,
    latitude_min=None,
    latitude_max=None,
    longitude_min=None,
    longitude_max=None,
    x_min=None,
    x_max=None,
    y_min=None,
    y_max=None
)
print(infrastructure.stat)
infrastructure.save()