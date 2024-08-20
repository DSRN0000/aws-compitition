import streamlit as st


# 로그인 상태 검사
if not st.session_state.logged_in:
    st.warning("로그인이 필요합니다.")
    st.stop()  # 로그인되지 않은 경우 이후 코드 실행 중지

st.set_page_config(
    page_title="TopTier",
    page_icon="🚩",
)

st.write("# TopTier를 향해 메모하기 🤓🚩🚩 ")


st.markdown(
    """
     완벽한 학습을 위해 탑티어를 이용하세요!

    ### 기능
    - 메모하기
    - 편리한 메모장 검색
    - 완벽한 습득을 위한 AI 학습

"""
)