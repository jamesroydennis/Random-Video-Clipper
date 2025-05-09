# 🎬 Video Montage Creator

This Python script creates a 20-minute montage by:
- Randomly selecting 10 `.mp4` videos from a given folder
- Extracting a 2-minute random clip from each
- Concatenating all 10 clips into a single video using FFmpeg

---

## ✅ Requirements

- **Python 3.8+**
- **FFmpeg** (`ffmpeg` and `ffprobe`) must be installed and in your system PATH
- No external Python packages required

---

## 📁 Folder Structure


> You can store your `.mp4` files in any folder; just pass the path when running the script.

---

## ⚙️ Installation

1. Create and activate a conda environment:

    ```bash
    conda create -n video_montage_env python=3.11
    conda activate video_montage_env
    ```

2. (Optional) Install from `requirements.txt`:

    ```bash
    pip install -r requirements.txt
    ```

3. Confirm FFmpeg is available in your system PATH:

    ```bash
    ffmpeg -version
    ffprobe -version
    ```

---

## 🚀 Usage

Run the script from the terminal or Anaconda Prompt, passing the folder containing your `.mp4` files:

```bash
python main.py "D:\MyVideos\RawFootage"
