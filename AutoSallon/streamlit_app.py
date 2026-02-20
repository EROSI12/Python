import base64
import os
from pathlib import Path

import pandas as pd
import requests
import streamlit as st

API_BASE = os.getenv("API_BASE", "http://127.0.0.1:8000").rstrip("/")
BACKGROUND_IMAGE = Path(os.getenv("APP_BG_IMAGE", "static/car-bg.jpg"))
DEFAULT_BG_URL = "https://images.unsplash.com/photo-1494976388531-d1058494cdd8?auto=format&fit=crop&w=1950&q=80"


def _build_background_css() -> str:
    if BACKGROUND_IMAGE.exists():
        encoded = base64.b64encode(BACKGROUND_IMAGE.read_bytes()).decode("ascii")
        return (
            "linear-gradient(rgba(6, 8, 12, 0.62), rgba(6, 8, 12, 0.62)), "
            f"url('data:image/jpeg;base64,{encoded}')"
        )
    return (
        "linear-gradient(rgba(6, 8, 12, 0.62), rgba(6, 8, 12, 0.62)), "
        f"url('{DEFAULT_BG_URL}')"
    )


st.set_page_config(page_title="AutoSallon | Car Inventory", page_icon=":car:", layout="wide")

st.markdown(
    f"""
    <style>
    .stApp {{
        background: {_build_background_css()};
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }}
    .title {{
        font-size: 2.3rem;
        font-weight: 800;
        color: #f4f7fb;
        margin-bottom: 0.2rem;
        text-shadow: 0 2px 8px rgba(0, 0, 0, 0.45);
    }}
    .subtitle {{
        color: #dce6f2;
        margin-bottom: 1rem;
        text-shadow: 0 1px 6px rgba(0, 0, 0, 0.4);
    }}
    .card {{
        background: rgba(255, 255, 255, 0.8);
        border: 1px solid rgba(19, 49, 92, 0.15);
        border-radius: 14px;
        padding: 14px;
    }}
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown('<div class="title">AutoSallon Dashboard</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Browse inventory, track prices, and add new arrivals.</div>', unsafe_allow_html=True)


def _json_or_error(resp: requests.Response) -> dict | list:
    try:
        return resp.json()
    except ValueError as exc:
        raise requests.RequestException(
            f"API returned non-JSON from {resp.url}. Make sure FastAPI is running on http://127.0.0.1:8000"
        ) from exc


@st.cache_data(ttl=3)
def get_cars() -> list[dict]:
    resp = requests.get(f"{API_BASE}/cars", timeout=5)
    resp.raise_for_status()
    return _json_or_error(resp)


@st.cache_data(ttl=3)
def get_summary() -> dict:
    resp = requests.get(f"{API_BASE}/summary", timeout=5)
    resp.raise_for_status()
    return _json_or_error(resp)


col1, col2 = st.columns([2, 1])

with col1:
    st.markdown("### Add New Car")
    with st.form("add_car_form", clear_on_submit=True):
        c1, c2 = st.columns(2)
        brand = c1.text_input("Brand", placeholder="Toyota")
        model = c2.text_input("Model", placeholder="Corolla")
        c3, c4 = st.columns(2)
        year = c3.number_input("Year", min_value=1980, max_value=2100, value=2024)
        price = c4.number_input("Price (USD)", min_value=1000.0, value=25000.0, step=500.0)
        submitted = st.form_submit_button("Save Car")

    if submitted:
        try:
            payload = {
                "brand": brand.strip(),
                "model": model.strip(),
                "year": int(year),
                "price": float(price),
            }
            res = requests.post(f"{API_BASE}/cars", json=payload, timeout=5)
            if res.status_code >= 400:
                st.error(f"Failed: {res.text}")
            else:
                st.success("Car saved")
                st.cache_data.clear()
                st.rerun()
        except requests.RequestException as exc:
            st.error(f"API not reachable: {exc}")

with col2:
    st.markdown("### Summary")
    try:
        s = get_summary()
        st.metric("Total Cars", s.get("total_cars", 0))
        st.metric("Avg Price", f"${s.get('average_price', 0):,.2f}")
        st.metric("Newest Year", s.get("newest_year", 0))
    except requests.RequestException as exc:
        st.error(f"Cannot load summary: {exc}")

st.markdown("### Inventory")
try:
    cars = get_cars()
    if not cars:
        st.info("No cars in inventory yet.")
    else:
        df = pd.DataFrame(cars)
        st.dataframe(df, use_container_width=True, hide_index=True)

        by_brand = df.groupby("brand", as_index=False)["price"].mean().sort_values("price", ascending=False)
        st.markdown("### Average Price by Brand")
        st.bar_chart(by_brand, x="brand", y="price", use_container_width=True)
except requests.RequestException as exc:
    st.error(f"Cannot load cars: {exc}")
