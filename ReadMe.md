# Grading-assignments-for-C-language-courses

## Overview

`Grading-assignments-for-C-language-courses` is a Python-based tool designed to automate the grading process for C language course assignments. The tool simplifies the workflow by extracting assignment submissions from emails, evaluating them based on predefined grading criteria, and outputting the results to an Excel file.

## Features

- **Email Parsing**: Automatically fetches emails with a subject format of `StudentID_Name` (e.g., `123456_JohnDoe`).
- **Submission Extraction**: Reads the C language program from the email body.
- **Grading Automation**: Grades the submissions based on user-defined criteria.
- **Time Range Filtering**: Supports grading within a specified submission period.
- **Excel Output**: Outputs grading results to an Excel file for easy review and record-keeping.

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/Grading-assignments-for-C-language-courses.git
   cd Grading-assignments-for-C-language-courses
2. **Install dependencies**:
   ```bash
   pip3 install -r requirements.txt
   ```

## Securely Managing Email Credentials Setting
To protect your email privacy and ensure secure authentication, this tool uses the keyring library to securely store your email password or authorization code. The stored credentials are accessed programmatically without hardcoding them into the project, reducing the risk of exposure.

1. **Enable IMAP/SMTP Services**:  
   Ensure that your email account has IMAP and SMTP services enabled.  

   **For 163 Mail users**:  
     - Log in to your email account at [163.com](https://mail.163.com/).  
     - Go to **Settings -> POP3/SMTP/IMAP**.  
     - Enable **IMAP/SMTP Service**.  
     - Generate an **Authorization Code** (this code will be used instead of your login password).  

   **For other email providers**:  
     - Refer to the official documentation or help center of your email provider to enable IMAP and SMTP services.  
     - Search for instructions on generating an authorization code if required.  

1. **Save Your Email Password/Authorization Code: Create a new Python file, e.g., set_password.py, and add the following code**:
   ```python
   import keyring

   # Replace with your email and authorization code
   service_name = 'imap.163.com'
   email = 'YourEmail@163.com'
   password = 'YourAuthorizationCode'

   # Save the password securely
   keyring.set_password(service_name, email, password)
   
   password = keyring.get_password(service_name, email)

   if not password:
      print("Password not found. Please set it first using keyring.")
   else:
      print("Password retrieved successfully!")
   ```
2. **Run the Script: Execute the script in your terminal**:
   ```bash
   python3 set_password.py
## Run the tool
   ```bash
   python3 GradingAssignmentsC.py
