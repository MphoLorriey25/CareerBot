import streamlit as st
from PIL import Image

# Page config
st.set_page_config(page_title="CareerBot 🤖", page_icon="🎓", layout="centered")

# Optional: Rounded banner
banner = Image.open("assets/banner.png")
st.image(banner, use_column_width=True)

# Welcome Section with stylized bubble
with st.container():
    st.markdown("""
    <div style="background-color:#FFF7E6;padding:20px;border-radius:15px;text-align:center;border: 1px solid #F0D9B5;">
        <h2>👋 Hi there! I'm <b>CareerBot</b> 🤖</h2>
        <p>I'm here to help you explore exciting career paths based on your:</p>
        <ul style="text-align:left">
            <li>🌈 Interests</li>
            <li>📘 Favorite Subjects</li>
            <li>💡 Strengths & Skills</li>
        </ul>
        <p>Let’s get started! 🚀</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("### 💬 Let's Chat!")

# Question 1: Interests
with st.container():
    interest = st.selectbox(
        "🌈 What are you most interested in?",
        ["Choose one", "💻 Technology", "🤝 Helping People", "💼 Business", "🎨 Art & Creativity", "🔬 Science"]
    )

# Question 2: School Subject
with st.container():
    subject = st.selectbox(
        "📚 What was your favorite subject in school?",
        ["Choose one", "➗ Maths", "🧬 Life Sciences", "💰 Economics", "📝 Languages", "🎭 Creative Arts"]
    )

# Question 3: Skills
with st.container():
    skill = st.selectbox(
        "🧠 What are you good at?",
        ["Choose one", "🧩 Problem-Solving", "🗣️ Communication", "🎨 Creativity", "🧭 Leadership", "🛠️ Technical Skills"]
    )

# Result Section
if st.button("🎯 Show My Career Suggestions"):
    if "Choose one" in [interest, subject, skill]:
        st.warning("⚠️ Please answer all 3 questions to get your results.")
    else:
        st.markdown("## 🌟 Career Suggestions for You")

        with st.container():
            if skill == "🧩 Problem-Solving":
                st.markdown("""
                <div style="background-color:#eaf6ff;padding:15px;border-radius:10px;">
                    <b>💻 Software Developer</b> – Build apps, websites, and systems.<br>
                    <b>📊 Data Analyst</b> – Interpret data to make smart decisions.<br>
                    <b>🤖 AI Engineer</b> – Design intelligent systems and chatbots.
                </div>
                """, unsafe_allow_html=True)

            elif skill == "🗣️ Communication":
                st.markdown("""
                <div style="background-color:#fff0f5;padding:15px;border-radius:10px;">
                    <b>🧠 Psychologist</b> – Help people manage mental health.<br>
                    <b>👩‍🏫 Teacher</b> – Educate and inspire learners.<br>
                    <b>👥 HR Specialist</b> – Manage workplace talent and people.
                </div>
                """, unsafe_allow_html=True)

            elif skill == "🎨 Creativity":
                st.markdown("""
                <div style="background-color:#f0fff4;padding:15px;border-radius:10px;">
                    <b>🎨 Graphic Designer</b> – Create visual content.<br>
                    <b>📸 Content Creator</b> – Produce blogs, videos, or social media.<br>
                    <b>🖌️ Animator</b> – Bring stories and visuals to life.
                </div>
                """, unsafe_allow_html=True)

            elif skill == "🧭 Leadership":
                st.markdown("""
                <div style="background-color:#fffaf0;padding:15px;border-radius:10px;">
                    <b>💼 Entrepreneur</b> – Launch and manage businesses.<br>
                    <b>📂 Project Manager</b> – Lead and deliver successful projects.<br>
                    <b>📣 Marketing Manager</b> – Strategize and promote products.
                </div>
                """, unsafe_allow_html=True)

            elif skill == "🛠️ Technical Skills":
                st.markdown("""
                <div style="background-color:#f5f5ff;padding:15px;border-radius:10px;">
                    <b>🏗️ Engineer</b> – Use technology to solve real-world problems.<br>
                    <b>🖥️ IT Technician</b> – Maintain and repair tech systems.<br>
                    <b>🤖 Robotics Specialist</b> – Build smart machines and robots.
                </div>
                """, unsafe_allow_html=True)

        st.success("✅ These are great careers to explore further! Talk to a teacher, mentor, or do online research to learn more.")
        st.balloons()

# Footer
st.markdown("---")
st.caption("✨ Built with ❤️ by Mpho Ndou | Powered by Streamlit")
