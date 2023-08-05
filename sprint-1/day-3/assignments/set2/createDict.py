sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New York"
}

keys = ["name", "salary"]

extracted_dict = {key: sample_dict[key] for key in keys}

print(extracted_dict)
