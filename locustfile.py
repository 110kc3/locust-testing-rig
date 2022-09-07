
import time
from locust import HttpUser, User,task,between


data_to_sort = []
with open('1k_numbers.txt') as f:
    for line in f:
        # inner_list = [elt.strip() for elt in line.split(',')]
        # in alternative, if you need to use the file content as numbers
        inner_list = [int(elt.strip()) for elt in line.split(',')]
        data_to_sort = inner_list

# print(len(data_to_sort))
# print(type(data_to_sort))
# print(str(data_to_sort))

class User(HttpUser):
    # task_set=[bubblesort_post]
    wait_time = between(5, 10)
    host="http://34.118.0.152:8080"


    @task
    def bubblesort_post(self):
      count = 0
      data={
        "numbers_to_sort": data_to_sort,
        "save_in_db": 0 }
      response= self.client.post("/api/bubblesort", json=data)
      file = 'test.txt'.format(count+1)
      with open(file, 'ab') as f:
            content_to_write = response.json()
            content_to_write = {
              "number_of_elements":content_to_write['number_of_elements'],
              "sorting_algorithm": content_to_write['sorting_algorithm'],
              "time_of_execution (s)" :content_to_write['time_of_execution (s)']}
            print(content_to_write)
            ( f.write(bytes(str(content_to_write), 'utf-8')+bytes("\n", 'utf-8')))
            # f.write(response.content+bytes("\n", 'utf-8'))
            count += 1

  

      # print(response.text)
      # print(response.headers)
      # print(response.status_code)
      # print(response.request.headers)

      # json_var = response.json()
      # number_of_elements = json_var['number_of_elements']
      # print(' Post title is ' +  str(number_of_elements))
      # print(' json_var ' +  str(json_var))




