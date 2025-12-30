import streamlit as st
import requests
import json

API_KEY = st.secrets["GEMINI_API_KEY"]

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

        url = (
            "https://generativelanguage.googleapis.com/v1beta/"
            "models/gemini-1.0-pro:generateContent"
            f"?key={API_KEY}"
        )

        payload = {
            "contents": [
                {
                    "parts": [
                        {"text": prompt}
                    ]
                }
            ]
        }

        headers = {"Content-Type": "application/json"}

        response = requests.post(url, headers=headers, data=json.dumps(payload))

        if response.status_code != 200:
            st.error(response.text)
        else:
            output = response.json()["candidates"][0]["content"]["parts"][0]["text"]
            st.text(output)
