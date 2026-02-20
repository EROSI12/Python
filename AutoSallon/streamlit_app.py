import requests
import pandas as pd
import streamlit as st

API_BASE = "http://127.0.0.1:8000"

st.set_page_config(page_title="AutoSallon Dashboard", page_icon="🚗", layout="wide")

st.markdown(
    """
    <style>
    .stApp {
        background: radial-gradient(circle at 10% 20%, #fdf6e3 0%, #e6f4ea 45%, #dceeff 100%);
    }
    .title {
        font-size: 2.3rem;
        font-weight: 800;
        color: #13315c;
        margin-bottom: 0.2rem;
    }
    .subtitle {
        color: #4f5d75;
        margin-bottom: 1rem;
    }
    .card {
        background: rgba(255, 255, 255, 0.8);
        border: 1px solid rgba(19, 49, 92, 0.15);
        border-radius: 14px;
        padding: 14px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown('<div class="title">AutoSallon</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Car inventory dashboard powered by Streamlit + FastAPI + SQLite</div>', unsafe_allow_html=True)


@st.cache_data(ttl=3)
def get_cars() -> list[dict]:
    resp = requests.get(f"{API_BASE}/cars", timeout=5)
    resp.raise_for_status()
    return resp.json()


@st.cache_data(ttl=3)
def get_summary() -> dict:
    resp = requests.get(f"{API_BASE}/summary", timeout=5)
    resp.raise_for_status()
    return resp.json()


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
