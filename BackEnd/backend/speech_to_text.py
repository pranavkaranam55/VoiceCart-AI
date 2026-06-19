import whisper
from word2number import w2n
from deep_translator import GoogleTranslator

model = whisper.load_model("tiny")


def convert_number_words(text):

    text = text.replace(" to ", " 2 ")
    text = text.replace(" too ", " 2 ")

    words = text.split()
    converted_words = []

    i = 0

    while i < len(words):

        found_number = False

        for j in range(min(4, len(words) - i), 0, -1):

            phrase = " ".join(words[i:i + j])

            try:
                number = w2n.word_to_num(phrase)

                converted_words.append(str(number))
                i += j
                found_number = True
                break

            except:
                pass

        if not found_number:
            converted_words.append(words[i])
            i += 1

    return " ".join(converted_words)


def transcribe_audio(audio_path):

    result = model.transcribe(
        audio_path,
        fp16=False
    )

    original_text = result["text"].strip()
    detected_language = result["language"]

    print("Language:", detected_language)
    print("Original Text:", original_text)

    translated_text = original_text

    if detected_language != "en":

        try:

            translated = GoogleTranslator(
                source="auto",
                target="en"
            ).translate(original_text)

            if translated:
                translated_text = translated

        except Exception as e:

            print("Translation Error:", e)

    print("Translated Text:", translated_text)

    cleaned_text = convert_number_words(
        translated_text.lower()
    )

    return {
        "language": detected_language,
        "text": cleaned_text
    }