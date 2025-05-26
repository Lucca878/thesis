import streamlit as st
from streamlit.components.v1 import html

st.title("Main Task")
st.write("You are now about to start the main task. Here is a reap of key points:")

st.markdown(
    """
    - **Understand the Task**: Your goal is to paraphrase statements to lower the AI's confidence score so that it changes the predicted class (truthful or deceptive).
    - **Maintain Meaning**: Ensure your paraphrases preserve the original meaning of the statement.
    - **Use of Language**: Use natural and grammatically correct language to rewrite the statements.
    - **Attempts to Modify the Statement**: You can obtain AI feedback by submitting your statement. In the main task, you have 10 attempts per statement.
    """
)
st.write("**IMPORTANT**: Please do not use any outside tools (e.g., Google, ChatGPT) to assist you in this task. This study is a test of your own ability.")


if st.button("Next"):
    st.switch_page("pages/experiment_intro_1_page.py")

# Define your javascript
my_js = """
alert("Refreshing or navigating away throughout the study will cause you to lose your progress. Only use the buttons provided in the app to continue.");
"""

# Wrap the javascript as html code
my_html = f"<script>{my_js}</script>"

html(my_html)