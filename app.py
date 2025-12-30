import streamlit as st
from openai import OpenAI

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

st.title("Nervous DM Generator")

platform = st.selectbox("Platform", ["Instagram", "LinkedIn"])
business = st.text_input("Business type")
noticed = st.text_area("What did you notice?")

if st.button("Generate DM"):
    if not business or not noticed:
        st.warning("Fill all fields")
    else:
        prompt = f"""
You are NOT an expert.
You are NOT confident.
You are a shy human writing nervous DMs.

Rules:
- No advice
- No explanations
- No strategy words
- No confidence

Context (do not repeat):
Platform: {platform}
Business: {business}
Noticed: {noticed}

Output EXACTLY in this format:

CLIENT TYPE:
(one short line)

WHERE TO FIND THEM:
(one short line)

FIRST DM TO SEND:
(1–2 short nervous sentences, only about what was noticed)

IF THEY REPLY WITH "THANKS":
REPLY TO SEND:
(1 short neutral sentence)

IF THEY REPLY WITH "WHAT DO YOU DO?":
REPLY TO SEND:
(1 vague observational sentence)
"""

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7,
        )

        st.text(response.choices[0].message.content)
