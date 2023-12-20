from logging import config


def configure_logger(logger: str, level: str, file_path: str):
    config.dictConfig(
        {
            "version": 1,
            "disable_existing_loggers": False,
            "formatters": {
                "defaultFormatter": {
                    "class": "logging.Formatter",
                    "datefmt": "%Y-%m-%dT%H:%M:%SZ",
                    "format": "%(asctime)s || %(levelname)s [%(name)s: %(lineno)s] - %(message)s",
                },
                "consoleFormatter": {
                    "class": "logging.Formatter",
                    "datefmt": "%Y-%m-%dT%H:%M:%SZ",
                    "format": "%(asctime)s || [%(levelname)s] [%(name)s: %(lineno)s] %(module)s.%(funcName)s %(process)d %(thread)d %(message)s",
                },
                "fileFormatter": {
                    "class": "logging.Formatter",
                    "datefmt": "%Y-%m-%dT%H:%M:%SZ",
                    "format": "%(asctime)s || [%(levelname)s] [%(name)s: %(lineno)s]: %(message)s",
                },
            },
            "handlers": {
                "defaultHandler": {
                    "level": "WARNING",
                    "stream": "ext://sys.stdout",
                    "formatter": "defaultFormatter",
                    "class": "logging.StreamHandler",
                },
                "consoleHandler": {
                    "level": level,
                    "stream": "ext://sys.stdout",
                    "formatter": "consoleFormatter",
                    "class": "logging.StreamHandler",
                },
                # "fileHandler": {
                #     "mode": "a",
                #     "level": level,
                #     "backupCount": 10,
                #     "maxBytes": 500000,
                #     "encoding": "utf-8",
                #     "formatter": "fileFormatter",
                #     "filename": file_path,
                #     # 'class': 'logging.FileHandler',
                #     "class": "logging.handlers.RotatingFileHandler",
                # },
            },
            "root": {
                "level": "WARNING",
                "propagate": True,
                "handlers": ["defaultHandler"],
            },
            "loggers": {
                "src": {
                    "propagate": False,
                    "level": level,
                    "handlers": ["consoleHandler"],
                },
            },
        }
    )
    # return logging.getLogger(logger)
