#type:ignore
from Icii import *

class Vars(PythonAutomation): 
    def ApplyAutomation(self):

        for item in self.Items: 
            with self.CodeAfterAutomation :
                ((item)) = if_contains(dictionary, '((item))')