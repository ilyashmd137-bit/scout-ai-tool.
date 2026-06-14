import streamlit as st

st.title("المحلل الذكي للإعلانة)
st.write("أهلاً بك في أول مشروع لي!")

text = st.text_input("اكتب شيئاً هنا وسأقوم بتحليله:")
if st.button("تحليل"):
    st.write("لقد استلمت نصك يا شريكي: " + text)
