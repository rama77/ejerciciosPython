import requests

response = requests.get("https://gitlab.com/api/v4/users/nanuchi/projects")

my_projects = response.json()


for project in my_projects:
    print (f"Proyect: { project['name'] } - url { project['web_url']}")
