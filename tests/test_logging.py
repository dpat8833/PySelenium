import logging


def test_plan_logs():
    LOGGER = logging.getLogger(__name__)
    LOGGER.info("This is information logs")
    LOGGER.error("This is a error log")
    LOGGER.critical("This is a critical log")
    LOGGER.warning("This is a warning log")
