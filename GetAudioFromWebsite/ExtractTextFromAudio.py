from faster_whisper import WhisperModel


def transcribe_with_whisper_to_file(mp3_file_path, output_txt_path):
    # Load the model
    model = WhisperModel("base", device="cpu", compute_type="int8")

    # Transcribe the audio
    segments, info = model.transcribe(mp3_file_path)

    # Combine all segments and save to file
    with open(output_txt_path, 'w', encoding='utf-8') as f:
        for segment in segments:
            f.write(segment.text + " ")

    print(f"Transcription saved to {output_txt_path}")


# Usage
transcribe_with_whisper_to_file("C:/Users/Jomo/Desktop/listingSourceFiles/34-C2.mp3", "C:/Users/Jomo/Desktop/listingSourceFiles/34-C2.txt")