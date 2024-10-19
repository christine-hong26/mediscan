import csv

def load_drug_data(filepath):
    """Loads the drug data from a CSV file into a dictionary."""
    drugs = {}
    with open(filepath, mode='r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header row
        for row in reader:
            drug_id = row[0]
            drug_name = row[1]
            # Store other information in a dictionary
            drugs[drug_name.lower()] = {  # Use lower case for case-insensitive matching
                'id': drug_id,
                'substitutes': row[2:7],
                'side_effects': row[7:10]
            }
    return drugs

import re

def find_drug_name(extracted_text, drug_list):
    """Finds the drug name in the extracted text."""
    # Create a list to hold matched drug names
    found_drugs = []
    
    for drug in drug_list:
        # Create a regex pattern that looks for the drug name and its dosage
        pattern = re.escape(drug) + r"\s*\d*\s*(mg|mg/|g|ml|tablet|capsule|injection)?"
        
        if re.search(pattern, extracted_text, re.IGNORECASE):
            found_drugs.append(drug)
    
    return found_drugs  # Return a list of matched drug names

