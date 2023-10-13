import os
import time

def add_layout_tag_to_xml(xml_file_path):
    # Read the content of the XML file
    with open(xml_file_path, 'r') as file:
        xml_content = file.read()

    #Trim the content of the XML file
    xml_content = xml_content.strip()

    # Check if the "<layout>" tag is present in the file and file does not ends with "</layout>"
    if '<layout' not in xml_content and not xml_content.endswith('</layout>'):
        # Add the "<layout>" tag after "?>" at the beginning of the file
        xml_content = xml_content.replace('?>', '?>\n<layout>\n')

        # Add the closing "</layout>" tag at the end of the file
        xml_content += '\n</layout>\n'

        # Write the modified content back to the file
        with open(xml_file_path, 'w') as file:
            file.write(xml_content)

        print(f"Successfully added <layout> tag to {xml_file_path}")
    else:
        print(f"File {xml_file_path} is already in the correct format")

def test_single_file(xml_file_path):
    if not os.path.exists(xml_file_path):
        print(f"File not found: {xml_file_path}")
        return

    # Test and modify the specified XML file
    add_layout_tag_to_xml(xml_file_path)

# Specify the path to the XML file you want to test
xml_file_path = "/Users/user/Projects/Android/project_name/app/src/main/res/layout/activity_full_image.xml"

def process_directory_with_sleep(directory_path, sleep_duration):
    for root, dirs, files in os.walk(directory_path):
        for file in files:
            if file.endswith(".xml"):
                file_path = os.path.join(root, file)
                add_layout_tag_to_xml(file_path)
                time.sleep(sleep_duration)  # Sleep for the specified duration

# Specify the path to the directory containing XML files
directory_path = "/Users/user/Projects/Android/project_name/app/src/main/res/layout/"

# Specify the sleep duration between edits (in seconds)
sleep_duration = 0.1  # Adjust this as needed

# Process the directory with sleep
process_directory_with_sleep(directory_path, sleep_duration)
# Test the specified XML file
# test_single_file(xml_file_path)
