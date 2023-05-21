import streamlit as st

import datetime

thedate = datetime.date.today()

st.set_page_config(
    page_title="20110298_Đỗ Duy Nhựt",
    page_icon="",
)
with open("style.css") as source_des:
    st.markdown(f"<style>{source_des.read()}</style>", unsafe_allow_html=True)

st.sidebar.success("Chọn bài để chạy ")

st.write("""
    # Đồ án Cuối kỳ Xử lý ảnh số
    """) 

st.markdown(
        """
    ### Giảng viên hướng dẫn: Trần Tiến Đức
    
    
    ------

    #### Sinh viên thực hiện:

    Đỗ Duy Nhựt - 20110298 - Lớp Xử lý ảnh số lớp 08 (T4, tiết 13-15)

    """
    )
st.write("#### Ngày: ", thedate)
