import os

from load import infrastructure
from piperabm.tools.file_manager.ora import infrastructure_to_ora

path = os.path.dirname(os.path.realpath(__file__))
infrastructure_to_ora(infrastructure, path)