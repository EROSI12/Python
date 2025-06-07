from http.client import responses

from pandas.core.interchange.from_dataframe import primitive_column_to_ndarray
from pyarrow import json_

import  request
from Lesson2.index import person

api_url = "https://127.0.0.1:8000/create_person"

person_data = {"name":"John","age":"30"}

responses = request.post(api_url,json=person_data)

print("Response code:", responses.status_code)
print("Response json:", responses.json())