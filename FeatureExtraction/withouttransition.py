import pandas as pd

# Load your original dataset
df = pd.read_csv("../Merged_dataset.csv")  # Or whatever your original file is

# Remove transition from part2_sentence
def split_without_transition(row):
    sentence = str(row['Sentence']).strip()
    transition = str(row['Transition Word']).strip()

    if transition in sentence:
        before, after = sentence.split(transition, 1)
        part1 = before.strip()
        part2 = after.strip()  # transition excluded here
    else:
        part1 = sentence.strip()
        part2 = ""
    return pd.Series([part1, part2])

df[['part1_sentence', 'part2_sentence']] = df.apply(split_without_transition, axis=1)

# Clean sentiment columns
df['Part1 Sentiment'] = df['Part1 Sentiment'].str.strip()
df['Part2 Sentiment'] = df['Part2 Sentiment'].str.strip()

# Clean spacing in parts
for col in ['part1_sentence', 'part2_sentence']:
    df[col] = df[col].apply(lambda x: " ".join(str(x).strip().split()))

# Save to a new file
df.to_csv("dataset_split_without_transition.csv", index=False, encoding='utf-8-sig')

print("✅ Dataset created with transition excluded from part2_sentence.")
