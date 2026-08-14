import pytest
from httpx import AsyncClient


@pytest.mark.anyio
async def test_full_crud_api_flow(client: AsyncClient):
    response = await client.post("/items/", json={"title": "Laptop", "description": "MacBook"})
    assert response.status_code == 201
    item_id = response.json()["id"]

    get_res = await client.get(f"/items/{item_id}")
    assert get_res.status_code == 200
    assert get_res.json()["title"] == "Laptop"

    del_res = await client.delete(f"/items/{item_id}")
    assert del_res.status_code == 204