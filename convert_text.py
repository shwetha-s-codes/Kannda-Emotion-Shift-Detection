import os
#spliting the data into pdf's
def split_large_text_file(input_file, output_folder, lines_per_file=1000):
    # Create the output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)

    # Read the large text file
    with open(input_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    # Split the lines into smaller chunks
    for i in range(0, len(lines), lines_per_file):
        chunk = lines[i:i + lines_per_file]
        output_file = os.path.join(output_folder, f"split_{i // lines_per_file + 1}.txt")
        
        # Write the chunk to a new text file
        with open(output_file, 'w', encoding='utf-8') as out_f:
            out_f.writelines(chunk)
        
        print(f"Created: {output_file}")

# Specify the input file, output folder, and lines per file
input_file = r"C:\Users\Hp\Downloads\archive\cc100\kn.txt"
output_folder = r"C:\Users\Hp\OneDrive\Desktop\Data_Collection\split_data"
lines_per_file = 10000

# Call the function
split_large_text_file(input_file, output_folder, lines_per_file)