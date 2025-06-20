#Normalizing the data to ensure consistency

import pandas as pd
from indicnlp import common
from indicnlp.normalize.indic_normalize import IndicNormalizerFactory

# Set path to the resources folder
INDIC_RESOURCES_PATH = "../indic_nlp_resources"  
common.set_resources_path(INDIC_RESOURCES_PATH)

# Create the normalizer for Kannada
factory = IndicNormalizerFactory()
normalizer = factory.get_normalizer("kn")

# Load your dataset
df = pd.read_csv("../dataset_1.csv")

# Normalize sentence in kannada
df['Column1'] = df['Column1'].apply(lambda x: normalizer.normalize(str(x)))


# Save cleaned version
df.to_csv("../dataset_1.csv", index=False)
print("Kannada text normalized and saved.")

