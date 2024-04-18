import csv

def find_common_words(csv1_path, csv2_path, common_csv_path, remaining_csv_path):
    common_words_set = set()

    with open(csv1_path, 'r') as file1:
        reader1 = csv.reader(file1)
        for row in reader1:
            common_words_set.update(word.lower() for word in row)

    with open(csv2_path, 'r') as file2:
        reader2 = csv.reader(file2)
        #for word in next(reader2, []):
        for row in reader2:
            for word in row:
                common_words_set.intersection_update(word.lower())
                print(word.lower())

    # Write common words to a new CSV file
    with open(common_csv_path, 'w', newline='') as common_file:
        writer_common = csv.writer(common_file)
        writer_common.writerow(list(common_words_set))

    # Write remaining words to a new CSV file
    with open(remaining_csv_path, 'w', newline='') as remaining_file:
        writer_remaining = csv.writer(remaining_file)
        remaining_words = set()

        with open(csv1_path, 'r') as file1:
            reader1 = csv.reader(file1)
            for row in reader1:
                remaining_words.update(word.lower() for word in row)

        with open(csv2_path, 'r') as file2:
            reader2 = csv.reader(file2)
            for row in reader2:
                remaining_words.update(word.lower() for word in row)

        remaining_words -= common_words_set
        writer_remaining.writerow(list(remaining_words))

csv1 = '/Users/jasminezhang/thesis/expanded_nyt.csv'
csv2 = '/Users/jasminezhang/thesis/mesh_keywords.csv'
intersection = '/Users/jasminezhang/thesis/intersecting_keywords.csv'
irrelevant = '/Users/jasminezhang/thesis/irrelevant_keywords.csv'

find_common_words(csv1, csv2, intersection, irrelevant)