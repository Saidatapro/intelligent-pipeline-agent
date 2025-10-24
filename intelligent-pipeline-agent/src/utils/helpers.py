
import logging, json, time
from .config import settings
logging.basicConfig(level=settings.log_level, format='%(asctime)s %(levelname)s %(name)s %(message)s')
logger = logging.getLogger("ipa")
def jsond(obj): return json.dumps(obj, ensure_ascii=False, default=str)
def ts_ms(): return int(time.time()*1000)
