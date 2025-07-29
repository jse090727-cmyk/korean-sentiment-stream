import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="대한민국 대학 취업률 계산기", layout="centered")

st.title("🎓 대한민국 대학 취업률 계산기")

st.write("전공별 졸업자 수와 취업자 수를 입력하면 자동으로 취업률을 계산합니다.")

# 사용자 입력
school = st.text_input("학교 이름을 입력하세요", placeholder="예: 서울대학교")
major = st.text_input("전공을 입력하세요", placeholder="예: 컴퓨터공학과")
graduates = st.number_input("졸업자 수", min_value=1, step=1)
employed = st.number_input("취업자 수", min_value=0, step=1, max_value=int(graduates))

# 계산 버튼
if st.button("취업률 계산하기"):
    if employed > graduates:
        st.error("취업자 수는 졸업자 수보다 클 수 없습니다.")
    else:
        rate = (employed / graduates) * 100
        st.success(f"✅ {school} {major}의 취업률은 **{rate:.2f}%** 입니다.")

        # 간단한 시각화
        fig, ax = plt.subplots()
        ax.bar(["취업자", "졸업자"], [employed, graduates], color=["green", "gray"])
        ax.set_ylabel("명")
        ax.set_title("졸업자 vs 취업자")
        st.pyplot(fig)

# 취업률 히스토그램 추가 입력
st.markdown("---")
st.subheader("📊 추가 분석 (여러 학과 입력)")

with st.expander("여러 학과의 데이터를 입력하여 비교해보세요"):
    sample_data = {
        "학교명": ["서울대학교", "연세대학교", "고려대학교"],
        "전공": ["전자공학", "기계공학", "화학공학"],
        "졸업자 수": [100, 120, 90],
        "취업자 수": [85, 90, 70]
    }

    df = st.data_editor(pd.DataFrame(sample_data), use_container_width=True, num_rows="dynamic")

    if st.button("📈 취업률 분석하기"):
        df["취업률(%)"] = (df["취업자 수"] / df["졸업자 수"]) * 100
        st.dataframe(df)

        fig, ax = plt.subplots(figsize=(8, 4))
        ax.barh(df["전공"], df["취업률(%)"], color="skyblue")
        ax.set_xlim(0, 100)
        ax.set_xlabel("취업률 (%)")
        ax.set_title("전공별 취업률")
        st.pyplot(fig)
