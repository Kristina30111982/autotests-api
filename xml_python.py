import xml.etree.ElementTree as ET

xml_data = """
<user>
    <id>1</id>
    <first_name>John</first_name>
    <last_name>Doe</last_name>
    <email>john.doe@example.com</email>
</user>    
"""

root = ET.fromstring(xml_data)
print(root.find("first_name").text)
print("User Emil:", root.find("email").text)