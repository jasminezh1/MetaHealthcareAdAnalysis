import csv

def process_csv(input_file, output_file):
    # Read the input CSV file
    with open(input_file, 'r', newline='') as infile:
        reader = csv.reader(infile)
        data = list(reader)

    # Process the data and extract individual words
    processed_data = []
    for row in data:
        for cell in row:
            words = cell.split()  # Split the cell into words
            if len(words)>1:
                processed_data.append([cell] + words)
            else:
                processed_data.append([cell])

    # Write the processed data to a new CSV file
    with open(output_file, 'w', newline='') as outfile:
        writer = csv.writer(outfile)
        writer.writerows(processed_data)

# Example usage
input_csv_file = '/Users/jasminezhang/thesis/uniquekeywords.csv'
output_csv_file = '/Users/jasminezhang/thesis/2.csv'
process_csv(input_csv_file, output_csv_file)
