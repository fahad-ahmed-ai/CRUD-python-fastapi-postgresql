from fastapi import APIRouter
from .views import login , create_user, create_transaction, get_transactions,\
                   update_transaction, delete_transaction

router = APIRouter(prefix="")

router.post("/login", tags=["User"])(login)
router.post("/register", tags=["User"])(create_user)
router.post("/transactions", tags=["Transaction"])(create_transaction)
router.get("/get_transactions", tags=["Transaction"])(get_transactions)
router.put("/transactions/{transaction_id}",tags=["Transaction"])(update_transaction)
router.delete("/transactions/{transaction_id}",tags=["Transaction"])(delete_transaction)