import csv

def remove_duplicates(input_csv, output_csv):
    unique_values = set()

    with open(input_csv, 'r', newline='') as infile:
        reader = csv.reader(infile)

        for row in reader:
            for cell in row:
                unique_values.add(cell)

    with open(output_csv, 'w', newline='') as outfile:
        writer = csv.writer(outfile)
        writer.writerow(list(unique_values))

input = '/Users/jasminezhang/thesis/extractednyt.csv'
output = '/Users/jasminezhang/thesis/uniquekeywords.csv'
remove_duplicates(input, output)