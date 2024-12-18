import json
from googletrans import Translator
from google.colab import files

# Loading the JSON file
with open('/content/20240803.json', 'r') as file:
    data = json.load(file)

translator = Translator()

# Translate solely "content" phrases
for message in data.get("messages", []):
    if "content" in message:
        # Extract and translate text within quotes
        content = message["content"]
        translated_phrases = []
        for phrase in content.split('"'):
            if phrase.strip():
                # Translate only text within quotes
                translated = translator.translate(phrase, src='en', dest='pt').text
                translated_phrases.append(translated)
            else:
                translated_phrases.append(phrase)
        # Rebuild content with translated phrases
        message["content"] = '"'.join(translated_phrases)

# Saving the updated JSON back to file
output_path = '/content/translated_20240803.json'
with open(output_path, 'w') as file:
    json.dump(data, file, ensure_ascii=False, indent=4)

print(f"Translation completed. Updated file saved to: {output_path}")

# Download the file to local machine
files.download(output_path)