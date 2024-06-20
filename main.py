import streamlit as st

st.set_page_config(layout='wide')

col1, col2 = st.columns(2)

with col1:
    st.image('images/photo.png')

with col2:
    st.title('Sean Vela')

    content = """
    Hi, I am Sean Vela! I am a junior software engineer transitioning from a career in mechanical engineering to software engineering, with a strong skill set in building scalable solutions and optimizing code for efficiency and reliability. Committed to tackling complex technical challenges and delivering high-quality software solutions. Proficient in multiple programming languages and frameworks. I am passionate about continuous learning and contributing to a team.
    
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
    Below you can find some apps that I have built in Python and Javascript. Feel free to contact me!
    </div>
    """

    # Render the custom CSS and HTML content in Streamlit
    st.markdown(custom_css, unsafe_allow_html=True)
    st.markdown(content2, unsafe_allow_html=True)
