import streamlit as st

st.title("Instructions")
st.write(":book: In this experiment, you will read **3** short statements about past experiences. Each statement is either truthful :white_check_mark: or deceptive :lying_face:. The statements have been shortened and might at times end aprubtly.")
st.write("Apart from the statements, we provide you with the predictions of a state-of-the-art lie detection algorithm based on artificial intelligence (AI) :robot_face:")
st.write("This shows you whether the AI thinks the statement is a lie or a truth and how confident it is in its classification.")

st.write("Your task is to **paraphrase** these statements. Specifically, your rewrite is meant to make the statement appear opposite in credibility compared to how they were originally classified by the AI.")
st.write("In total you will have **10** attempts per statement to decrease the confidence score of the AI as much as possible. If you manage to change the class (truth or lie) the AI thinks the statement belongs to, you will immediately move on to the next statement.")
st.write("Importantly, your rewrite has to maintain the original meaning, be grammatically correct, and appear natural. Naturalness is described by fluency, readability, and coherence.")
st.write("**Please note that you should read and rewrite the statements carefully.**")

if st.button("Next"):
    st.switch_page("pages/stepwise_training_page.py")