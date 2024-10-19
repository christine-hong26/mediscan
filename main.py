from image import detect_text
from data.data_loader import load_drug_data, find_drug_name

if __name__ == "__main__":
    # Load the drug dataset
    drug_data = load_drug_data('data/medicine_dataset.csv')

    # Extract text from the image
    extracted_text = detect_text('/Users/fernandabarraza/Documents/Tylenol-Extra-Strength-Caplets-with-500-mg-Acetaminophen-100-Ct_7fbb68c5-7b34-4c89-a54c-c9d17d4d2e20.7b8aa7dde99c41d6a005183b29865f6c.webp')
    print(extracted_text)

    if not extracted_text:
        print("No text was detected in the image.")
    else:
        # Find all drug names in the extracted text
        found_drug_names = find_drug_name(extracted_text, drug_data.keys())

        if found_drug_names:
            for drug_name in found_drug_names:
                print(f"Found drug: {drug_name}")
                # Access additional information about the drug
                drug_info = drug_data[drug_name]
                print(f"Drug ID: {drug_info['id']}")
                print(f"Substitutes: {drug_info['substitutes']}")
                print(f"Side Effects: {drug_info['side_effects']}")
        else:
            print("No drugs found in the extracted text.")
