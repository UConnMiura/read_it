import sys
import soundfile as sf
from kokoro_onnx import Kokoro

def sanitize_text(text):
    """Sanitize text by replacing smart quotes and normalizing spacing."""
    replacements = {
        "“": '"', "”": '"',  # Smart double quotes → standard "
        "‘": "'", "’": "'",  # Smart single quotes → standard '
        "\n": " ",           # Replace newlines with spaces
        "\r": "",            # Remove carriage returns
    }
    for old, new in replacements.items():
        text = text.replace(old, new)
    
    return " ".join(text.split())  # Remove extra spaces

def main():
    if len(sys.argv) < 2:
        print("Usage: uv run hello4.py <file.txt>")
        return
    
    filename = sys.argv[1]
    
    try:
        with open(filename, "r", encoding="utf-8") as f:
            text = f.read().strip()
        
        if not text:
            print("Error: The file is empty.")
            return

        sanitized_text = sanitize_text(text)

        kokoro = Kokoro("kokoro-v1.0.onnx", "voices-v1.0.bin")
        samples, sample_rate = kokoro.create(sanitized_text, voice="af_sarah", speed=1.0, lang="en-us")

        output_filename = "audio.wav"
        sf.write(output_filename, samples, sample_rate)
        print(f"Created {output_filename} from {filename}")

    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
