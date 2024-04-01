import os

from piperabm.infrastructure_new import Infrastructure
from piperabm.data.utqiavik.load import add_to_model
from piperabm.data.utqiavik.samples.downtown.info import latitude_min, latitude_max, longitude_min, longitude_max


infrastructure = Infrastructure()
infrastructure.path = os.path.dirname(os.path.realpath(__file__))
infrastructure = add_to_model(
    model=infrastructure,
    streets=True,
    homes=True,
    markets=True,
    latitude_min=latitude_min,
    latitude_max=latitude_max,
    longitude_min=longitude_min,
    longitude_max=longitude_max,
    x_min=None,
    x_max=None,
    y_min=None,
    y_max=None
)
infrastructure.show_stat()
infrastructure.save()
infrastructure.show()