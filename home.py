import streamlit as st
from datetime import datetime

st.set_page_config(
    page_title="FullstackGPT Home",
    page_icon="🤖",
)
today = datetime.today().strftime("%H:%M:%S")
st.title(today)



st.markdown(
    """
# Hello!

Welcome to my FullstackGPT Portfolio!

Here are the apps I made:

- [ ] [DocumentGPT](/DocumentGPT)
- [ ] [PrivateGPT](/PrivateGPT)
- [ ] [QuizGPT](/QuizGPT)
- [ ] [SiteGPT](/SiteGPT)
- [ ] [MeetingGPT](/MeetingGPT)
- [ ] [InvestorGPT](/InvestorGPT)
"""
)