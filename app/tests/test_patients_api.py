import pytest

# ✅ Create patient
def test_create_patient(client):
    payload = {"first_name": "John", "last_name": "Doe", "email": "john@doe.com"}
    response = client.post("/patients/", json=payload)

    assert response.status_code == 201
    data = response.json()

    assert data["first_name"] == "John"
    assert data["last_name"] == "Doe"
    assert data["email"] == "john@doe.com"
    assert "id" in data


# ✅ Get all patients
def test_get_patients_list(client):
    # Insert a patient
    client.post("/patients/", json={"first_name": "Ana", "last_name": "Smith", "email": "ana@smith.com"})

    response = client.get("/patients/")
    assert response.status_code == 200

    data = response.json()
    assert isinstance(data, list)
    assert len(data) == 1
    assert data[0]["email"] == "ana@smith.com"


# ✅ Get patient by ID
def test_get_patient_by_id(client):
    created = client.post("/patients/", json={
        "first_name": "Mark",
        "last_name": "Lee",
        "email": "mark@lee.com"
    }).json()

    response = client.get(f"/patients/{created['id']}")
    assert response.status_code == 200

    data = response.json()
    assert data["email"] == "mark@lee.com"
    assert data["id"] == created["id"]


# ❌ Patient not found
def test_get_patient_not_found(client):
    response = client.get("/patients/9999")
    assert response.status_code == 404
    assert response.json()["detail"] == "Patient not found"


# ✅ Update patient
def test_update_patient(client):
    created = client.post("/patients/", json={
        "first_name": "Lia",
        "last_name": "Fox",
        "email": "lia@fox.com"
    }).json()

    response = client.put(f"/patients/{created['id']}", json={"first_name": "LiaUpdated"})
    assert response.status_code == 200

    data = response.json()
    assert data["first_name"] == "LiaUpdated"
    assert data["email"] == "lia@fox.com"


# ✅ Delete patient
def test_delete_patient(client):
    created = client.post("/patients/", json={
        "first_name": "Eli",
        "last_name": "Stone",
        "email": "eli@stone.com"
    }).json()

    response = client.delete(f"/patients/{created['id']}")

    assert response.status_code == 204

    # Verify it’s actually gone
    get_deleted = client.get(f"/patients/{created['id']}")
    assert get_deleted.status_code == 404
