from locust import HttpUser, task, between


class PostRequestToken(HttpUser):
    def __init__(self, parent):
        super(PostRequestToken, self).__init__(parent)
        self.token = ""

    wait_time = between(2, 5)
    host = "https://reqres.in"

    def on_start(self):
        pyload = {
            "email": "eve.holt@reqres.in",
            "password": "cityslicka"
        }
        with self.client.post(url="/api/login", data=pyload) as response:
            self.token = response.json()["token"]

    @task
    def login(self):
        pyload = {
            "email": "eve.holt@reqres.in",
            "password": "cityslicka"
        }

        self.client.post(url="/api/login", data=pyload, headers={"token": self.token})