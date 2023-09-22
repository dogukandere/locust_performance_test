from locust import HttpUser, task, between


class AmazonTest(HttpUser):

    wait_time = between(1, 5)

    def on_start(self):
        print("Test starting")

    @task
    def get_first_request(self):
        response = self.client.get("/gp/bestsellers?ref_=nav_cs_bestsellers")
        print("Response text:", response.text)
        print("Response status code:", response.status_code)
        print("Response Headers:", response.headers)

    @task
    def get_second_request(self):
        response = self.client.get("/gp/new-releases/?ref_=nav_cs_newreleases")
        print("Response text:", response.text)
        print("Response status code:", response.status_code)
        print("Response Headers:", response.headers)

    @task(2)
    def get_third_request(self):
        response = self.client.get("/gp/browse.html?node=12466553031&ref_=nav_cs_fashion")
        print("Response text:", response.text)
        print("Response status code:", response.status_code)
        print("Response Headers:", response.headers)
