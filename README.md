File Processor - Text Modifier 📝
A robust Python application for reading, modifying, and writing text files with comprehensive error handling and multiple text transformation options.

🚀 Features
Multiple Text Transformations:

Convert text to uppercase

Convert text to lowercase

Capitalize sentences

Add line numbers to text

Comprehensive Error Handling:

File not found errors

Permission errors

File encoding issues

Invalid user input handling

User-Friendly Interface:

Interactive prompts with clear instructions

Preview of modified content

Option to retry after errors

Smart File Naming:

Automatically generates output filenames

Preserves original file extensions

📋 Requirements
Python 3.6 or higher

No external dependencies

🛠 Installation
Clone or download the Python script

Ensure Python is installed on your system

Run the script from your terminal or command prompt:

bash
python file_processor.py
📖 Usage
Basic Usage
Run the script

Enter the filename you want to process when prompted

Select a transformation option (1-4)

The program will create a modified version of your file

Transformation Options
Uppercase Conversion: Converts all text to uppercase letters

Lowercase Conversion: Converts all text to lowercase letters

Sentence Capitalization: Capitalizes the first letter of each sentence

Line Numbering: Adds sequential numbers to each line of the file

Example
text
Please enter the filename to read: example.txt
✅ Successfully read 'example.txt'

Choose how to modify the file:
1. Convert to uppercase
2. Convert to lowercase
3. Capitalize each sentence
4. Add line numbers

Enter your choice (1-4): 4
✅ Successfully created 'example_modified.txt' with line numbers

Preview of modified content:
------------------------------
1: This is the first line.
2: This is the second line.
3: And this is the third line...
🧪 Error Handling
The application handles various error scenarios gracefully:

File Not Found: Provides clear error message and retry option

Permission Issues: Informs user about access restrictions

Encoding Problems: Detects and reports binary file issues

Invalid Input: Validates user choices and provides feedback

🏗️ Code Structure
The application is organized as follows:

Main Function (file_processor()):

Coordinates the file processing workflow

Handles user interaction

Manages error handling

File Reading:

Uses context managers for safe file handling

Implements multiple exception handling for robust operation

Text Processing:

Implements four different text transformation algorithms

Handles edge cases in text processing

File Writing:

Creates modified files with appropriate naming

Ensures proper encoding for output files

🔧 Customization
The code is modular and easy to extend:

Add new transformation options by expanding the choice menu

Modify error handling for specific use cases

Adjust preview length by changing the character limit

📊 Testing
Test the application with various scenarios:

Valid text files with different content

Non-existent files to test error handling

Files with special characters and formatting

Large files to ensure performance

🐛 Known Limitations
Sentence capitalization uses a simple period-based approach

Large files (>100MB) may have performance issues

Preview shows only the first 200 characters

📝 License
This project is open source and available under the MIT License.

🤝 Contributing
Contributions, issues, and feature requests are welcome! Feel free to check the issues page.

👨‍💻 Development
To modify or extend the application:

Fork the repository

Create a feature branch

Make your changes

Add tests if applicable

Submit a pull request

📞 Support
If you have any questions or encounter issues, please open an issue in the repository.
