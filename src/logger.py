import logging
from datetime import datetime

from config import CARPETA_LOGS

CARPETA_LOGS.mkdir(
    exist_ok=True
)

nombre = datetime.now().strftime(
    "%Y-%m-%d_%H-%M-%S.log"
)

archivo_log = CARPETA_LOGS / nombre

logging.basicConfig(
    filename=archivo_log,
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
)

logger = logging.getLogger(__name__)