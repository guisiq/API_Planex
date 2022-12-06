import lorem
from locust import HttpUser, task, between


class WebsiteUser(HttpUser):
    wait_time = between(1, 3)

    @task(1)
    def matrix(self):
        self.client.get('/matrix/2/2')
    
    @task(5)
    def matriTesteT(self):
        self.client.get('/matriTesteT/2/2/\[\[0\]\,\[0\],\[0\],\[0\],\[0\],\[0\]\]')

    @task(2)
    def tabAnova(self):
        self.client.get('/tab_anova/2/2/[[0],[0],[0],[0],[0],[0]]/[[1],[1],[1],[1]]')

