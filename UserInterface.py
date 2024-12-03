import os
import keyring

def GetUserSettings():
    """
    Get user settings, including time range and file paths.
    """
    # Define the time range here
    start_date = '2024-04-23'   
    end_date = '2024-05-01'
    

    current_dir = os.getcwd()
    source_code_dir = os.path.join(current_dir, 'source_code')
    output_file = os.path.join(current_dir, 'output.xlsx') # Set the file name of your choice."
    password = keyring.get_password('imap.163.com', 'shermingchen@163.com') # Specify the email address associated with your account.

    return {
        'start_date': start_date,
        'end_date': end_date,
        'source_code_dir': source_code_dir,
        'output_file': output_file,
        'password': password
    }

def GetImapClientInfo():
    return (
        "name", "shermingchen", # your name
        "contact", "shermingchen@163.com",  #your email
        "version", "1.0.0",
        "vendor", "Imbox"
    )
def GetInputOutputValues():
    # Please adapt the expected input and output to match the requirements of your assignment.
    input_value = 0.02  
    expect_output = 50
    return input_value, expect_output