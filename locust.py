
import time
from locust import HttpUser, task, between


class WebsiteUser(HttpUser):
    wait_time = between(1, 5)

    # @task
    # def index_page(self):
    #     self.client.get(url="/view")

    @task
    def uuid_gen(self):
        self.client.get(url="/api/uuid")