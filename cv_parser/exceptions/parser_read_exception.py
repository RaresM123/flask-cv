from functools import wraps


class ReadException(Exception):

    def __init__(self, message="Read Exception", code=500, *args):
        self.message = message
        self.code = code
        super().__init__(self.message, self.code, *args)

    def __str__(self):
        return f"{self.code}: {self.message}"


class PdfReadException(ReadException):

    def __init__(self, message="Pdf Read Exception", code=500, *args):
        self.message = message
        self.code = code
        super().__init__(self.message, self.code, *args)


class JsonReadException(ReadException):

    def __init__(self, message="Json Read Exception", code=500, *args):
        self.message = message
        self.code = code
        super().__init__(self.message, self.code, *args)





# def read_exception(fn):
#     """
#     A decorator that catches exceptions thrown by the decorated function,
#     logs the exception and raises an HTTPException with a status code of 500 and detail "Something went wrong".
#
#     :param fn: The function to be decorated.
#     :return: A new function that wraps the original function and catches exceptions.
#     """
#
#     @wraps(fn)
#     async def _wrapped(*args, **kwargs):
#         try:
#             return await fn(*args, **kwargs)
#         except Exception as e:
#             logger = logging.getLogger(fn.__module__)
#             logger.error(f"error: {e}", exc_info=EXC_INFO)
#             raise HTTPException(status_code=500, detail=str(e))
#
#     return _wrapped