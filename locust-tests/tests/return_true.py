import os
from http import HTTPStatus

from locust import between, HttpUser, task


class ShortenUrlUser(HttpUser):
    wait_time = between(0.01, 0.02)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.target_uri = f"/{os.getenv('URI_RETURN_TRUE')}"

    @task
    def get_api(self):
        headers = {
            "Content-Type": "application/json",
        }

        with self.client.get(
                self.target_uri,
                headers=headers,
                name=self.target_uri,
                catch_response=True,
        ) as response:
            if response.status_code in (HTTPStatus.OK, HTTPStatus.CREATED):
                response.success()
            else:
                response.failure(
                    f"Unexpected status code: {response.status_code}"
                )
