from fastapi import FastAPI

from src.settings import static, media
from src.shop.views import router as shop_router
from src.api.endpoints import router as api_router


app = FastAPI(
    docs_url=None,
    redoc_url=None,
    openapi_url=None,
    swagger_ui_parameters=None,
    swagger_ui_init_oauth=None,
    swagger_ui_oauth2_redirect_url=None
)
app.mount(path='/static', app=static, name='static')
app.mount(path='/media', app=media, name='media')
app.include_router(router=shop_router)
app.include_router(router=api_router)
