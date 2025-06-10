import streamlit as st
import random
name = st.text_input("이름을 입력하세요:")

# 조건문 사용
if name:
    if name == "홍길동":
        st.success("✅ 반갑습니다, 홍길동님!")
    else:
        st.warning("❗ 누구세요?")
st.set_page_config(page_title="✊✋✌️ 가위바위보 게임", page_icon="🎮")

choices = ['✊ 가위', '✋ 바위', '✌️ 보']
computer_choice = random.choice(choices)

st.title("✊✋✌️ 가위바위보")
st.markdown("컴퓨터와 대결하세요!")

user_choice = st.radio("당신의 선택:", choices)

if st.button("결과 보기 🎲"):
    st.write(f"🖥️ 컴퓨터의 선택: **{computer_choice}**")
    if user_choice == computer_choice:
        st.success("무승부입니다! 😐")
    elif (user_choice == '✊ 가위' and computer_choice == '✌️ 보') or \
         (user_choice == '✋ 바위' and computer_choice == '✊ 가위') or \
         (user_choice == '✌️ 보' and computer_choice == '✋ 바위'):
        st.success("승리! 🎉")
    else:
        st.error("패배! 😭")

