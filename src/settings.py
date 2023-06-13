from pathlib import Path
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

from .types import Settings
from .mixins import contact_mixin


BASE_DIR = Path(__file__).resolve().parent.parent
SETTINGS = Settings()

templating = Jinja2Templates(
    directory=BASE_DIR / 'templates',
    context_processors=[contact_mixin]
)
static = StaticFiles(directory=BASE_DIR / 'static')
media = StaticFiles(directory=BASE_DIR / 'media')
