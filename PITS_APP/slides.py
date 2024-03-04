### TODO: 
# - persist audio files in Slide

import json

class SlideDeck:
    def __init__(self, topic, slides):
        self.topic = topic
        self.slides = slides

    def to_dict(self):
        return {
            'topic': self.topic,
            'slides': [slide.to_dict() for slide in self.slides]
        }

    def save_to_file(self, filename):
        with open(filename, 'w') as file:
            json.dump(self.to_dict(), file, indent=4)

    @classmethod
    def load_from_file(cls, filename):
        with open(filename, 'r') as file:
            data = json.load(file)
            slides = [Slide(**slide_data) for slide_data in data['slides']]
            return cls(data['topic'], slides)


class Slide:
    def __init__(self, section, topic, narration, bullets):
        self.section = section
        self.topic = topic
        self.narration = narration
        self.bullets = bullets

    def to_dict(self):
        return {
            'section': self.section,
            'topic': self.topic,
            'narration': self.narration,
            'bullets': self.bullets
        }
        
    def render(self, display_narration=False):
        markdown_text = f"# {self.section}\n## {self.topic}\n"
        for index, bullet in enumerate(self.bullets, start=1):
            markdown_text += f"{index}. {bullet.strip()}\n\n"
        if display_narration:
            markdown_text += "---\n\n\n"  # Separator line
            markdown_text += f"*{self.narration}*"
        return markdown_text