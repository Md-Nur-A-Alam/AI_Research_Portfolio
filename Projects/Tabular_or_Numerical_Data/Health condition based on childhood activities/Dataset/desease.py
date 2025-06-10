import pandas as pd

df = pd.read_excel("desease_list.xlsx")  # This will now work


# Define your disease list (English part only, for clean column names)
disease_list = [
    "Obesity",
    "ADHD",
    "Anxiety",
    "Depression",
    "Scoliosis",
    "Asthma",
    "Sleep Disorder",
    "Vitamin D Deficiency",
    "Speech/Language Delay",
    "Postural Issues/Chronic Back Pain",
    "Allergies",
    "Carpal Tunnel Syndrome"
]

# Clean the text: remove Bangla in parentheses, then split by comma
df['Cleaned'] = df['33. Current_problems'].str.replace(r'\([^)]*\)', '', regex=True)
df['Cleaned'] = df['Cleaned'].str.split(',')

# Strip whitespace
df['Cleaned'] = df['Cleaned'].apply(lambda x: [i.strip() for i in x])

# Create 0/1 columns for each disease
for disease in disease_list:
    df[disease] = df['Cleaned'].apply(lambda x: 1 if disease in x else 0)

# Drop the helper column if not needed
df.drop(columns=['Cleaned'], inplace=True)

# Save the updated data to a new Excel file
df.to_excel("disease_onehot_output.xlsx", index=False)
