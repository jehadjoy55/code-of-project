import RPi.GPIO as GPIO

# Initialize GPIO
def setup_gpio(config):
    GPIO.setmode(GPIO.BCM)
    for device, pin in config["devices"].items():
        GPIO.setup(pin, GPIO.OUT)
        GPIO.output(pin, GPIO.LOW)  # Ensure all devices are off initially

def control_device(device, state, config):
    pin = config["devices"].get(device)
    if pin is None:
        raise ValueError(f"Invalid device: {device}")
    
    GPIO.output(pin, GPIO.HIGH if state == "on" else GPIO.LOW)
    print(f"{device.capitalize()} turned {state.upper()}")
