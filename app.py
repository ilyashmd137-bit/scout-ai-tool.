import streamlit as st

st.title( اجعله "المحلل الذكي للإعلانات - V1". ")
st.write("أهلاً بك في أول مشروع لي!")

text = st.text_input("اكتب شيئاً هنا وسأقوم بتحليله:")
if st.button("تحليل"):
    st.write("لقد استلمت نصك يا شريكي: " + text)
