import json
import logging
from functools import wraps

import click
from pydantic import ValidationError

from cv_parser.exceptions.parser_read_exception import JsonReadException


def http_exception(fn):
    """
    A decorator that catches exceptions thrown by the decorated function,
    logs the exception and return into a nice format the error appearing.

    :param fn: The function to be decorated.
    :return: A new function that wraps the original function and catches exceptions.
    """

    @wraps(fn)
    def _wrapped(*args, **kwargs):
        try:
            return fn(*args, **kwargs)
        except ValidationError as e:
            logger = logging.getLogger(fn.__module__)
            logger.error(f"error: {e}")
            return {
                "status_code": 422,
                "error_message": str(e),
                "result": {}
            }

        except Exception as e:
            logger = logging.getLogger(fn.__module__)
            logger.error(f"error: {e}")
            return {
                "status_code": 500,
                "error_message": str(e),
                "result": {}
            }

    return _wrapped


def commands_exception(fn):
    """
    A decorator that catches exceptions thrown by the decorated function,
    logs the exception and return into a nice format the error appearing.

    :param fn: The function to be decorated.
    :return: A new function that wraps the original function and catches exceptions.
    """
    @wraps(fn)
    def _wrapped(*args, **kwargs):
        try:
            return fn(*args, **kwargs)
        except ValidationError as e:
            logger = logging.getLogger(fn.__module__)
            logger.error(f"error: {e}")
            click.echo({
                "status_code": 422,
                "error_message": str(e),
                "result": {}
            })

        except JsonReadException as e:
            logger = logging.getLogger(fn.__module__)
            logger.error(f"error: {e}")
            click.echo({
                "status_code": 500,
                "error_message": str(e),
                "result": {}
            })
    return _wrapped
