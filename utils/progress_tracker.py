class ProgressTracker:
    """
    Tracks the user's progress through tutorials, exercises, and quizzes.
    """
    
    def __init__(self):
        """Initialize the progress tracker with empty dictionaries."""
        # Structure to track completed tutorials, exercises, and quiz scores
        self.completed_tutorials = {}
        self.completed_exercises = {}
        self.quiz_results = {}
    
    def complete_tutorial(self, tutorial_index):
        """Mark a tutorial as completed."""
        self.completed_tutorials[tutorial_index] = True
    
    def complete_exercise(self, exercise_index):
        """Mark an exercise as completed."""
        self.completed_exercises[exercise_index] = True
    
    def validate_exercise(self, exercise_index, user_code, output, validation_func=None, expected_output=''):
        """
        Validate a user's exercise solution.
        
        Args:
            exercise_index: Index of the exercise
            user_code: The user's submitted code
            output: The output from executing the user's code
            validation_func: Optional function to validate the code directly
            expected_output: Expected output string for comparison
            
        Returns:
            Boolean indicating whether the solution is correct
        """
        # If no validation_func and no expected_output, just mark as completed
        if not validation_func and not expected_output:
            self.complete_exercise(exercise_index)
            return True
            
        # Clean outputs for comparison
        clean_output = output.strip().replace('\r\n', '\n')
        clean_expected = expected_output.strip().replace('\r\n', '\n')
        
        # If validation function is provided, use it
        if validation_func:
            try:
                # Create a local namespace and execute the user code
                local_namespace = {}
                exec(user_code, {}, local_namespace)
                # Validate using the provided function
                is_correct = validation_func(local_namespace)
            except Exception:
                is_correct = False
        else:
            # Otherwise compare output
            is_correct = clean_output == clean_expected
        
        if is_correct:
            self.complete_exercise(exercise_index)
        
        return is_correct
    
    def evaluate_quiz(self, quiz_index, answers, questions):
        """
        Evaluate a quiz submission.
        
        Args:
            quiz_index: Index of the quiz
            answers: Dictionary of user's answers
            questions: List of question dictionaries with correct answers
            
        Returns:
            Tuple of (score, total questions, feedback list)
        """
        score = 0
        total = len(questions)
        feedback = []
        
        for i, question in enumerate(questions):
            user_answer = answers.get(f"q{i}", None)
            correct_answer = question['correct_answer']
            
            # Check if answer is correct
            is_correct = False
            if user_answer is not None:
                if question['type'] == 'true_false':
                    # Convert string "True"/"False" to boolean for comparison
                    user_bool = user_answer == "True"
                    correct_bool = correct_answer == "True" or correct_answer == True
                    is_correct = user_bool == correct_bool
                else:
                    is_correct = str(user_answer).strip().lower() == str(correct_answer).strip().lower()
            
            if is_correct:
                score += 1
                feedback.append({
                    'correct': True,
                    'explanation': question.get('explanation', 'Correct!'),
                    'user_answer': user_answer,
                    'correct_answer': correct_answer
                })
            else:
                feedback.append({
                    'correct': False,
                    'explanation': question.get('explanation', ''),
                    'user_answer': user_answer,
                    'correct_answer': correct_answer
                })
        
        # Record quiz result
        self.quiz_results[quiz_index] = {
            'score': score,
            'total': total,
            'completed': score >= total * 0.7  # 70% threshold to be considered completed
        }
        
        return score, total, feedback
    
    def complete_quiz(self, quiz_index, score=None, total=None):
        """Mark a quiz as completed with an optional score."""
        if quiz_index in self.quiz_results:
            self.quiz_results[quiz_index]['completed'] = True
        else:
            self.quiz_results[quiz_index] = {
                'score': score if score is not None else 0,
                'total': total if total is not None else 0,
                'completed': True
            }
    
    def get_statistics(self):
        """
        Get progress statistics.
        
        Returns:
            Dictionary with progress statistics
        """
        from content.tutorials import tutorials
        from content.exercises import exercises
        from content.quizzes import quizzes
        
        # Count completed items
        tutorials_completed = sum(1 for completed in self.completed_tutorials.values() if completed)
        exercises_completed = sum(1 for completed in self.completed_exercises.values() if completed)
        quizzes_completed = sum(1 for result in self.quiz_results.values() if result.get('completed', False))
        
        # Calculate total progress
        total_items = len(tutorials) + len(exercises) + len(quizzes)
        completed_items = tutorials_completed + exercises_completed + quizzes_completed
        
        total_progress = completed_items / total_items if total_items > 0 else 0
        
        return {
            'tutorials_completed': tutorials_completed,
            'exercises_completed': exercises_completed,
            'quizzes_completed': quizzes_completed,
            'total_progress': total_progress
        }
    
    def get_detailed_progress(self):
        """
        Get detailed progress information.
        
        Returns:
            Dictionary with detailed progress for each section
        """
        return {
            'tutorials': self.completed_tutorials,
            'exercises': self.completed_exercises,
            'quizzes': self.quiz_results
        }
