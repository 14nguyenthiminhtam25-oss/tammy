import streamlit as st

st.title("📚 Thư viện cá nhân của Tammy")

st.write("Chào mừng đến với trang web giới thiệu bạn bè, gia đình và người thân của mình 💙")

# ===== HÌNH ẢNH =====
st.header("🖼️ Hình ảnh")
st.image("image.jpg", caption="Hình ảnh gia đình / bạn bè", width=300)

# ===== ÂM THANH =====
st.header("🎵 File ghi âm")
st.audio("audio.mp3", format="audio/mp3")

# ===== VIDEO =====
st.header("🎬 Video")
st.video("video.mp4")
