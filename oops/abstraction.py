from abc import ABC, abstractmethod

import json
from urllib.request import urlopen

class Greet(ABC):
    @abstractmethod
    def say_hello(self):
        pass #abstract method 

class English(Greet):
    def say_hello(self):
        return "hello!"

    def word(self):
        return "how are youu" # concrete method

g = English()
print(g.say_hello())


class ApiClient(ABC):
    @abstractmethod
    def get(self, url):
        pass


class JsonApiClient(ApiClient):
    def get(self, url):
        with urlopen(url, timeout=10) as response:
            return json.loads(response.read().decode("utf-8"))


if __name__ == "__main__":
    client = JsonApiClient()
    post = client.get("https://jsonplaceholder.typicode.com/posts/1")
    print(post)