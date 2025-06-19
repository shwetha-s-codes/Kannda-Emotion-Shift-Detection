import pandas as pd

# List of Kannada words to extract
target_words = ["ಆದರೆ", "ಒಂದು ವೇಳೆ", "ಅಥವಾ", "ಇಲ್ಲವೇ", "ಏಕೆಂದರೆ", "ಆದ್ದರಿಂದ", "ಯಾವಾಗಲೂ"]

def extract_sentences(file_path):
    extracted_data = []

    # Read the .txt file line by line
    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            sentence = line.strip()
            for word in target_words:
                if word in sentence:
                    extracted_data.append([sentence,"", "",word])  # Empty sentiment column for annotation
    
    return extracted_data

# Provide the path to your .txt file
file_path = "split_data/split_2.txt"  # Replace with actual file path

# Extract sentences
sentences_with_keywords = extract_sentences(file_path)

# Create a DataFrame with required columns
df = pd.DataFrame(sentences_with_keywords, columns=["Sentence", "Part1 Sentiment", "Part2 Sentiment","Transition Word"])

# Save to CSV
csv_filename = "extracted_sentences2.csv"
df.to_csv(csv_filename, index=False, encoding="utf-8")

print(f"\nExtraction complete! Sentences saved in '{csv_filename}'.")
