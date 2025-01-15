# Brain-Controlled Smart Home System

Control your smart home devices using brainwaves with the help of an EEG headset and a Raspberry Pi. This system allows for hands-free and efficient management of home appliances.

---

## What Controls What?

| **Brainwave Activity** | **Controlled Device**     | **Action**                     |
|-------------------------|---------------------------|---------------------------------|
| Focus Level             | Light                    | Turn ON/OFF                   |
| Relaxation Level        | Fan                      | Turn ON/OFF                   |
| Intensity Level         | Door Lock               | Lock/Unlock                   |
| Calmness Level          | Curtain                 | Open/Close                    |
| Overall Brain Activity  | Thermostat              | Turn ON/OFF                   |

---

## Materials Needed

- **Raspberry Pi** (with GPIO support)
- **EEG Headset** (e.g., Muse, OpenBCI)
- **Relay Modules** (to control appliances)
- Smart devices: Lights, Fans, Door Locks, Curtains, Thermostat
- Wires and Connectors
- Power Supply for Raspberry Pi

---

## Setup Process

### 1. Hardware Setup
1. **Connect Devices to Raspberry Pi:**
   - Use relay modules to connect smart devices (light, fan, etc.) to the GPIO pins on the Raspberry Pi.
   - Refer to `config.json` for assigning pins to each device.

2. **Set Up EEG Headset:**
   - Pair your EEG headset (e.g., via Bluetooth) with the Raspberry Pi.
   - Ensure the headset software or library is installed.

---

### 2. Software Setup

1. **Install Python and Libraries**
   - Ensure Python 3.7+ is installed on your Raspberry Pi.
   - Install required libraries using pip:
     ```bash
     sudo apt update
     sudo apt install python3-pip
     pip install RPi.GPIO
     pip install muse-lsl  # Replace with your EEG headset's library
     ```

2. **Clone the Repository**
   - Clone the project from GitHub:
     ```bash
     git clone https://github.com/your-username/brain-controlled-smart-home.git
     cd brain-controlled-smart-home
     ```

3. **Configure the System**
   - Open `config.json` to set up GPIO pins and brainwave thresholds:
     ```json
     {
       "devices": {
         "light": 17,
         "fan": 27,
         "lock": 22,
         "curtain": 23,
         "thermostat": 24
       },
       "thresholds": {
         "focus": 70,
         "relaxation": 60,
         "intensity": 80,
         "calm": 65,
         "overall_activity": 75
       }
     }
     ```

---

### 3. Run the System

1. **Start the Main Program**
   - Run the main Python script:
     ```bash
     python3 main.py
     ```

2. **Monitor Logs**
   - Check `logs/system_log.txt` for activity logs and troubleshooting.

---

## Benefits of This System

- Hands-free, brain-controlled device management.
- Enhances accessibility for people with disabilities.
- Eco-friendly and energy-efficient.

---

## Future Improvements

- Add mobile app integration for remote control.
- Integrate machine learning for personalized brainwave thresholds.
- Include energy consumption monitoring.

---

## Troubleshooting

1. **Device Not Responding?**
   - Ensure correct GPIO pin connections and check `config.json`.
   
2. **EEG Headset Not Connecting?**
   - Verify that the headset is paired and its library is installed.

3. **Script Errors?**
   - Ensure all required Python libraries are installed.
   - Check logs for detailed error messages.

---

## Contributing

We welcome contributions! Follow these steps:
1. Fork the repository.
2. Create a feature branch (`feature-branch`).
3. Commit your changes.
4. Submit a pull request.

---

## project for INNOVATIVE MINDS 2025




