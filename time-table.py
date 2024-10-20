import streamlit as st
import pandas as pd

# Set the title of the app
st.title('Student Timetable Creator')

# Input the student name
student_name = st.text_input('Enter your name:')

# Input the day of the timetable
day_of_week = st.selectbox('Choose the day of the week:', 
                           ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'])

# Input class details
st.header(f"Enter your classes for {day_of_week}")

# Create a form to input subjects, start time, and end time
class_schedule = []

with st.form(key='timetable_form'):
    subject = st.text_input('Subject')
    start_time = st.time_input('Start Time')
    end_time = st.time_input('End Time')
    
    submit_button = st.form_submit_button(label='Add Class')
    
    if submit_button:
        class_schedule.append({'Subject': subject, 'Start Time': start_time.strftime('%H:%M'), 'End Time': end_time.strftime('%H:%M')})
        st.success(f'Added {subject} from {start_time.strftime("%H:%M")} to {end_time.strftime("%H:%M")}')
    
# Display the timetable
if len(class_schedule) > 0:
    st.header("Your Timetable")
    timetable_df = pd.DataFrame(class_schedule)
    st.dataframe(timetable_df)
else:
    st.info("No classes added yet. Add your classes above.")

# Download the timetable as CSV
if len(class_schedule) > 0:
    csv = timetable_df.to_csv(index=False)
    st.download_button(
        label="Download Timetable as CSV",
        data=csv,
        file_name=f"{student_name}_timetable_{day_of_week}.csv",
        mime="text/csv",
    )
