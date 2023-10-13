import os
import time

def add_layout_tag_to_xml(xml_file_path):
    with open(xml_file_path, 'r') as file:
        xml_content = file.read()

    xml_content = xml_content.strip()

    if '<layout' not in xml_content and not xml_content.endswith('</layout>'):
        xml_content = xml_content.replace('?>', '?>\n<layout>\n')

        xml_content += '\n</layout>\n'

        with open(xml_file_path, 'w') as file:
            file.write(xml_content)

        print(f"Successfully added <layout> tag to {xml_file_path}")
    else:
        print(f"File {xml_file_path} is already in the correct format")

def test_single_file(xml_file_path):
    if not os.path.exists(xml_file_path):
        print(f"File not found: {xml_file_path}")
        return

    add_layout_tag_to_xml(xml_file_path)

xml_file_path = "/Users/user/Projects/Android/project_name/app/src/main/res/layout/activity_full_image.xml"

def process_directory_with_sleep(directory_path, sleep_duration):
    for root, dirs, files in os.walk(directory_path):
        for file in files:
            if file.endswith(".xml"):
                file_path = os.path.join(root, file)
                add_layout_tag_to_xml(file_path)
                time.sleep(sleep_duration) 

directory_path = "/Users/user/Projects/Android/project_name/app/src/main/res/layout/"

sleep_duration = 0.1 

process_directory_with_sleep(directory_path, sleep_duration)
# test_single_file(xml_file_path)
