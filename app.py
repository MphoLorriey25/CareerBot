import streamlit as st
from PIL import Image

st.set_page_config(page_title="CareerBot 🤖", page_icon="🎓", layout="centered")

# Optional: Add a banner/logo
st.image("assets/banner.png", use_container_width=True)

st.title("🎓 Welcome to CareerBot 🤖")
st.markdown("""
> **Hi there!** I'm your friendly career guide bot.  
> Let's find the best career path for you based on your **interests**, **school subjects**, and **skills**.

✨ Answer the questions below and get personalized career suggestions! ✨
""")

# Step 1: Interests
interest = st.selectbox(
    "🌈 What are you most interested in?",
    ["Choose one", "💻 Technology", "🤝 Helping People", "💼 Business", "🎨 Art & Creativity", "🔬 Science"]
)

# Step 2: School Subject
subject = st.selectbox(
    "📚 What was your favorite subject in school?",
    ["Choose one", "➗ Maths", "🧬 Life Sciences", "💰 Economics", "📝 Languages", "🎭 Creative Arts"]
)

# Step 3: Skills
skill = st.selectbox(
    "🧠 What are you good at?",
    ["Choose one", "🧩 Problem-Solving", "🗣️ Communication", "🎨 Creativity", "🧭 Leadership", "🛠️ Technical Skills"]
)

# Submit and show results
if st.button("🎯 Show My Career Suggestions"):
    if "Choose one" in [interest, subject, skill]:
        st.warning("⚠️ Please answer all 3 questions to continue.")
    else:
        st.subheader("🌟 Career Suggestions for You")

        if skill == "🧩 Problem-Solving":
            st.markdown("""
            - 💻 **Software Developer** – Build apps, websites, and systems.  
            - 📊 **Data Analyst** – Interpret data to make smart decisions.  
            - 🤖 **AI Engineer** – Design intelligent systems and chatbots.
            """)
        elif skill == "🗣️ Communication":
            st.markdown("""
            - 🧠 **Psychologist** – Help people manage mental health and emotions.  
            - 👩‍🏫 **Teacher** – Educate and inspire learners.  
            - 👥 **HR Specialist** – Manage workplace relationships and talent.
            """)
        elif skill == "🎨 Creativity":
            st.markdown("""
            - 🎨 **Graphic Designer** – Create visual content and branding.  
            - 📸 **Content Creator** – Make videos, blogs, or social content.  
            - 🖌️ **Animator** – Bring characters and stories to life.
            """)
        elif skill == "🧭 Leadership":
            st.markdown("""
            - 💼 **Entrepreneur** – Start and grow your own business.  
            - 📂 **Project Manager** – Plan and lead teams to success.  
            - 📣 **Marketing Manager** – Promote products to the right audience.
            """)
        elif skill == "🛠️ Technical Skills":
            st.markdown("""
            - 🏗️ **Engineer** – Solve problems using science and technology.  
            - 🖥️ **IT Technician** – Maintain and fix computer systems.  
            - 🤖 **Robotics Specialist** – Build and program smart machines.
            """)

        st.success("✅ These are great careers to research further or ask a mentor about!")
        st.balloons()

st.markdown("---")
st.caption("Made with ❤️ by Mpho Ndou | Built using Streamlit")
