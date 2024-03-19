from pathlib import Path

import streamlit as st
from PIL import Image



# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "Lahiru Senavirathna CV.pdf"
profile_pic = current_dir / "assets" / "prof-5.png"
#st.image(profile_pic, width=300)
#page_icon = current_dir / "assets" / "pp.png"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Lahiru Senavirathna"
PAGE_ICON = ":technologist:"
NAME = "Lahiru Senavirathna"
DESCRIPTION = """
Mobile App: | Web App: | Software | Developer | You Tuber | Programmer | Associate Software Engineer at SLIBTEC.
"""

EMAIL = "lahirusenavirathna02@gmail.com"


SOCIAL_MEDIA = {
    "YouTube": "https://www.youtube.com/channel/UCEcQ2x422yrxqGAoKZ7s1-Q",
    "LinkedIn": "https://www.linkedin.com/in/lahiru-senavirathna-39b11a215/",
    "GitHub": "https://github.com/SE-LAPS",
    "Facebook": "https://www.facebook.com/CodeShowLapZ?mibextid=ZbWKwL",
    "Twitter": "https://twitter.com/LahiruSenavira5?s=09",
}
PROJECTS = {
    "👨‍💻 A Full-stack Food Ordering Apps made in Flutter with Firebase": "https://youtu.be/PT4ipPYW5Jo?si=fb07Q3iRAAC2R36y",
    "👩‍💻 Point-Of-Sale (POS) Systems For Inventory Management System": "https://youtu.be/TJRgU1c-1rw?si=SuTby5CTOVtQMqWC",
    "👩‍💻 3D Modern Portfolio Web Application ": "https://youtu.be/uj98U-oLDo0?si=dExjVEyQtNfBv_mc",
    "👩‍💻 Responsive Garbage Collection Web-Site": "https://youtu.be/5fubYeKQP94?si=eEWIDx1SlIb-r7xx",
    "👩‍💻 Complete E-Commerce Website Using PHP and MySQL": "https://youtu.be/up_38g5Axms?si=muwnRpcglI1hBkJW",
    "👩‍💻 Blind-Supporter C# .Net Web Application": "https://youtu.be/VMrFU5u0EDQ?si=jVEGp5Yzg5rlNYAu",
    "👩‍💻 Online Food Delivery Management System": "https://youtu.be/Lqom3Fejhuk?si=gEVbB1dmTboGN8Re",
    "👩‍💻 Horizontal Scrolling Astrology Web-Site": "https://youtu.be/eFJxO6jkVrE?si=wecSylhrCO9PZdrD",
    "👩‍💻 Advanced Movie Booking Web Project Design": "https://youtu.be/u57VAUB3f9U?si=IIg6BJQwCdUApZlF",
    "👩‍💻 Simple Sniper Game Project": "https://youtu.be/RKgkkgiTj58?si=26M1-cvmqSST7sFD",
    "👩‍💻 E-Banking System": "https://youtu.be/U0akBKITlyc?si=qQ2msCwvMCDhx_SG",
    "👩‍💻 Construction and Engineering Billing System": "https://youtu.be/2fgYoAyPUcE?si=fBWT9bMaTYT0kRcq",
    "👩‍💻 Simple Sniper Game Project": "https://youtu.be/RKgkkgiTj58?si=haimyjwynfPQfUxW",
}


st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)




# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)


with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    #st.write(DESCRIPTION)
    st.markdown(f"<font color='lightblue'>{DESCRIPTION}<br><br></font>", unsafe_allow_html=True)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL)



# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[ <font color='orange' size='+4'>{platform}</font> ]({link})", unsafe_allow_html=True)


# --- EXPERIENCE & QUALIFICATIONS ---
st.write('\n')
st.subheader("⏩Experience & Qulifications⏪")
st.write("---")
st.write(
    """
-    ✔️ 2+ Years expereince extracting Full-Stack Software Development.
-    ✔️ Proficient understanding of Artificial Intelligent and its diverse applications.
-    ✔️ Good understanding of Machine Learning and their respective applications.
-    ✔️ Excellent team-player and displaying strong sense of initiative on tasks.
-    ✔️ Strong hands on experience and knowledge in Java , Python , Php , Dart and MERN.
-    ✔️ Comprehensive knowledge of trend programming content creation YouTube chanel .
"""
)


# --- SKILLS ---
st.write('\n')
st.subheader("⏩Hard Skills⏪")
st.write("---")
st.write(
    """
-    👩‍💻  <font color='lightgreen'>Programming:</font> Java , Python , C# , C++ , PHP , Dart , MERN,  SQL,
-    📊  <font color='lightgreen'>Data Visulization:</font> Tableau , Matplotlib , Plotly
-    📚  <font color='lightgreen'>Modeling:</font> Python , R , TensorFlow , Pytorch
-    🗄️  <font color='lightgreen'>Databases:</font> Postgres, MongoDB, MySQL , SQLite
"""
, unsafe_allow_html=True)


# --- WORK HISTORY ---
st.write('\n')
st.subheader("⏩Work History⏪")
st.write("---")

# --- JOB 1
st.write("👨‍💻", "**Software Engineer | [<font color='yellow'>Sri Lanka Institute of Biotechnology (SLIBTEC)</font>](https://slibtec.gov.lk/)**", unsafe_allow_html=True)
st.write("-  🔵 December - 2023 ➖ Present")
st.write(
    """
- 🔶 Proficient in multiple programming languages like Python, Java, or C++, adept at designing and developing scalable software solutions.
- 🔶 Expertise in utilizing frameworks such as Django or Spring to streamline the development process and ensure code maintainability.
- 🔶 Strong problem-solving skills, capable of tackling complex technical challenges and optimizing code for performance.
- 🔶 Collaborative team player, effectively communicating with cross-functional teams to deliver high-quality software products.
- 🔶 Continuous learner, staying updated with emerging technologies and best practices to drive innovation in software development.
"""
)

# --- JOB 2
st.write('\n')
st.write("👨‍💻", "**Data Science Enthusiast | [<font color='yellow'>Cognifyz Technologies · Part-time </font>](https://cognifyz.com/)**", unsafe_allow_html=True)
st.write("-  🔵 January - 2024 ➖ Present")
st.write(
    """
- 🔶 Collect, preprocess, and analyze large datasets to extract valuable insights and patterns.
- 🔶 Implement and scale machine learning solutions using programming languages such as Python or R.  
- 🔶 Design and develop machine learning models to address business challenges and enhance decision-making processes.
- 🔶 Stay updated on emerging technologies and best practices to continually improve the performance and efficiency of machine learning systems.
- 🔶 Collaborate with data scientists and software engineers to deploy, maintain, and optimize machine learning algorithms in production environments.

"""
)

# --- JOB 3
st.write('\n')
st.write("👨‍💻", "**Mobile Application Developer | [<font color='yellow'>CodeAlpha · Part-time </font>](https://www.codealpha.tech/)**", unsafe_allow_html=True)
st.write("-  🔵 January - 2024 ➖ Present")
st.write(
    """
- 🔶 Skilled in mobile app development for iOS and Android platforms, utilizing tools like Swift, Kotlin, or React Native to create intuitive user experiences.
- 🔶 Proficiency in optimizing app performance and ensuring compatibility with a variety of devices, screens, and operating systems.
- 🔶 Thorough understanding of platform-specific guidelines and requirements, implementing features that leverage device capabilities effectively.
- 🔶 Collaborative mindset, working closely with UX/UI designers to translate design concepts into functional and visually appealing mobile apps.
- 🔶 Passionate about staying informed on the latest trends and advancements in mobile technology, delivering innovative solutions to meet user needs.
"""
)

# --- JOB 4
st.write('\n')
st.write("👨‍💻", "**Software Engineer | [<font color='yellow'>Prodigy InfoTech · Part-time</font>](https://prodigyinfotech.dev/)**", unsafe_allow_html=True)
st.write("-  🔵 January - 2024 ➖ Present")
st.write(
    """
- 🔶 Proficiency in designing and implementing robust software solutions using languages like Python, Java, or C++, coupled with in-depth knowledge of frameworks like Django or Spring.
- 🔶 Strong analytical and problem-solving skills, capable of optimizing code for performance and scalability to meet business requirements.
- 🔶 Effective communicator and team player, collaborating with diverse teams to deliver high-quality software solutions within specified timelines.
- 🔶 Adaptable and quick learner, staying abreast of emerging technologies and industry trends to drive innovation in software development practices.
- 🔶 Commitment to continuous improvement, actively seeking feedback and refining processes to enhance productivity and deliver value to stakeholders.
"""
)

# --- JOB 5
st.write('\n')
st.write("👨‍💻", "**Full-stack Developer | [<font color='yellow'>Bharat Intern · Part-time</font>](https://bharatintern.live/)**", unsafe_allow_html=True)
st.write("-  🔵 January - 2024 ➖ Present")
st.write(
    """
- 🔶 Proficient in both front-end and back-end development, utilizing technologies like JavaScript, React, Node.js, and databases such as MongoDB or MySQL to create dynamic web applications.
- 🔶 Ability to design and implement responsive and visually appealing user interfaces, ensuring seamless user experiences across devices and platforms.
- 🔶 Strong problem-solving skills, capable of architecting scalable and maintainable software solutions to meet project requirements.
- 🔶 Collaborative mindset, working closely with designers and other stakeholders to ensure alignment between design and development goals.
- 🔶 Passionate about exploring new technologies and methodologies, continuously seeking opportunities to innovate and optimize development processes.
"""
)


# --- JOB 6
st.write('\n')
st.write("👨‍💻", "**YouTuber | [<font color='yellow'>YouTube · Freelance</font>](https://www.youtube.com/channel/UCEcQ2x422yrxqGAoKZ7s1-Q)**", unsafe_allow_html=True)
st.write("-  🔵 January - 2021 ➖ Present")
st.write(
    """
- 🔶 Specializes in creating engaging and informative content, focusing on programming tutorials and technology reviews to educate and entertain viewers.
- 🔶 Proficient in video editing software such as Adobe Premiere Pro or Final Cut Pro, producing high-quality videos with polished visuals and captivating storytelling.
- 🔶 Builds a strong community through active engagement and interaction, fostering a supportive and collaborative environment for viewers.
- 🔶 Tailors content to meet audience interests and needs, delivering valuable insights and practical advice to inspire and empower viewers.
- 🔶 Committed to continuous improvement, refining content creation processes and exploring new topics to keep content fresh and relevant.
"""
)


# --- Projects & Accomplishments ---
st.write('\n')
st.subheader("⏩Projects & Accomplishments⏪")
st.write("---")
for project, link in PROJECTS.items():

    #st.write(f"[{project}]({link})")
    #st.write(f"<font color='lightgreen'>👨‍💻{project}<br></font>🛑 {link}", unsafe_allow_html=True)
    st.write(f"<font color='lightgreen'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;{project}<br></font>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;🛑 {link}",
             unsafe_allow_html=True)

    #st.markdown(f"<font color='blue'>{DESCRIPTION}</font>", unsafe_allow_html=True)

