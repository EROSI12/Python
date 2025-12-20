from datetime import datetime
import plotly.express as px
from dotenv import load_dotenv
import os
import requests
import streamlit as st

load_dotenv()

BASE_URL = os.getenv("BASE_URL")

api_key_input = st.text_input("Enter API Key", type="password")


def validate_api_key(api_key):
    headers = {"api-key": api_key}
    response = requests.get(
        url=f"{BASE_URL}/validate_key/",
        headers=headers
    )
    return response.status_code == 200


def add_author(api_key, name):
    headers = {"api-key": api_key}
    response = requests.post(
        url=f"{BASE_URL}/authors/",
        json={"name": name},
        headers=headers
    )

    if response.status_code == 200:
        st.success(f"Author '{name}' added successfully!")
    else:
        st.error(
            f"Failed to add author: "
            f"{response.json().get('detail', 'Unknown error')}"
        )


def update_author(api_key, author_id, name):
    headers = {"api-key": api_key}
    response = requests.put(
        url=f"{BASE_URL}/authors/{author_id}",
        json={"name": name},
        headers=headers
    )

    if response.status_code == 200:
        st.success(f"Author '{name}' updated successfully!")
    else:
        st.error(
            f"Failed to update author: "
            f"{response.json().get('detail', 'Unknown error')}"
        )


def delete_author(api_key, author_id):
    headers = {"api-key": api_key}
    response = requests.delete(
        url=f"{BASE_URL}/authors/{author_id}",
        headers=headers
    )

    if response.status_code == 200:
        st.success("Author deleted successfully!")
    else:
        st.error(
            f"Failed to delete author: "
            f"{response.json().get('detail', 'Unknown error')}"
        )
