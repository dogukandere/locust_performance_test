from locust import task, constant, HttpUser, TaskSet, between, constant_pacing


class FirstTest(HttpUser):
    host = "https://reqres.in"
    #wait_time = constant(1)
    wait_time = between(1, 5)  #1 ila 5 saniye arasında random bir değer bekler
    # wait_time = constant_pacing(3) metotun gerçekleşme süresi 3 saniyeden az ise 3 saniyede bir, 3 saniyeden fazla
    # ise metot süresi kadar bekler
    weight = 2

    def on_start(self):
        print("start settings")

    @task
    def get_users(self):
        response = self.client.get("/api/users?page=2")
        print("Response text:", response.text)
        print("Response status code:", response.status_code)
        #print("Response Headers:", response.headers)

    @task(2)
    def create_user(self):
        response = self.client.post("/api/users", data='''
        { "name": "morpheus","job": "leader"}''')
        print("Response text:", response.text)
        print("Response status code:", response.status_code)
        #print("Response Headers:", response.headers)
