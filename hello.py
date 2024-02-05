import streamlit as st

# Function to add CSS styling
def set_style():
    st.markdown(
        """
        <style>
            body {
                background-color: #f5f5f5;
            }
            .main {
                max-width: 800px;
                margin: auto;
                padding: 20px;
                background-color: #000000;
                box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
                border-radius: 10px;
            }
            .header {
                color: #4A90E2;
                text-align: center;
                font-size: 2.5em;
                margin-bottom: 20px;
            }
            .subheader {
                color: #333333;
                text-align: center;
                font-size: 1.5em;
                margin-bottom: 30px;
            }
            .section-header {
                color: #4A90E2;
                font-size: 1.8em;
                margin-top: 20px;
                margin-bottom: 10px;
            }
            .project-title {
                color: #333333;
                font-size: 1.5em;
                margin-top: 15px;
                margin-bottom: 10px;
            }
            .contact-info {
                margin-top: 15px;
                margin-bottom: 30px;
            }
            .interests {
                margin-top: 20px;
                margin-bottom: 30px;
            }
            .achievements {
                margin-top: 20px;
                margin-bottom: 30px;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )

# Apply CSS styling
set_style()

# Navigation sidebar
st.sidebar.title("Navigation")
selected_section = st.sidebar.radio("", ["About", "Education", "Experience", "Projects", "Contact"])

# Main content
with st.container():
    # Header
    st.markdown("<h1 class='header'>Piyush Ghante's Portfolio</h1>", unsafe_allow_html=True)
    st.markdown("<p class='subheader'>Aspiring Software Engineer | Data Structures | Machine Learning</p>", unsafe_allow_html=True)

    # About Section
    if selected_section == "About":
        st.write("Welcome to my portfolio! I am an aspiring software engineer with a strong background in data structures and machine learning.")
        st.write("Feel free to explore the other sections to learn more about my education, experience, projects, and how to get in touch.")

    # Education Section
    elif selected_section == "Education":
        st.markdown("<h2 class='section-header'>Education</h2>", unsafe_allow_html=True)
        st.markdown("1. **B. Tech in Artificial Intelligence and Data Science**<br>"
                    "   - *Vishwakarma Institute of Technology, Bibwewadi, Pune*<br>"
                    "   - *Dec 2022, Studying in Third Year*<br>"
                    "   - *CGPA: 8.32*<br><br>"
                    "2. **Diploma in Computer Technology**<br>"
                    "   - *Government Polytechnic, Solapur*<br>"
                    "   - *Aug 2019 - Aug 2022*<br>"
                    "   - *Percentage: 92.40%*",
                    unsafe_allow_html=True)

    # Experience Section
    elif selected_section == "Experience":
        st.markdown("<h2 class='section-header'>Professional Experience</h2>", unsafe_allow_html=True)
        st.markdown("**Web Developer Intern**, Vertex Technosys<br>"
                    "Sep 2021 - Jan 2022<br>"
                    "PHP and SQL<br>"
                    "Worked as a backend developer on Car Booking and Maintenance website. "
                    "Developed the backend in 2 months, resulting in increased user engagement and efficiency.",
                    unsafe_allow_html=True)

    # Projects Section
    elif selected_section == "Projects":
        st.markdown("<h2 class='section-header'>Projects</h2>", unsafe_allow_html=True)
        st.markdown("**Securing Data Image using Advanced Encryption Standard**<br>"
                    "(Python, Encryption Algorithm, Streamlit)<br>"
                    "Implemented a robust encryption and decryption software for data embedded within images, ensuring end-to-end security<br><br>"
                    "**AI Driven Car Suggestion System for Autonomous Car**<br>"
                    "(Deep learning, Python, Streamlit)<br>"
                    "DL model that directs car control operations such as maintaining speed, accelerating, and breaking<br><br>"
                    "**Multiprogramming Operating System Phase 1 & 2**<br>"
                    "(C++, OOP)<br>"
                    "Implementation of Multiprogramming OS using concepts of C++",
                    unsafe_allow_html=True)

    # Contact Section
    elif selected_section == "Contact":
        st.markdown("<h2 class='section-header'>Contact Information</h2>", unsafe_allow_html=True)
        st.markdown("Email: piyush.ghante22@vit.edu<br>"
                    "Mobile: (+91) 7666521197<br>"
                    "LinkedIn: [linkedin.com/in/piyushghante](linkedin.com/in/piyushghante)<br>"
                    "GitHub: [github.com/piyushghante](github.com/piyushghante)<br>"
                    "Address: Pune, Maharashtra",
                    unsafe_allow_html=True)

# Footer
st.markdown("<p style='text-align: center; color: #888888; font-size: 0.8em;'>"
            "Designed with ❤️ using Streamlit | [View on GitHub](https://github.com/piyushghante/portfolio-streamlit)"
            "</p>", unsafe_allow_html=True)
