import streamlit as st
from PIL import Image
import cohere
import os
from dotenv import load_dotenv

# Load API key
load_dotenv()
COHERE_API_KEY = os.getenv("COHERE_API_KEY") or "qAp1dlVpeCTkI1KJOyWwpInNQ11hucBLRRJjESyI"
co = cohere.Client(COHERE_API_KEY)

# Page config
st.set_page_config(page_title="CareerBot 🤖", page_icon="🎓", layout="centered")

# --- Header ---
st.image("assets/banner.png", use_container_width=True)
st.title("🎓 CareerBot: Discover Your Path")
st.markdown("Welcome! Take this short quiz to find a career that fits your **personality, interests, and strengths.**")

st.markdown("---")

# --- Section: Personality Quiz ---
st.header("🧠 Step 1: Personality Quiz")

q1 = st.radio("When solving a problem, you usually:", ["Rely on logic", "Talk it through", "Trust your gut"], key="q1")
q2 = st.radio("In a group project, you prefer to:", ["Lead the group", "Support and motivate others", "Do your part quietly"], key="q2")
q3 = st.radio("You are most energized by:", ["Being around people", "Working alone", "A mix of both"], key="q3")
q4 = st.radio("You make decisions based on:", ["Data & facts", "Feelings & values", "Both equally"], key="q4")

# --- Section: Interests ---
st.markdown("---")
st.header("🌈 Step 2: Your Interests & Skills")

interest = st.selectbox("What are you most interested in?", ["Choose one", "💻 Technology", "🤝 Helping People", "💼 Business", "🎨 Art & Creativity", "🔬 Science"])
subject = st.selectbox("What was your favorite subject in school?", ["Choose one", "➗ Maths", "🧬 Life Sciences", "💰 Economics", "📝 Languages", "🎭 Creative Arts"])
skill = st.selectbox("What are you naturally good at?", ["Choose one", "🧩 Problem-Solving", "🗣️ Communication", "🎨 Creativity", "🧭 Leadership", "🛠️ Technical Skills"])

# --- Button ---
st.markdown("---")
if st.button("🎯 Show My Career Path"):
    if "Choose one" in [interest, subject, skill]:
        st.warning("⚠️ Please complete all fields to continue.")
    else:
        st.subheader("🌟 Your AI-Powered Career Suggestions")
        with st.spinner("Generating your personalized career match..."):

            # Create a simple personality profile from answers
            personality = ""
            if q1 == "Rely on logic": personality += "Thinker, "
            if q1 == "Talk it through": personality += "Communicator, "
            if q1 == "Trust your gut": personality += "Intuitive, "

            if q2 == "Lead the group": personality += "Leader, "
            if q2 == "Support and motivate others": personality += "Helper, "
            if q2 == "Do your part quietly": personality += "Independent, "

            if q3 == "Being around people": personality += "Extrovert, "
            if q3 == "Working alone": personality += "Introvert, "
            if q3 == "A mix of both": personality += "Balanced, "

            if q4 == "Data & facts": personality += "Logical"
            if q4 == "Feelings & values": personality += "Empathetic"
            if q4 == "Both equally": personality += "Well-rounded"

            # AI prompt for Cohere
            prompt = f"""
You're an expert career advisor. A student took a short quiz and has this personality profile: {personality}.
Their interests are: {interest}, favorite school subject: {subject}, and skill: {skill}.
Suggest 3–5 career paths with short motivational explanations for each one.
Tone: encouraging, simple, and friendly.
"""

            try:
                response = co.chat(
                    model="command-r",
                    message=prompt,
                    temperature=0.7,
                    max_tokens=300
                )
                st.markdown(response.text.strip())
                st.success("✅ Explore these paths further by researching or asking a mentor.")
                st.balloons()
            except Exception as e:
                st.error(f"❌ Something went wrong: {e}")

# --- Footer ---
st.markdown("---")
st.caption("Made with ❤️ by Tech Avengers | Powered by Streamlit + Cohere AI")

