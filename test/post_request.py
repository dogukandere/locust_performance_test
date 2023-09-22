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
        headers = {
            "token": "QpwL5tke4Pnpja7X4"
        }

        with self.client.post("/api/login", data=pyload, headers=headers) as response:
            if response.status_code == 200:
                print(response)
            else:
                print("Failed")


