import json

def load_and_analyze():
    # Load the JSON database
    try:
        with open('database.json', 'r', encoding='utf-8') as file:
            data = json.load(file)
    except FileNotFoundError:
        print("Error: database.json file not found.")
        return

    print("==============================================")
    print("--- CHUUKESE-POHNPEIAN CONVERSATIONAL PIPELINE ---")
    print(f"Total Phrase Mappings Processed: {len(data)}")
    print("==============================================\n")
    
    # Process and print the structured data entries
    for entry in data:
        print(f"ID: {entry['concept_id']} | Concept: '{entry['english_meaning']}'")
        print(f"  Category: [{entry['semantic_category'].upper()}] | Type: {entry['dialogue_type']}")
        print(f"  └─ Chuukese:  {entry['chuukese']['phrase']} {entry['chuukese']['ipa_phonetics']}")
        print(f"  └─ Pohnpeian: {entry['pohnpeian']['phrase']} {entry['pohnpeian']['ipa_phonetics']}")
        print(f"  └─ Analysis:  {entry['linguistic_overlap']}")
        print("-" * 50)

if __name__ == "__main__":
    load_and_analyze()
