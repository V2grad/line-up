from typing import Dict

from fastapi.testclient import TestClient

from app.core.config import settings
from app import crud


def test_admin_access(client: TestClient) -> None:
    admin_data = {
        "name":  "Someone",
    }
    r = client.post(f"{settings.API_V1_STR}/login/user", data=login_data)
    resp = r.json()
    assert resp.status_code == 200
    assert resp["name"] == 'Someone'


def test_(
    client: TestClient, superuser_token_headers: Dict[str, str]
) -> None:
    r = client.post(
        f"/api/v1/login/test-token", headers=superuser_token_headers,
    )
    result = r.json()
    assert r.status_code == 200
    assert "email" in result
