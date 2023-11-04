from aiogram import Router

from .orders import router as order_router
from .start import router as start_router

router = Router()

router.include_router(start_router)
router.include_router(order_router)