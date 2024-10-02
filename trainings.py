import json
from datetime import datetime, timedelta

"""
Module to manage training data and provide insights on training completions.
"""

def load_data(file_path):
    """Load training data from a JSON file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:  # Specified encoding
            data = json.load(file)
            return data
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        return []
    except json.JSONDecodeError:
        print("Error: The file is not a valid JSON.")
        return []

def parse_date(date_str):
    """Parse date in 'Oct 1st, 2023' format to a datetime object."""
    # Remove the 'st', 'nd', 'rd', 'th' from the day part
    day_suffixes = ['st', 'nd', 'rd', 'th']
    for suffix in day_suffixes:
        date_str = date_str.replace(suffix, '')

    return datetime.strptime(date_str.strip(), "%b %d, %Y")

def task_1(data):
    """List each completed training with a count of how many people have completed that training."""
    training_counts = {}
    for person in data:
        for completion in person.get('completions', []):
            training_name = completion['name']
            training_counts[training_name] = training_counts.get(training_name, 0) + 1
    return training_counts

def task_2(data, trainings, fiscal_year):
    """List all people that completed the specified training in the specified fiscal year."""
    start_date = datetime(fiscal_year - 1, 7, 1)
    end_date = datetime(fiscal_year, 6, 30)
    results = {}
    
    for training in trainings:
        results[training] = []
        for person in data:
            for completion in person.get('completions', []):
                if completion['name'] == training:
                    completion_date = datetime.strptime(completion['timestamp'], "%m/%d/%Y")
                    if start_date <= completion_date <= end_date:
                        results[training].append(person['name'])
    return results

def task_3(data, specified_date):
    """Find people with completed trainings that have expired or will expire soon."""
    expiration_date = datetime.strptime(specified_date, "%m/%d/%Y")
    results = []
    
    for person in data:
        person_results = {'name': person['name'], 'completed_trainings': []}
        
        for completion in person.get('completions', []):
            if completion['expires'] is not None:  # Check if there's an expiration date
                expiration_timestamp = datetime.strptime(completion['expires'], "%m/%d/%Y")
                # Check for expiration or expiration within one month
                if expiration_timestamp < expiration_date or (
                    expiration_date <= expiration_timestamp <= expiration_date + timedelta(days=30)
                ):
                    status = 'expired' if expiration_timestamp < expiration_date else 'expires soon'
                    person_results['completed_trainings'].append({
                        'training_name': completion['name'],
                        'status': status
                    })
        
        if person_results['completed_trainings']:  # Only add if there are relevant trainings
            results.append(person_results)
    return results

def main():
    """Main function to run tasks interactively."""
    data = load_data('trainings.txt')  # Load data from JSON file
    if not data:  # If data loading failed, exit early
        return

    # Task 1
    print("\n=== Task 1: Count of Completed Trainings ===")
    task_1_result = task_1(data)
    print(json.dumps(task_1_result, indent=4))

    # Task 2
    print("\n=== Task 2: People Who Completed Specified Trainings ===")
    try:
        trainings_input = input("Enter the trainings in the format: '\"Training 1\", \"Training 2\"' (comma separated): ")
        trainings = [training.strip().strip('"') for training in trainings_input.split(',')]
        fiscal_year = int(input("Enter the fiscal year (e.g., 2024): "))
        
        task_2_result = task_2(data, trainings, fiscal_year)
        
        # Save the result to a JSON file
        with open('task_2_output.json', 'w', encoding='utf-8') as outfile:  # Specified encoding
            json.dump(task_2_result, outfile, indent=4)
        
        print("Results saved to 'task_2_output.json':")  # Removed unnecessary f-string
        print(json.dumps(task_2_result, indent=4))
        
    except ValueError:
        print("Error: Please provide a valid fiscal year as an integer.")
        return

    # Task 3
    print("\n=== Task 3: People with Expired or Expiring Soon Trainings ===")
    try:
        specified_date = input("Enter the date in 'Oct 1st, 2023' format: ")
        parsed_date = parse_date(specified_date)  # Parse the input date
        task_3_result = task_3(data, parsed_date.strftime("%m/%d/%Y"))  # Format for task_3
        print(json.dumps(task_3_result, indent=4))
    except ValueError:
        print("Error: Please provide a valid date in the expected format.")
        return

if __name__ == "__main__":
    main()
