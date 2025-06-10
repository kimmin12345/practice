import streamlit as st
import random

# Streamlit 기본 설정
st.set_page_config(page_title="🌟 오늘의 점심 메뉴 추천기!", page_icon="🍽️", layout="centered")

# 점심 메뉴 리스트 (이모지 포함)
menus = [
    ("🍣 스시", "신선한 생선과 고소한 밥의 환상적인 조화!"),
    ("🍜 라멘", "진한 육수와 쫄깃한 면발이 어우러진 일본식 라멘!"),
    ("🍔 햄버거", "두툼한 패티와 고소한 번! 먹는 순간 행복!"),
    ("🍛 카레라이스", "매콤하고 진한 소스와 따뜻한 밥의 완벽 조화!"),
    ("🥟 군만두", "겉은 바삭, 속은 촉촉한 만두!"),
    ("🍗 치킨", "누구나 사랑하는 바삭바삭한 치킨!"),
    ("🍕 피자", "치즈가 쭉~ 늘어나는 따뜻한 피자 한 조각!"),
    ("🍱 한식 도시락", "따뜻한 밥과 반찬이 가득한 한국식 도시락!"),
    ("🍜 짬뽕", "얼큰한 국물에 해산물이 가득!"),
    ("🥗 샐러드", "가볍고 건강하게! 신선한 샐러드로 상큼하게~")
]

# 헤더 영역
st.markdown(
    """
    <h1 style='text-align: center; color: #ff4b4b;'>✨ 오늘 점심 뭐 먹지? ✨</h1>
    <h3 style='text-align: center;'>🎲 버튼을 눌러 당신의 점심 운명을 정해보세요! 🎲</h3>
    """,
    unsafe_allow_html=True
)

st.markdown("---")

# 추천 버튼
if st.button("👉 오늘의 메뉴 추천 받기!"):
    menu, desc = random.choice(menus)
    st.markdown(
        f"""
        <div style='text-align: center;'>
            <h2 style='font-size: 48px;'>{menu}</h2>
            <p style='font-size: 20px; color: #6c6c6c;'>{desc}</p>
            <p style='font-size: 80px;'>😋🍽️💖</p>
        </div>
        """,
        unsafe_allow_html=True
    )
else:
    st.markdown(
        "<p style='text-align: center; font-size: 24px;'>아직 추천을 받지 않았어요! 🍽️</p>",
        unsafe_allow_html=True
    )

# 푸터
st.markdown("---")
st.markdown(
    "<p style='text-align: center; color: #888;'>🧠 Powered by Streamlit | Made with ❤️ by 점심요정</p>",
    unsafe_allow_html=True
)
