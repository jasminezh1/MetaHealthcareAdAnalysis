import xml.etree.ElementTree as ET

# Replace 'your_file.xml' with the path to your MeSH XML file
file_path = '/Users/jasminezhang/Downloads/desc2024.xml'
output_path = '/Users/jasminezhang/Downloads/mesh_headings.txt'

# Parse the XML file
tree = ET.parse(file_path)
root = tree.getroot()

with open(output_path, 'w') as file:
        for descriptor in root.findall('.//DescriptorName/String'):
            # Write each term to the file followed by a newline
            file.write(descriptor.text + '\n')

print(f"MeSH terms successfully written to {output_path}")
# # Extract and print DescriptorName values
# for descriptor in root.findall('.//DescriptorName/String'):
#     print(descriptor.text)