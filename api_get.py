import requests

response = requests.get("https://progressive.me/api")
print(response.status_code)
print(response.json())

gender = response.json(["results"][0]["gender"])
title = response.json(["results"][0]["title"])
first_name = response.json(["results"][0]["first_name"])
last_name = response.json(["results"][0]["last_name"])
age = response.json(["results"][0]["age"])
vehicle = response.json(["results"][0]["registered_vehicle"])
policy_number = response.json(["results"][0]["policy_number"])

print(
    f"This vehicle is registered to: {title}{first_name} {last_name}{age}{vehicle}{policy_number}"
)
print(
    f"This may also be driven by: {title}{first_name} {last_name}{age}{vehicle}{policy_number} "
)
