from locust import HttpUser, task
import os

class QuickstartUser(HttpUser):
    pass

    def on_start(self):
        email = os.getenv("EMAIL")
        password = os.getenv("PASSWORD")
        response = self.client.post(
            "/accounts/api/v2/jwt/create/",
            data={
                "email": email,
                "password": password,
            },
        ).json()
        self.client.headers = {
            "Authorization": f"Bearer {response.get('access', None)}"
        }

    @task
    def post_list(self):
        self.client.get("/blog/api/v1/post/")

    @task
    def category_list(self):
        self.client.get("/blog/api/v1/category/")
