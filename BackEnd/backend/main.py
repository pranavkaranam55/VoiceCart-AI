from backend.speech_to_text import transcribe_audio
from backend.order_parser import extract_order
from backend.database import save_orders


def process_order(audio_file):

    result = transcribe_audio(audio_file)

    language = result["language"]
    text = result["text"]

    orders = extract_order(text)

    save_orders(orders, language)

    return {
        "language": language,
        "transcribed_text": text,
        "orders": orders
    }