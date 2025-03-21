# src/py_unifi_ddns_sync/py_logging.py
"""Custom logging configuration module."""
import logging
import time


def configure_logger(level=logging.INFO):
    """Configure logging with a custom format and local timezone.
    Args:
        level (int): Logging level (e.g., logging.INFO, logging.DEBUG).
    """
    logging.basicConfig(
        level=level,
        format='%(asctime)s %(levelname)s:%(name)s: %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S %Z',
        handlers=[logging.StreamHandler()]
    )

    logging.Formatter.converter = time.localtime
    logging.debug("Logging setup complete with level: %s",
                  logging.getLevelName(level))


def get_logger(name):
    """Get a logger with the specified name.
    Args:
        name (str): Logger name.
    Returns:
        logging.Logger: Logger instance.
    """
    return logging.getLogger(name)
