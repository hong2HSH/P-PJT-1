from django.test import TestCase
import requests

# Create your tests here.

print(requests.get("https://api.github.com/events"))
