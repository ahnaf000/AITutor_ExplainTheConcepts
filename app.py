import streamlit as st
from explain_the_concepts_new import process_chains  

# Load environment variables, API key, and initialize your models here

# Streamlit interface
st.title("AI Tutor for Data Analytics")

# Input fields
topic = st.text_input("Topic", "p-values")
background = st.text_input("Background", "Software Engineering")
name = st.text_input("Name", "Raj")
course = st.text_input("Course", "Data Analytics")
course_expertise = st.selectbox("Course Expertise", ["Novice", "Intermediate", "Advanced"])

# # # Button to start processing
# if st.button("Start Tutoring Session"):
#     print("Hi")
# #     # Call the process_chains function
#     for response in process_chains(topic, background, name, course, course_expertise):
#         # Display each response
#         st.write(response)
if st.button("Start Tutoring Session"):
    # Initialize a placeholder for the first section
    first_section_placeholder = st.empty()

    # Display a loading sign until the first output is returned
    with first_section_placeholder.container():
        with st.spinner('Processing the first section...'):
            responses = process_chains()
            
            # Get the first response
            first_response = next(responses)
            
            # Once the first response is ready, display it in the first expanded section
            with st.expander(f"Section 1: Introduction", expanded=True):
                st.markdown(first_response)

    # Counter to keep track of the other responses
    response_counter = 1  # Starts from 1 as we've already processed the first response


    for response in responses:
        response_counter += 1

        # Set the title for each subsection
        subsection_title = f"Section {response_counter}: " + ("Introduction" if response_counter == 1 else "Key Concepts" if response_counter == 2 else "Application" if response_counter == 3 else "Example" if response_counter == 4 else "Analysis" if response_counter == 5 else "Visualization")

        # Use an expander for each subsection. The first one is expanded by default.
        with st.expander(subsection_title, expanded=(response_counter == 1)):
            st.markdown(response)

        # Show a loading sign for the next section until it's loaded
        if response_counter < 6:  # Assuming there are 6 responses
            with st.spinner(f'Loading {subsection_title}...'):
                pass