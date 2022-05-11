
from logger.logger import Applogs

log = Applogs('logger\logs\projectlogs.log', 'DEBUG')
log.getlogger(__file__)

log.debug("debug logged")
