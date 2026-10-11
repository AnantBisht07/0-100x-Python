class UpperCase:
    @staticmethod
    def shout(text):
        return text.upper()

text = "Sangeeta"
print(f"UpperCase is {UpperCase.shout(text)}")