import whisper
from word2number import w2n
from deep_translator import GoogleTranslator

model = whisper.load_model("small")


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

    result = model.transcribe(audio_path)

    original_text = result["text"]

    print("Language:", result["language"])
    print("Original Text:", original_text)

    try:

        translated_text = GoogleTranslator(
            source="auto",
            target="en"
        ).translate(original_text)

        if translated_text is None:
            translated_text = original_text

    except Exception as e:

        print("Translation Error:", e)

        translated_text = original_text

    print("Translated Text:", translated_text)

    text = translated_text.lower()

    cleaned_text = convert_number_words(text)

    return {
        "language": result["language"],
        "text": cleaned_text
    }