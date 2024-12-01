from locust import HttpUser, task, between


class FlaskTestUser(HttpUser):
    wait_time = between(1, 3)  # Wait time between tasks (1 to 3 seconds)

    @task
    def hello_world(self):
        self.client.get("/")  # Send a GET request to the root endpoint
