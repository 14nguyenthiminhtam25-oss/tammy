import streamlit as st

st.title("📝 Đăng ký tài khoản")

progress = 0
bar = st.progress(progress)

if st.text_input("👤 Tài khoản"):
    progress += 20
    bar.progress(progress)

if st.text_input("🔒 Mật khẩu", type="password"):
    progress += 20
    bar.progress(progress)

if st.text_input("🔁 Nhập lại mật khẩu", type="password"):
    progress += 20
    bar.progress(progress)

if st.text_input("📛 Tên người dùng"):
    progress += 20
    bar.progress(progress)

if st.text_input("📧 Email"):
    progress += 20
    bar.progress(progress)

if st.button("🚀 Đăng ký") and progress == 100:
    st.success("🎉 Đăng ký thành công!")
    st.balloons()
