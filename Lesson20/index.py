data = {
    "name": "Eros",
    "age": 18,
    "address": {
        "street": "123 street",
        "city": "Prishtina"
    },
    "Contact":[
        {
            "type": "email"
        },
        {
            "type": "phone"
        }
    ]
}
print(data["contact"]["type"])
print(data["contact"][1]["type"])