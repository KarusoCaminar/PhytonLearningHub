import streamlit as st
import sys
from utils.code_execution import execute_code
from utils.progress_tracker import ProgressTracker
from content.tutorials import tutorials
from content.exercises import exercises
from content.quizzes import quizzes

# Set page config
st.set_page_config(
    page_title="Python Learning Hub",
    page_icon="🐍",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Initialize session state variables if they don't exist
if 'current_tutorial' not in st.session_state:
    st.session_state.current_tutorial = 0
if 'current_exercise' not in st.session_state:
    st.session_state.current_exercise = 0
if 'current_quiz' not in st.session_state:
    st.session_state.current_quiz = 0
if 'progress_tracker' not in st.session_state:
    st.session_state.progress_tracker = ProgressTracker()
if 'code_input' not in st.session_state:
    st.session_state.code_input = ""
if 'code_output' not in st.session_state:
    st.session_state.code_output = ""
if 'active_tab' not in st.session_state:
    st.session_state.active_tab = "Tutorials"

# Sidebar for navigation
st.sidebar.title("Python Learning Hub")
st.sidebar.image("https://www.python.org/static/community_logos/python-logo-generic.svg", width=200)

# Navigation options
nav_option = st.sidebar.radio(
    "Navigation",
    ["Tutorials", "Exercises", "Quizzes", "Progress"]
)

st.sidebar.markdown("---")
st.sidebar.markdown("### Your Progress")
progress_stats = st.session_state.progress_tracker.get_statistics()
st.sidebar.progress(progress_stats['total_progress'])
st.sidebar.markdown(f"**Overall Progress:** {progress_stats['total_progress']:.0%}")
st.sidebar.markdown(f"**Tutorials Completed:** {progress_stats['tutorials_completed']}/{len(tutorials)}")
st.sidebar.markdown(f"**Exercises Completed:** {progress_stats['exercises_completed']}/{len(exercises)}")
st.sidebar.markdown(f"**Quizzes Completed:** {progress_stats['quizzes_completed']}/{len(quizzes)}")

# Display chosen content
if nav_option == "Tutorials":
    st.session_state.active_tab = "Tutorials"

    st.title("Python Tutorials")
    st.markdown("Learn Python step-by-step with these interactive tutorials.")
    
    # Tutorial navigation
    col1, col2, col3 = st.columns([1, 3, 1])
    with col1:
        if st.button("⬅️ Previous Tutorial") and st.session_state.current_tutorial > 0:
            st.session_state.current_tutorial -= 1
            st.rerun()
    with col3:
        if st.button("Next Tutorial ➡️") and st.session_state.current_tutorial < len(tutorials) - 1:
            st.session_state.current_tutorial += 1
            # Mark the previous tutorial as completed
            st.session_state.progress_tracker.complete_tutorial(st.session_state.current_tutorial - 1)
            st.rerun()
    
    # Tutorial selector
    tutorial_options = [f"{i+1}. {t['title']}" for i, t in enumerate(tutorials)]
    selected_tutorial = st.selectbox(
        "Select Tutorial",
        tutorial_options,
        index=st.session_state.current_tutorial
    )
    st.session_state.current_tutorial = tutorial_options.index(selected_tutorial)
    
    # Display tutorial content
    tutorial = tutorials[st.session_state.current_tutorial]
    st.header(tutorial['title'])
    st.markdown(tutorial['content'])
    
    # Code examples
    if 'example' in tutorial:
        st.subheader("Example Code")
        st.code(tutorial['example'], language='python')
        
        with st.expander("Try it yourself"):
            if 'example' in tutorial:
                default_code = tutorial.get('starter_code', tutorial['example'])
            else:
                default_code = "# Your code here"
                
            user_code = st.text_area("Code", value=default_code, height=200, key=f"tutorial_code_{st.session_state.current_tutorial}")
            
            if st.button("Run Code", key=f"run_tutorial_{st.session_state.current_tutorial}"):
                output = execute_code(user_code)
                st.code(output, language=None)
                # Mark the current tutorial as completed if code executed
                st.session_state.progress_tracker.complete_tutorial(st.session_state.current_tutorial)

elif nav_option == "Exercises":
    st.session_state.active_tab = "Exercises"
    
    st.title("Python Exercises")
    st.markdown("Practice what you've learned with these exercises.")
    
    # Exercise navigation
    col1, col2, col3 = st.columns([1, 3, 1])
    with col1:
        if st.button("⬅️ Previous Exercise") and st.session_state.current_exercise > 0:
            st.session_state.current_exercise -= 1
            st.rerun()
    with col3:
        if st.button("Next Exercise ➡️") and st.session_state.current_exercise < len(exercises) - 1:
            st.session_state.current_exercise += 1
            st.rerun()
    
    # Exercise selector
    exercise_options = [f"{i+1}. {e['title']}" for i, e in enumerate(exercises)]
    selected_exercise = st.selectbox(
        "Select Exercise",
        exercise_options,
        index=st.session_state.current_exercise
    )
    st.session_state.current_exercise = exercise_options.index(selected_exercise)
    
    # Display exercise content
    exercise = exercises[st.session_state.current_exercise]
    st.header(exercise['title'])
    st.markdown(exercise['problem'])
    
    # Expected output
    if 'expected_output' in exercise:
        with st.expander("Expected Output"):
            st.code(exercise['expected_output'], language=None)
    
    # Hint
    if 'hint' in exercise:
        with st.expander("Hint"):
            st.markdown(exercise['hint'])
    
    # User code input
    default_code = exercise.get('starter_code', "# Your solution here")
    user_code = st.text_area("Your Solution", value=default_code, height=300, key=f"exercise_code_{st.session_state.current_exercise}")
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Run Code", key=f"run_exercise_{st.session_state.current_exercise}"):
            output = execute_code(user_code)
            st.session_state.code_output = output
            st.code(output, language=None)
    
    with col2:
        if st.button("Submit Solution", key=f"submit_exercise_{st.session_state.current_exercise}"):
            output = execute_code(user_code)
            is_correct = st.session_state.progress_tracker.validate_exercise(
                st.session_state.current_exercise,
                user_code,
                output,
                exercise.get('validation', None),
                exercise.get('expected_output', '')
            )
            
            if is_correct:
                st.success("Correct! Good job!")
                # Mark the exercise as completed
                st.session_state.progress_tracker.complete_exercise(st.session_state.current_exercise)
            else:
                st.error("Your solution doesn't match the expected output. Try again!")
            
            st.code(output, language=None)
    
    # Show solution
    with st.expander("Show Solution"):
        if st.button("Reveal Solution", key=f"reveal_solution_{st.session_state.current_exercise}"):
            if 'solution' in exercise:
                st.code(exercise['solution'], language='python')
                st.markdown("Remember, trying to solve it yourself is the best way to learn!")
            else:
                st.info("Solution not available for this exercise.")

elif nav_option == "Quizzes":
    st.session_state.active_tab = "Quizzes"
    
    st.title("Python Quizzes")
    st.markdown("Test your knowledge with these quizzes.")
    
    # Quiz navigation
    col1, col2, col3 = st.columns([1, 3, 1])
    with col1:
        if st.button("⬅️ Previous Quiz") and st.session_state.current_quiz > 0:
            st.session_state.current_quiz -= 1
            st.rerun()
    with col3:
        if st.button("Next Quiz ➡️") and st.session_state.current_quiz < len(quizzes) - 1:
            st.session_state.current_quiz += 1
            st.rerun()
    
    # Quiz selector
    quiz_options = [f"{i+1}. {q['title']}" for i, q in enumerate(quizzes)]
    selected_quiz = st.selectbox(
        "Select Quiz",
        quiz_options,
        index=st.session_state.current_quiz
    )
    st.session_state.current_quiz = quiz_options.index(selected_quiz)
    
    # Display quiz content
    quiz = quizzes[st.session_state.current_quiz]
    st.header(quiz['title'])
    st.markdown(quiz['description'])
    
    # Initialize answers in session state
    quiz_key = f"quiz_{st.session_state.current_quiz}"
    if quiz_key not in st.session_state:
        st.session_state[quiz_key] = {f"q{i}": None for i in range(len(quiz['questions']))}
    
    # Display questions
    for i, question in enumerate(quiz['questions']):
        st.subheader(f"Question {i+1}: {question['question']}")
        
        if question['type'] == 'mcq':
            answer = st.radio(
                f"Select one option (Q{i+1}):",
                question['options'],
                key=f"quiz_{st.session_state.current_quiz}_q{i}"
            )
            st.session_state[quiz_key][f"q{i}"] = answer
        
        elif question['type'] == 'true_false':
            answer = st.radio(
                f"True or False (Q{i+1}):",
                ["True", "False"],
                key=f"quiz_{st.session_state.current_quiz}_q{i}"
            )
            st.session_state[quiz_key][f"q{i}"] = answer
        
        elif question['type'] == 'short_answer':
            answer = st.text_input(
                f"Your answer (Q{i+1}):",
                key=f"quiz_{st.session_state.current_quiz}_q{i}"
            )
            st.session_state[quiz_key][f"q{i}"] = answer
        
        st.markdown("---")
    
    # Submit button
    if st.button("Submit Quiz", key=f"submit_quiz_{st.session_state.current_quiz}"):
        score, total, feedback = st.session_state.progress_tracker.evaluate_quiz(
            st.session_state.current_quiz,
            st.session_state[quiz_key],
            quiz['questions']
        )
        
        st.success(f"You scored {score}/{total}!")
        
        # Display feedback for each question
        for i, fb in enumerate(feedback):
            if fb['correct']:
                st.success(f"Question {i+1}: Correct! {fb.get('explanation', '')}")
            else:
                st.error(f"Question {i+1}: Incorrect. {fb.get('explanation', '')} The correct answer is: {fb['correct_answer']}")
        
        # Mark quiz as completed if score is above threshold
        if score >= total * 0.7:  # 70% threshold
            st.session_state.progress_tracker.complete_quiz(st.session_state.current_quiz)
            st.balloons()

elif nav_option == "Progress":
    st.session_state.active_tab = "Progress"
    
    st.title("Your Learning Progress")
    
    progress_data = st.session_state.progress_tracker.get_detailed_progress()
    
    # Overall progress
    st.header("Overall Progress")
    stats = st.session_state.progress_tracker.get_statistics()
    st.progress(stats['total_progress'])
    st.markdown(f"**Overall completion: {stats['total_progress']:.0%}**")
    
    # Tutorials progress
    st.header("Tutorials Progress")
    tutorial_progress = progress_data['tutorials']
    for i, completed in tutorial_progress.items():
        if i < len(tutorials):  # Ensure index is valid
            title = tutorials[i]['title']
            if completed:
                st.markdown(f"✅ Tutorial {i+1}: {title}")
            else:
                st.markdown(f"⬜ Tutorial {i+1}: {title}")
    
    # Exercises progress
    st.header("Exercises Progress")
    exercise_progress = progress_data['exercises']
    for i, completed in exercise_progress.items():
        if i < len(exercises):  # Ensure index is valid
            title = exercises[i]['title']
            if completed:
                st.markdown(f"✅ Exercise {i+1}: {title}")
            else:
                st.markdown(f"⬜ Exercise {i+1}: {title}")
    
    # Quizzes progress
    st.header("Quizzes Progress")
    quiz_progress = progress_data['quizzes']
    for i, score_data in quiz_progress.items():
        if i < len(quizzes):  # Ensure index is valid
            title = quizzes[i]['title']
            if score_data['completed']:
                st.markdown(f"✅ Quiz {i+1}: {title} - Score: {score_data['score']}/{score_data['total']}")
            else:
                st.markdown(f"⬜ Quiz {i+1}: {title}")

# Code playground (additional feature)
st.sidebar.markdown("---")
with st.sidebar.expander("Code Playground"):
    st.markdown("Try any Python code here without affecting your progress")
    playground_code = st.text_area("Code", value="# Your code here\nprint('Hello, Python!')", height=200, key="playground_code")
    if st.button("Run", key="run_playground"):
        output = execute_code(playground_code)
        st.code(output, language=None)

# Footer
st.sidebar.markdown("---")
st.sidebar.markdown("© 2023 Python Learning Hub")
st.sidebar.markdown("Made with Streamlit")
