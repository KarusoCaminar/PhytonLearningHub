import sys
import io
import contextlib
import traceback

def execute_code(code_string):
    """
    Safely executes the given Python code string and returns the output or error message.
    
    Args:
        code_string: The Python code to execute
    
    Returns:
        String containing output or error message
    """
    # Redirect stdout and stderr
    stdout_buffer = io.StringIO()
    stderr_buffer = io.StringIO()
    
    # Result to return
    result = ""
    
    try:
        # Redirect standard output and standard error
        with contextlib.redirect_stdout(stdout_buffer), contextlib.redirect_stderr(stderr_buffer):
            # Execute the code as a whole
            exec(code_string)
            
        # Get output
        stdout_output = stdout_buffer.getvalue()
        stderr_output = stderr_buffer.getvalue()
        
        # Combine outputs
        if stdout_output:
            result += stdout_output
        if stderr_output:
            result += "\nStandard Error:\n" + stderr_output
            
    except Exception as e:
        # Get the traceback
        error_msg = traceback.format_exc()
        result = f"Error:\n{error_msg}"
    
    # If no output was generated at all
    if not result:
        result = "Code executed successfully (no output)"
        
    return result

def validate_solution(user_code, expected_output, validation_func=None):
    """
    Validates a user's solution against expected output or using a validation function.
    
    Args:
        user_code: The user's submitted code
        expected_output: The expected output string
        validation_func: Optional function to validate the code directly
    
    Returns:
        Boolean indicating whether the solution is correct
    """
    # If a validation function is provided, use it
    if validation_func:
        try:
            # Create a local namespace
            local_namespace = {}
            # Execute the user code in this namespace
            exec(user_code, {}, local_namespace)
            # Use the validation function to check the solution
            return validation_func(local_namespace)
        except Exception:
            return False
    
    # Otherwise compare output
    output = execute_code(user_code)
    
    # Clean up output for comparison (remove leading/trailing whitespace, normalize line endings)
    clean_output = output.strip().replace('\r\n', '\n')
    clean_expected = expected_output.strip().replace('\r\n', '\n')
    
    return clean_output == clean_expected
