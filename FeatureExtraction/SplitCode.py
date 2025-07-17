#Code to split the data set to train each part separately along with their emotions
import pandas as pd

# Load your dataset
df = pd.read_csv("../DataSets/Merged_dataset.csv")  # Update with your actual filename

# Robust split function
def split_with_transition(row):
    sentence = str(row['Sentence']).strip()
    transition = str(row['Transition Word']).strip()

    if transition in sentence:
        before, after = sentence.split(transition, 1)
        part1 = before.strip()
        part2 = (transition + " " + after).strip()
    else:
        # If transition not found, treat the entire sentence as part1
        part1 = sentence
        part2 = ""
    return pd.Series([part1, part2])

# Apply the function
df[['part1_sentence', 'part2_sentence']] = df.apply(split_with_transition, axis=1)



# Optional: remove extra spaces in parts
for col in ['part1_sentence', 'part2_sentence']:
    df[col] = df[col].apply(lambda x: " ".join(str(x).strip().split()))

# Save the cleaned dataset
df.to_csv("../DataSets/dataset_split_with_transition.csv", index=False, encoding='utf-8-sig')

print("✅ Sentences split successfully. Transition and sentence correctly stored in part2.")
