from locust import task, constant, HttpUser, TaskSet, between, constant_pacing


class FirstTest(HttpUser):

    wait_time = between(1, 5)

    def on_start(self):
        print("start settings")

    @task
    def get_users(self):
        response = self.client.get("/api/users?page=2")
        print("Response text:", response.text)
        print("Response status code:", response.status_code)

    @task(2)
    def create_user(self):
        response = self.client.post("/api/users", data='''
        { "name": "morpheus","job": "leader"}''')
        print("Response text:", response.text)
        print("Response status code:", response.status_code)

