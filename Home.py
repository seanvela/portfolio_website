import streamlit as st
import pandas
import os

st.set_page_config(layout='wide')

col1, col2 = st.columns(2)

with col1:
    st.image('images/photo.png')

with col2:
    st.title('Sean Vela')

    content = """
    Hi, I am Sean Vela! I am a junior software engineer focused on backend development,  transitioning from a career in mechanical engineering to software engineering, with a strong skill set in building scalable solutions and optimizing code for efficiency and reliability. Committed to tackling complex technical challenges and delivering high-quality software solutions. I am proficient in multiple programming languages and frameworks. I am passionate about continuous learning and contributing to a team.
    
    I hold a Bachelor of Science in Mechanical Engineering and have recently obtained a Full Stack Development certification from the University of Texas at Austin. My diverse educational background equips me with a unique blend of analytical and technical skills, enabling me to build efficient and innovative software solutions."""

    st.info(content)

    # Custom CSS for the info bubble
    custom_css = """
    <style>
    .info-bubble {
        background-color: #DFF0D8;
        color: #3C763D; /* Text color */
        padding: 10px;
        border-radius: 5px;
        border: 1px solid #ccc;
    }
    </style>
    """

    # HTML content with the custom class
    content2 = """
    <div class="info-bubble">
    Below you can find some apps that I have built. Feel free to contact me!
    </div>
    """

    # Render the custom CSS and HTML content in Streamlit
    st.markdown(custom_css, unsafe_allow_html=True)
    st.markdown(content2, unsafe_allow_html=True)

    # contact information
    st.header('Get in Touch')
    st.write("""
    Click the links below!
    """)

    # Email, GitHub, and LinkedIn links with icons
    st.markdown("""
    <div style="display: flex; justify-content: space-around;">
        <a href="https://www.linkedin.com/in/seanvela1514" target="_blank">
            <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/ca/LinkedIn_logo_initials.png/480px-LinkedIn_logo_initials.png" alt="LinkedIn" style="width:60px;height:60px;">
        </a>     
        <a href="https://github.com/seanvela" target="_blank">
            <img src="https://img.icons8.com/ios-glyphs/50/000000/github.png" alt="GitHub" style="width:60px;height:60px;">
        </a>
    </div>
    """, unsafe_allow_html=True)


col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])

df = pandas.read_csv('data.csv', sep=';')
with col3:
    for index, row in df[:8].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source code]({row['url']})")

with col4:
    for index, row in df[8:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source code]({row['url']})")