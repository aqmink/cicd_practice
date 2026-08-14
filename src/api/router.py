from fastapi import APIRouter, Depends, HTTPException, status
from api.dependencies import get_item_use_cases
from api.schemas import ItemCreate, ItemResponse
from use_cases.item_repo import ItemUOW

router = APIRouter(prefix="/items", tags=["Items"])


@router.post("/", response_model=ItemResponse, status_code=status.HTTP_201_CREATED)
async def create_item(
    item_in: ItemCreate,
    use_cases: ItemUOW = Depends(get_item_use_cases)
):
    return await use_cases.create(title=item_in.title, description=item_in.description)


@router.get("/{item_id}", response_model=ItemResponse)
async def get_item(item_id: int, use_cases: ItemUOW = Depends(get_item_use_cases)):
    item = await use_cases.get_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item


@router.delete("/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_item(item_id: int, use_cases: ItemUOW = Depends(get_item_use_cases)):
    try:
        await use_cases.delete(item_id)
    except:
        raise HTTPException(status_code=404, detail="Item not found")
