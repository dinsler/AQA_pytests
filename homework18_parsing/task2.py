"""
Implement provided methods. You need to convert the class instance to JSON or XML. When the user provides the command
 json to cli, the program should call convert_to_json, when providing xml to cli program should
 convert the class instance to xml string.
And print it, or even better write it to a separate file.
You can use third parties libraries for this. If you use such a library please add it to requirement.txt
"""
import json
import xml.etree.ElementTree as ET


class Human:
    def __init__(self, name, age, gender, birth_year):
        self.name = name
        self.age = age
        self.gender = gender
        self.birth_year = birth_year

    def convert_to_json(self):
        return json.dumps(self.__dict__)

    def get_xml_text(self, human_data):
        for key, value in self.__dict__.items():
            ET.SubElement(human_data, key).text = str(value)

    def convert_to_xml(self):
        human_data = ET.Element('Human')
        self.get_xml_text(human_data)
        return ET.tostring(human_data, encoding='utf8').decode('utf8')

    @classmethod
    def convert_to_json_or_xml(cls, command: str, *args):
        """
        :param command: str 'json' or 'xml'
        """
        human = cls(*args)
        if command == 'json':
            json_human_data = human.convert_to_json()
            with open('json_human_data.json', 'w') as file:
                file.write(json_human_data)
        elif command == 'xml':
            xml_human_data = human.convert_to_xml()
            with open('xml_human_data.xml', 'w') as file:
                file.write(xml_human_data)
        else:
            raise Exception('Only "json" or "xml" command supported')


if __name__ == '__main__':
    Human.convert_to_json_or_xml('json', 'Marko', 23, 'male', 1992)
    Human.convert_to_json_or_xml('xml', 'Marko', 23, 'male', 1992)
