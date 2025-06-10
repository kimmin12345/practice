import streamlit as st

st.title("👤 이름 확인 웹앱")

# 사용자로부터 이름 입력 받기
name = st.text_input("이름을 입력하세요:")

# 조건문 사용
if name == "홍길동":
   st.success("✅ 반갑습니다, 홍길동님!")
else:
   st.warning("❗ 누구세요?")
