from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.schemas.client_schema import ClientCreate, ClientRead
from app.repositories.client_repository import ClientRepository
from auth import verify_token

router = APIRouter(prefix="/clients", tags=["Clients"])


@router.post("/", response_model=ClientRead)
async def create_client(
        data: ClientCreate,
        db: Session = Depends(get_db),
        user_id: int = Depends(verify_token)
):
    client = ClientRepository(db)
    return client.create_client(data)


@router.get("/{client_name}", response_model=ClientRead)
async def get_client(
        client_name: str,
        db: Session = Depends(get_db),
        user_id: int = Depends(verify_token)
):
    client = ClientRepository(db)
    return client.get_client(client_name)


@router.put("/{client_name}", response_model=ClientRead)
async def update_client(
    client_name: str,
    client_data: ClientCreate,
    db: Session = Depends(get_db),
    user_id: int = Depends(verify_token)
):
    client = ClientRepository(db)
    return client.update_client(client_name, client_data)


@router.delete("/{client_name}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_client(
        client_name: str,
        db: Session = Depends(get_db),
        user_id: int = Depends(verify_token)
):
    client = ClientRepository(db)
    return client.detete_client(client_name)
