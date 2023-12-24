from kivy.uix.scrollview import ScrollView
from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
# from kivy.app import App
from kivy.properties import ObjectProperty, StringProperty
# from kivy.core.window import Window

import spacy

model = spacy.load('model-best')

# Priyanshu is a MCA student from Chandigarh University. His hometown is in Bihar. He has completed BCA from Patna University. Recently applied for a Driving License in Bihar with the help of his ADHAAR and Voter Card. The ADHAAR number of Priyanshu is 4567xxxx7865 and the Voter ID number is SYG8827486. But the problem is that the address in the adhaar and the voter id mismatches. So therefore he was advised to provide his PAN Card having PAN no- AKKJM7865D and the Bank account passbook with an account in State Bank Of India, the account number is 63562782789.

Builder.load_file('ner.kv')

class PII(MDScreen):
    inputtext = ObjectProperty(None)
    output = StringProperty()

    def pii_detected(self):
        pii_detected = []
        output = model(self.inputtext.text)
        for word in output.ents:
            pii_detected.append(word.text)
        self.outtext = ",".join(pii_detected)
        self.output = self.outtext


class ner(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Amber"
        # self.theme_cls.primary_palette = "Orange"
        self.theme_cls.theme_style = "Dark"
        return PII()


if __name__ == "__main__":
    ner().run()

