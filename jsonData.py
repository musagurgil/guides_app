import json

data ='{"firstName":"Musa","lastName":"Gürgil"}'

y = json.loads(data)

print(y["firstName"])

customer = {
    "firstName": "Musa",
    "lastName": "Gürgil",
    "age": "26",
    "email": "musagurgil@gmail.com",
}
customerJson = json.dumps(customer)
print(customer)

