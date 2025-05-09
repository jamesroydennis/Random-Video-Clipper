
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
