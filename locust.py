
import time
from locust import HttpUser, task, between, TaskSet


# class WebsiteUser(HttpUser):
#     wait_time = between(1, 5)

#     # @task
#     # def index_page(self):
#     #     self.client.get(url="/view")

#     @task
#     def uuid_gen(self):
#         self.client.get(url="/api/uuid")

    
class Test_1(TaskSet):
    @task(1)
    def bubblesort_post(self):
        response = self.client.post("/api/bubblesort", json=
        {
        "numbers_to_sort": [2154, 3845, 4141, 8050, 1106, 4285, 1067, 7663, 823, 7363, 8443, 434, 5016, 3, 55],
        "save_in_db": 0
        }
        )
        json_var = response.json()
        number_of_elements = json_var['number_of_elements']
        print( json_var + ' Post title is ' + number_of_elements)