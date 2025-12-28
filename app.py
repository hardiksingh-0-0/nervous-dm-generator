import streamlit as st
import google.generativeai as genai
import os

# -------------------------
# Gemini setup (Cloud-safe)
# -------------------------
genai.configure(api_key=os.getenv("AIzaSyA9W-TAA3ein_OJ3Eg4_9n62sErMtU3jQo"))
model = genai.GenerativeModel("gemini-1.5-flash")

# -------------------------
# UI
# -------------------------
st.title("Nervous DM Generator")

platform = st.selectbox("Platform", ["Instagram", "LinkedIn"])
business = st.text_input("Business type")
noticed = st.text_area("What did you notice?")

# -------------------------
# Generation
# -------------------------
if st.button("Generate DM"):
    prompt = f"""
SYSTEM ROLE:
You are NOT an expert.
You are NOT confident.
You are a shy, observant human.

ABSOLUTE RULES:
- Do NOT explain
- Do NOT teach
- Do NOT give advice
- Do NOT sound professional

INPUT (do not repeat):
Platform: {platform}
Business type: {business}
What was noticed: {noticed}

TASK:
Generate EXACTLY ONE outreach opportunity.

OUTPUT FORMAT (EXACT — NO EXTRA TEXT):

CLIENT TYPE:
(one short line)

WHERE TO FIND THEM:
(one short line)

FIRST DM TO SEND:
(1–2 short sentences, curious, unsure, only about what was noticed)

IF THEY REPLY WITH "THANKS":
REPLY TO SEND:
(1 short sentence, polite, neutral)

IF THEY REPLY WITH "WHAT DO YOU DO?":
REPLY TO SEND:
(1 short sentence, vague, observational)
"""

    try:
        response = model.generate_content(prompt)
        st.write(response.text)
    except Exception as e:
        st.error("Something went wrong. Please try again in a moment.")
