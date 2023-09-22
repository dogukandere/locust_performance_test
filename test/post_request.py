from locust import HttpUser, task, between

class PostRequest(HttpUser):

    wait_time = between(1, 3)
    host = "https://reqres.in"

    @task
    def login_request(self):
        pyload = {
            "email": "eve.holt@reqres.in",
            "password": "cityslicka"
        }

        with self.client.post("/api/login", data=pyload) as response:
            if response.status_code == 200:
                print(response)
            else:
                print("Failed")


