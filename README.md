# MailAutomation

MailAutomation is a Python-based script that allows you to automatically send personalized emails using data from an Excel file. It supports customizable message formatting and automatic attachment of all files in a specified folder.

## Features

- Send personalized emails using data from an Excel spreadsheet  
- Support for plain text messages (HTML optional in future versions)  
- Automatically attach all files from a given folder  
- Customizable subject, message body, and signature  
- Simple configuration using a dedicated setup file  

## Project Structure

```
MailAutomation/
│
├── src/
│   ├── main.py         # Main script to send emails
│   ├── setup.py        # Configuration (SMTP settings, paths, message content)
│   ├── attach.py       # Utility to handle file attachments
│   └── testSMTP.py     # Utility tO test smtp connection
│
├── attachments/        # Folder containing all files to be attached
├── tabs/
│   └── your_excel_file.xlsx  # Excel file with recipient data
├── README.md           # Project documentation
```

## Requirements

- Python 3.10 or newer  
- Required Python libraries:
  - `pandas`
  - `openpyxl`
  - Standard library modules: `smtplib`, `email`, `os`, `mimetypes`

You can install the required libraries using:

```bash
pip install pandas openpyxl
```

## Excel File Format

The Excel file must be in this format (case-sensitive):

| Civilité | Name | Email            |
|----------|------|------------------|
| Mr.      | John | john@email.com   |
| Ms.      | Jane | jane@email.com   |

## Configuration

Edit the `setup.py` file to configure:

- Your email address and password  
- SMTP server and port (e.g., `smtp.office365.com` for Outlook or `smtp.gmail.com`)  
- Message subject, body, and signature  

## Usage

Put the Excel file in the folder `tabs/`
If you want to join some files put them in the folder `attachments/` and turn the variable `USE_ATTACHMENT` tu `True`
Run the script from the `src/` directory:

```bash
python main.py
```

The script will:
1. Read recipient data from the Excel file.  
2. Log into the SMTP server.  
3. Create and send emails with optional attachments.  
4. Display progress and status messages in the console.  

## Author

Created by 9Pierrot — 01/05/2025

## License

This project is licensed under the MIT License.
