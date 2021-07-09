from .logging_config import get_logger

logger = get_logger(__name__)

def from_function():
    
    logger.debug("Root logging using simple logger from module function")



logger.debug("Root logging using simple logger from module")

from_function()