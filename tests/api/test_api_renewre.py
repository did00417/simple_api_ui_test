import pytest

def test_get_by_post(api):
    
    response = api.get("/posts/1")
    assert response.status_code == 200
    print(f"상태 코드: {response.status_code}")

    data = response.json()
    print(data)
    
    assert isinstance(data, dict)
    
    assert data['id'] == 1
    assert data['userId'] == 1
    assert data['title']

def test_create_post(api):

    payload = {
        "title": "api_test_title",
        "body": "api_test_body",
        "userId": 1
    }

    response = api.post("/posts", json=payload)
    assert response.status_code == 201
    print(f"상태 코드: {response.status_code}")

    data = response.json()
    print(data)
    
    assert isinstance(data, dict)
    
    assert data['id'] == 101 
    assert 'userId' in data
    assert 'title' in data
    assert 'body' in data
    
def test_update_post(api):
    
    payload = {
        "id": 1,
        "title": "updated_title",
        "body": "updated_body",
        "userId": 1
    }

    response = api.put("/posts/1", json=payload)
    assert response.status_code == 200
    print(f"상태 코드: {response.status_code}")

    data = response.json()
    print(data)
    
    assert isinstance(data, dict)
    
    assert data['id'] == 1
    assert data['title'] == "updated_title"
    assert data['body'] == "updated_body"
    assert data['userId'] == 1
    print("업데이트된 데이터 확인됨")


def test_delete_post(api):

    response = api.delete("/posts/1")

    assert response.status_code == 200
    print(f"상태 코드: {response.status_code}")