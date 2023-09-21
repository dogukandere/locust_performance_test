from locust import User, task, constant


class FirstTest(User):
    wait_time = constant(1)

    @task
    def launch(self):
        print("url")

    @task
    def search(self):
        print("search")
