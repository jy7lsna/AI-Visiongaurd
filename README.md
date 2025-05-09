# AI VisionGuard

**AI VisionGuard** is an intelligent, contactless security system that uses facial recognition to control access to physical spaces. By combining Python-based AI vision with an Arduino-controlled lock, buzzer, and LED, this project provides a modern, secure, and user-friendly solution for doors, lockers, or other restricted areas.

---

## 🚀 Features

- **Real-Time Face Recognition:** Uses your webcam and AI to detect and recognize authorized faces.
- **Secure Access Control:** Only unlocks for authorized users; triggers alerts for unauthorized attempts.
- **Arduino Integration:** Controls a servo lock, buzzer, and LED based on recognition results.
- **Easy to Use:** Simple setup and clear feedback via hardware indicators.
- **Customizable:** Easily add more authorized users or modify hardware actions.

---

## 🛠️ Hardware & Software Requirements

### Hardware

- Computer with webcam
- Arduino Uno (or compatible)
- Servo motor (for lock mechanism)
- Buzzer
- LED
- Jumper wires, breadboard
- USB cable (for Arduino)

### Software

- Python 3.x
- [face_recognition](https://github.com/ageitgey/face_recognition) Python library
- OpenCV (`cv2`)
- pyserial
- Arduino IDE

---

## 📦 Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/ai-visionguard.git
cd ai-visionguard
```


### 2. Install Python Dependencies

Make sure you have Python 3 installed. Then, install the required libraries:

```bash 
pip install face_recognition opencv-python pyserial
```

If you encounter errors with `face_recognition`, also install:

```bash 
pip install cmake dlib
```


### 3. Prepare the Authorized Face Image

- Place a clear, front-facing photo of the authorized user in the project folder.
- Name it `user1.jpg` (or update the code if you use a different name).

### 4. Wire the Arduino

- **Servo:** Signal to pin 9, VCC to 5V, GND to GND.
- **Buzzer:** Positive to pin 4, negative to GND.
- **LED:** Anode (long leg) to pin 5 (with resistor), cathode to GND.

See the diagram below (or check `/docs/arduino_wiring.png` if you provide one).

### 5. Upload the Arduino Code

- Open `arduino_code.ino` in Arduino IDE.
- Select the correct board and port.
- Upload the code to your Arduino.

### 6. Connect Arduino to Your Computer

- Use a USB cable to connect the Arduino.

### 7. Run the Python Script


