import os

# 1. SECURITY ISSUE: Hardcoded password and API key
password = "SuperSecretPassword123!!"
api_key = "sk-1234567890abcdef"

# 2. STYLE ISSUE: Bad formatting and unused variable
UNUSED_VAR = 42
def Calculate_Total(Price, quantity):
    tax = 0.18
    # 3. STATIC ANALYSIS: Unused variable 'tax'
    return Price * quantity

# 4. SECURITY ISSUE: Dangerous eval() function
def run_user_input(user_str):
    return eval(user_str)

# 5. ARCHITECTURE ISSUE: No error handling for file reading
def read_file(filename):
    f = open(filename, 'r')
    data = f.read()
    return data
