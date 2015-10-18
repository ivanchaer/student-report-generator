# This Python file uses the following encoding: utf-8 
from modules.Excel import Excel
from modules.Graph import Graph
from modules.Word import Word

class generate_reports():

    def __init__(self):
        data = self.get_data()
        self.generate_images(data)
        self.generate_reports(data)

    def file_naming_convention(self, string):
        remove_spaces = '-'.join(string.split()).lower()
        remove_special_characters = ''.join(ch for ch in remove_spaces if ch.isalnum() or ch == '-')
        return remove_special_characters
    
    def get_data(self): 

        # Initialize variable that will contain the data
        data = []

        # retrieve grades from Excel
        data.append(Excel().get_semester_grades('EERSTE TRIMESTER'))
        data.append(Excel().get_semester_grades('TWEEDE TRIMESTER'))

        return data;

    def generate_images(self, data):

        Graph().generate_images(data, self.file_naming_convention)

    def generate_reports(self, data):

        Word().generate_reports(data, self.file_naming_convention)


generate_reports()