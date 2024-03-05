import requests


def test_student_creation():
    name = "Nataliia"
    age = 25

    request_json = {"name": name, "age": age}

    response = requests.post(
        "http://localhost:5001/students",
        json=request_json
    )
    print(response.status_code)
    print(response.json())


def test_student_update():
    age = 26

    request_json = {"age": age}

    response = requests.patch(
        "http://localhost:5001/students/1",
        json=request_json
    )
    print(response.status_code)
    print(response.json())


if __name__ == "__main__":
    test_student_update()
