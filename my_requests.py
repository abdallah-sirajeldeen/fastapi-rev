import requests


def create_user_lists():
    users = []
    for _ in range(0, 10):
        users.append({"email": "email" + str(_), "is_active": True, "bio": "bio" + str(_)})

    for x in users:
        url = 'http://127.0.0.1:8000/users'
        r = requests.post(url, json=x)
        print(r.text)


if __name__ == "__main__":
    create_user_lists()
