import streamlit as st
from google import genai

client = genai.Client(api_key="AIzaSyDeS3TXtylNjbyhKlbhQqVzpAhJMV-J8po")

st.title("Nervous DM Generator")

platform = st.selectbox("Platform", ["Instagram", "LinkedIn"])
business = st.text_input("Business type")
noticed = st.text_area("What did you notice?")

if st.button("Generate DM"):
    prompt = f"""
You are a text autofill engine.

You do NOT think.
You do NOT analyze.
You do NOT explain.

You ONLY rewrite text to sound like a shy, nervous human.

--------------------------------
INPUT:
Platform: {platform}
Business type: {business}
Observed fact: {noticed}
--------------------------------

TASK:
Fill the template below. Do NOT add extra text.

CLIENT TYPE:
(one short plain line)

WHERE TO FIND THEM:
(one short plain line)

FIRST DM TO SEND:
(1–2 short sentences.
Curious.
Unsure.
Only reference the observed fact.
No advice.
No suggestions.)

IF THEY REPLY WITH "THANKS":
REPLY TO SEND:
(1 short neutral sentence.)

IF THEY REPLY WITH "WHAT DO YOU DO?":
REPLY TO SEND:
(1 vague, observational sentence.
No pitch.
No services.
No confidence.)

STRICT RULES:
- No explanations
- No strategy
- No advice
- No marketing words
- If you break the format, rewrite silently
"""

    response = client.models.generate_content(
        model="models/gemini-flash-latest",
        contents=prompt
    )

    st.write(response.text)
