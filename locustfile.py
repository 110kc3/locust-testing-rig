
from locust import HttpUser, TaskSet,task,between

class UserBehaviour(TaskSet):

    @task
    def bubblesort_post(self):
      response= self.client.post("/api/bubblesort",
      data={
        "numbers_to_sort": [2154, 3845, 4141, 8050, 1106, 4285, 1067, 7663, 823, 7363, 8443, 434, 5016, 3, 55],
        "save_in_db": 0
        })
      print(response.text)
      print(response.headers)
      print(response.status_code)
      print(response.request.headers)

      json_var = response.json()
      number_of_elements = json_var['number_of_elements']
      print( json_var + ' Post title is ' + number_of_elements)



class User(HttpUser):
    task_set=[UserBehaviour]
    wait_time = between(5, 10)
    host="http://34.118.0.152:8080"

