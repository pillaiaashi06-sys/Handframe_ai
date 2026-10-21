\# HandFrame AI 🖐️



A real-time computer vision project that uses hand gestures to control a virtual frame with a thermal-style heatmap effect.



\## Features



\- Real-time webcam processing using OpenCV

\- Hand tracking using MediaPipe

\- Frame movement controlled by the index fingertip

\- Frame resizing based on thumb-index finger distance

\- JET colour-mapped heatmap effect

\- Purple holographic grid and neon border




## 🛠️ Tech Stack

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![OpenCV](https://img.shields.io/badge/OpenCV-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white)
![MediaPipe](https://img.shields.io/badge/MediaPipe-4285F4?style=for-the-badge&logo=google&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white)
![Spyder](https://img.shields.io/badge/Spyder-FF0000?style=for-the-badge&logo=spyderide&logoColor=white)
![Git](https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white)
![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)




\## How It Works



The application detects hand landmarks from webcam frames. The index fingertip controls the frame position, while the distance between the thumb and index fingertip adjusts its size.



The live image inside the frame is converted to grayscale and mapped to colours using OpenCV's JET colour map.



\*\*Note:\*\* The heatmap is a visual effect based on image brightness, not actual body temperature.



\## Installation



1\. Install Python 3.11.

2\. Clone this repository.

3\. Install the required libraries:



&#x20;  `pip install -r requirements.txt`



4\. Run the application:



&#x20;  `python main.py`



Make sure your webcam is available. Press Q to exit.



\## Future Improvements



\- Face-centred heatmap

\- Multiple visual styles

\- Pinch-to-grab controls

\- Two-hand rotation and scaling



\## Project Status



Working prototype — under development.

