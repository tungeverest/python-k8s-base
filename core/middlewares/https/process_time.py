import http
import time
import logging

from fastapi import Request


# https://dev.to/dpills/fastapi-production-setup-guide-1hhh
async def process_time_log_middleware(request: Request, call_next):
    """
    This middleware will log all requests and their processing time.
    E.g. log:  HOST:PORT - GET /ping 200 OK 1.00ms
    """
    logging.debug("middleware: process_time_log_middleware")
    url = f"{request.method}: {request.url.path}?{request.query_params}" if request.query_params else request.url.path
    start_time = time.time()
    response = await call_next(request)
    process_time = (time.time() - start_time) * 1000
    formatted_process_time = "{0:.2f}".format(process_time)
    host = getattr(getattr(request, "client", None), "host", None)
    port = getattr(getattr(request, "client", None), "port", None)
    response.headers["X-Process-Time"] = formatted_process_time
    try:
        status_phrase = http.HTTPStatus(response.status_code).phrase
    except ValueError:
        status_phrase=""
    logging.info(f'{host}:{port} - "{request.method} {url}" {response.status_code} {status_phrase} {formatted_process_time}ms')
    return response
