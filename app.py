import streamlit as st

# Page configuration
st.set_page_config(
    page_title="Letlhogonolo Mothoagae - Portfolio",
    page_icon="👋",
    layout="wide"
)

# Custom CSS for styling
st.markdown("""
    <style>
    .main-header {
        text-align: center;
        padding: 2rem 0;
    }
    .subtitle {
        text-align: center;
        color: #666;
        font-size: 1.2rem;
        margin-bottom: 1rem;
    }
    .intro-text {
        text-align: center;
        font-size: 1.1rem;
        margin-bottom: 2rem;
    }
    .section-header {
        color: #0e75b6;
        margin-top: 2rem;
        margin-bottom: 1rem;
    }
    .profile-views {
        text-align: center;
        margin: 1rem 0;
    }
    </style>
""", unsafe_allow_html=True)

# Header Section
st.markdown("<h1 class='main-header'>Hi 👋, I'm Letlhogonolo Mothoagae</h1>", unsafe_allow_html=True)

st.markdown("""
    <h3 class='subtitle'>
    Final-year BSc Computer Science & Electronics student | Full-Stack Developer | Systems & Automation Builder
    </h3>
""", unsafe_allow_html=True)

st.markdown("""
    <p class='intro-text'>
    I design and build practical digital systems that help businesses operate better — from web platforms and automation workflows to secure, scalable system architectures.
    </p>
""", unsafe_allow_html=True)

st.markdown("""
    <div class='profile-views'>
    <img src="https://komarev.com/ghpvc/?username=iamluckyt&label=Profile%20views&color=0e75b6&style=flat" alt="profile views" />
    </div>
""", unsafe_allow_html=True)

st.markdown("---")

# About Me Section
st.markdown("### 👨‍💻 About Me")

col1, col2 = st.columns([1, 2])

with col2:
    st.markdown("""
    - 🎓 Final-year **BSc Computer Science & Electronics** student (South Africa)
    - 🏗️ Founder & Developer at **Plug Connect Solutions** — a digital solutions and systems development initiative
    - 🔍 Strong interest in **Full-Stack Development, Cybersecurity Awareness, Cloud Computing, Networks, and Business Automation**
    - 🧠 I focus on **how systems work end-to-end**, not just writing code
    - 🏆 Actively building **competition-ready and client-ready prototypes**
    """)

st.markdown("---")

# Current Focus Section
st.markdown("### 🚀 Current Focus")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    **🔭 Building and scaling Plug Connect Solutions**
    
    A software-focused initiative delivering:
    - Web & App Development
    - Business Systems & Dashboards
    - Automation & AI-assisted workflows
    - Digital presence & social media systems
    """)

with col2:
    st.markdown("""
    **🌱 Deepening skills in:**
    - Full-Stack Web Development
    - System architecture & integration
    - Secure-by-design thinking
    - Real-world project delivery
    """)

st.markdown("---")

# What I Bring Section
st.markdown("### 🧩 What I Bring to Teams & Clients")

st.markdown("""
- Ability to translate **business needs into technical systems**
- Strong foundation in **networks, databases, and system logic**
- Hands-on experience with **real projects**, not just coursework
- Clear communication — I can **explain what I build and why**
- Entrepreneurial mindset with a focus on **scalability and impact**
""")

st.markdown("---")

# Projects & Portfolio Section
st.markdown("### 📂 Projects & Portfolio")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    **👨‍💻 All projects:**
    
    👉 [github.com/IamLuckyT](https://github.com/IamLuckyT)
    """)

with col2:
    st.markdown("""
    **🏗️ Organization work:**
    
    👉 [Plug Connect Solutions](https://github.com/plug-connect-solutions)
    """)

st.info("Projects include system prototypes, business-focused platforms, and experimental solutions aligned with real-world use cases.")

st.markdown("---")

# Ask Me About Section
st.markdown("### 💬 Ask Me About")

topics = [
    "HTML, CSS, JavaScript",
    "Full-Stack fundamentals",
    "Networks & system communication",
    "Business automation concepts",
    "Social media systems for brands & startups"
]

cols = st.columns(3)
for idx, topic in enumerate(topics):
    with cols[idx % 3]:
        st.markdown(f"- {topic}")

st.markdown("---")

# Connect With Me Section
st.markdown("### 🤝 Connect With Me")

col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    st.markdown("""
    <p align="center">
    <a href="https://linkedin.com/in/letlhogonolo-mothoagae" target="_blank">
    <img src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/linked-in-alt.svg" height="30" width="40" />
    LinkedIn
    </a>
    &nbsp;&nbsp;&nbsp;&nbsp;
    <a href="https://fb.com/letlhogonolo.mothoagae" target="_blank">
    <img src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/facebook.svg" height="30" width="40" />
    Facebook
    </a>
    </p>
    """, unsafe_allow_html=True)

st.markdown("---")

# Languages & Tools Section
st.markdown("### 🛠️ Languages & Tools")

tools = [
    ("HTML5", "https://raw.githubusercontent.com/devicons/devicon/master/icons/html5/html5-original-wordmark.svg"),
    ("CSS3", "https://raw.githubusercontent.com/devicons/devicon/master/icons/css3/css3-original-wordmark.svg"),
    ("JavaScript", "https://raw.githubusercontent.com/devicons/devicon/master/icons/javascript/javascript-original.svg"),
    ("Python", "https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg"),
    ("TypeScript", "https://raw.githubusercontent.com/devicons/devicon/master/icons/typescript/typescript-original.svg"),
    ("Vite", "https://raw.githubusercontent.com/devicons/devicon/master/icons/vite/vite-original.svg"),
    ("Java", "https://raw.githubusercontent.com/devicons/devicon/master/icons/java/java-original.svg"),
    ("MySQL", "https://raw.githubusercontent.com/devicons/devicon/master/icons/mysql/mysql-original-wordmark.svg"),
    ("Git", "https://www.vectorlogo.zone/logos/git-scm/git-scm-icon.svg")
]

cols = st.columns(9)
for idx, (name, icon_url) in enumerate(tools):
    with cols[idx]:
        st.markdown(f"""
            <div style="text-align: center;">
            <img src="{icon_url}" width="40" height="40" title="{name}"/>
            </div>
        """, unsafe_allow_html=True)

st.markdown("---")

# Fun Fact Section
st.markdown("### ⚡ Fun fact")
st.info("Beyond coding, I enjoy **project planning, system design, and building ideas that can realistically turn into businesses.**")

# Footer
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #666;'>Built with Streamlit 🎈</p>", unsafe_allow_html=True)
