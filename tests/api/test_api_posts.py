import requests

def test_get_by_id():
    
    url = "https://jsonplaceholder.typicode.com/posts/1"
    
    response = requests.get(url)
    assert response.status_code == 200
    print(f"상태 코드: {response.status_code}")

    data = response.json()
    print(data)
    
    assert isinstance(data, dict)
    
    assert data['id'] == 1
    assert data['userId'] == 1
    assert data['title']

def test_create_post():
    
    url = "https://jsonplaceholder.typicode.com/posts"
    
    payload = {
        "title": "api_test_title",
        "body": "api_test_body",
        "userId": 1
    }

    response = requests.post(url, json=payload)
    assert response.status_code == 201
    print(f"상태 코드: {response.status_code}")

    data = response.json()
    print(data)
    
    assert isinstance(data, dict)
    
    assert data['id'] == 101 
    assert 'userId' in data
    assert 'title' in data
    assert 'body' in data
    
def test_update_post():
    
    url = "https://jsonplaceholder.typicode.com/posts/1"
    
    payload = {
        "id": 1,
        "title": "updated_title",
        "body": "updated_body",
        "userId": 1
    }

    response = requests.put(url, json=payload)
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


def test_delete_post():
    url = "https://jsonplaceholder.typicode.com/posts/1"

    response = requests.delete(url)

    assert response.status_code == 200
    print(f"상태 코드: {response.status_code}")