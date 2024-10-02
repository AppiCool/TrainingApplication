# Training Application

## Description
This console application reads training data from a JSON file (trainings.txt) and generates output in three ways: 
1. It lists each completed training along with a count of how many people have completed that training. 
2. Given a list of trainings and a fiscal year (defined as July 1st of the previous year to June 30th of the current year), it lists all individuals who completed specified trainings in that fiscal year.    - **Parameters**:     - Trainings: "Electrical Safety for Labs", "X-Ray Safety", "Laboratory Safety Training"     - Fiscal Year: 2024 (for example)
3. It finds all people who have completed trainings that have already expired or will expire within one month of a specified date (with the note that a training is considered expired the day after its expiration date).   - **Date Used**: October 1st, 2023 (for example)

### Assumptions
- Trainings with an expiration date of `NULL` are considered active.

## Features
- Count and display completed trainings for all users.
- Filter and list users who completed specific trainings within a given fiscal year.
- Identify and categorize trainings that are expired or expiring soon.

## Installation Instructions
1. Clone this repository to your local machine using the following command:   ```bash   git clone https://github.com/your-username/Training Application.git   ``` 2. Navigate to the project directory:   ```bash   cd Training Application   ``` 
3. Ensure you have Python installed on your machine. You can download it from [python.org](https://www.python.org/). 
4. Install any necessary packages (if applicable) by running:   ```bash   pip install -r requirements.txt   ```

## Usage Instructions
To run the application, follow these steps:

### Using Command Prompt
1. Open Command Prompt. 
2. Navigate to the project directory:   ```bash   cd path\to\Training Application   ``` 
3. Run the application using Python:   ```bash   python trainings.py   ```

### Using Visual Studio Code
1. Open Visual Studio Code. 
2. Use the "Open Folder" option to open the project directory. 
3. Open the terminal in VS Code (View > Terminal). 
4. Run the application with the following command:   ```bash   python trainings.py   ```

## Author Information
Apeksha Padaliya
