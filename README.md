# Read It

**Cut and Paste Dictation Using Kokoro**

This is a simple way to dictate some text on your Mac using Kokoro. Kokoro offers extensive customization and various voices, delivering speech quality close to paid services like Speechify. It significantly outperforms built-in dictation tools in most software and is free. Additionally, since everything runs locally, your text remains private.

I personally use this tool to dictate sensitive documents while reading. It helps me stay focused, especially when I struggle to concentrate on text.

## How It Works

The Python script, `hello4.py`, allows you to specify a text file, and it will generate an audio file with the spoken version of the text.

### Usage

Run the script with:

```sh
uv run hello4.py aims2.txt
```

This will generate a `.wav` file containing the speech output of the text in `aims2.txt`.

- **Input:** `aims2.txt` (or any text file you specify)
- **Output:** `audio.wav`

You can listen to `audio.wav` using Apple Music, VLC Player, or any media player that supports `.wav` files.

## Installation

1. Install [pipx](https://pypa.github.io/pipx/).
2. Install `uv`:
   ```sh
   pipx install uv
   ```
3. Initialize `uv` for Python 3.12:
   ```sh
   uv init -p 3.12
   ```
4. Copy the files kokoro-v1.0.onnx, and voices-v1.0.bin and place them in the same directory. These files are found here:https://pypi.org/project/kokoro-onnx/

5. Clone this repository:
   ```sh
   git clone https://github.com/yourusername/read_it.git
   cd read_it
   ```
6. Install dependencies:
   ```sh
   uv add kokoro-onnx soundfile
   ```
7. Run the script:
   ```sh
   uv run hello4.py aims2.txt
   ```

For more details on Kokoro, see its [PyPI page](https://pypi.org/project/kokoro-onnx/).

## Automating Execution

For convenience, I use a shell script called `run_kokoro` to simplify execution:

```sh
#!/bin/bash
uv add kokoro-onnx soundfile
uv run hello4.py aims2.txt
```

1. Save this script as `run_kokoro.sh`
2. Make it executable:
   ```sh
   chmod +x run_kokoro.sh
   ```
3. Run it anytime with:
   ```sh
   ./run_kokoro.sh
   ```

## License

This project is licensed under the MIT License. See below for details:

```
MIT License

Copyright (c) 2025 Your Name

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

---

Let me know if you'd like any modifications, such as adding examples or additional instructions!

