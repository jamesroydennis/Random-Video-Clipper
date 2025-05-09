<<<<<<< HEAD
Absolutely — here’s the **updated `README.md`** with all your requested notes included.

---

### 📄 `README.md`

```markdown
# 🎬 Video Montage Creator

This Python script creates a 20-minute montage by:
- Randomly selecting 10 `.mp4` videos from a given folder
- Extracting a 2-minute random clip from each
- Concatenating all 10 clips into a single video using FFmpeg

---

## ✅ Requirements

- **Python 3.8+**
- **FFmpeg** (including `ffmpeg` and `ffprobe`) must be installed and in your system PATH
- No external Python packages required

---

## 📁 Folder Structure

```

video\_montage/
├── main.py
├── requirements.txt
└── README.md

````

> You can store your `.mp4` files in any folder; just pass the path when running the script.

---

## ⚙️ Installation

1. Create and activate a conda environment:

```bash
conda create -n video_montage_env python=3.11
conda activate video_montage_env
````

2. (Optional) Install from `requirements.txt` (empty if not using additional libraries):

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
```

The script will:

* Create an `output/` folder inside your target directory
* Save 10 temporary clips as `clip_0.mp4` to `clip_9.mp4`
* Concatenate them into `final_video.mp4` in the same `output/` folder

---

## 🧼 Notes

* **Temporary clips** are **retained** after final concatenation, which can be useful for debugging or further editing.
* All clips are extracted using `-c copy` (stream copy) in FFmpeg, which means:

  * No re-encoding (faster execution)
  * Source and output must be compatible (same codec/container)
* If a selected video is **shorter than 2 minutes**, the entire video is included starting at time `0:00`.
* FFmpeg must be installed and **`ffmpeg.exe` and `ffprobe.exe` must be in your system PATH**.
* Only `.mp4` files are processed; other formats are ignored.

---

## 🧩 Future Ideas

* Support for user-defined:

  * Clip duration
  * Number of clips
* Optional automatic deletion of temporary clips after final video creation
* GUI version with drag-and-drop or folder picker (Tkinter / PyQt)

---

Built with ❤️ using Python and FFmpeg.

```

Would you like me to add a command-line flag (e.g., `--cleanup`) to automatically delete temporary clips if desired?
```

=======
# Random-Video-Clipper
>>>>>>> d004766d0e8549988aa2a0b801d2841345775e35
