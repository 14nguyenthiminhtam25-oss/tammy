import streamlit as st

st.set_page_config(page_title="Bạn thân của Tammy 🤓🤡", layout="centered")

st.title("📒 Danh sách bạn thân")

# 1️⃣ Lưu thông tin bạn thân
friends = {
    "Bin": {
        "Tuổi": 12,
        "Sở thích": "Bóng đá",
        "Tính cách": "hài"
    },
    "Mary": {
        "Tuổi": 11,
        "Sở thích": "nói nhảm",
        "Tính cách": "Nhẹ nhàng"
    },
    "Maryie": {
        "Tuổi": 12,
        "Sở thích": "vẻ tranh",
        "Tính cách": "Hòa đồng"
    }
}

# 2️⃣ Chọn tên bạn
name = st.selectbox("👫 Chọn tên một người bạn thân:", friends.keys())

# Hiển thị thông tin
st.subheader("📌 sikidi")
st.write(f"👤 Tên: {name}")
st.write(f"🎂 Tuổi: {friends[name]['Tuổi']}")
st.write(f"⭐ Sở thích: {friends[name]['Sở thích']}")
st.write(f"💖 Tính cách: {friends[name]['Tính cách']}")
