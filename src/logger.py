import logging

logging.basicConfig(
    filename="copier.log", format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger()

logger.setLevel(logging.DEBUG)