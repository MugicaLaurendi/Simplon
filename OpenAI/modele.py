import openai
import deepl


def traduct(file_to_convert) :

    audio_file= open(file_to_convert, "rb")

    openai.api_key = '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'

    transcript = openai.Audio.transcribe("whisper-1", audio_file)["text"]

    #file_convert = transcript["text"]

    def clean_texte(texte):
        texte = texte.replace(". ", ".\n")
        texte = texte.replace("? ", ".\n")
        texte = texte.replace("! ", ".\n")
        return texte

    auth_key = "4c4edf95-8ccc-93ec-a1fb-4503f21f0967:fx"  # Replace with your key
    translator = deepl.Translator(auth_key)

    result = translator.translate_text(transcript, target_lang="FR")
    print(result.text)

bob = "angela.mp3"

traduct(bob)
