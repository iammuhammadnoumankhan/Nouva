from langchain_experimental.utilities import PythonREPL

def execute_python_code(code):
    """Execute a Python command and return the output."""
    python_repl = PythonREPL()
    result = python_repl.run(code)
    return result