import serial
import time
PORT = 'COM5' 
BAUD_RATE = 9600

def read_from_port(ser):
    """Thread function to continuously read data from STM32."""
    while True:
        if ser.in_waiting > 0:
            data = ser.read(ser.in_waiting).decode('utf-8', errors='ignore')
            print(f"\r[STM32]: {data}", end='', flush=True)
            print("\n[You]: ", end='', flush=True)

try:
    # Initialize Serial Port
    ser = serial.Serial(PORT, BAUD_RATE, timeout=1)
    print(f"--- Connected to {PORT} at {BAUD_RATE} baud ---")
    print("Type characters to send to STM32 (Ctrl+C to exit)\n")

    # Start a background thread to listen for incoming data
    # thread = threading.Thread(target=read_from_port, args=(ser,), daemon=True)
    # thread.start()

    while True:
        for i in range (0,180):
            msg=str(i)
            while (len(msg)!=3):
                msg="0"+msg
            msg="A"+msg    
            print(msg)
            ser.write(msg.encode('utf-8'))
            time.sleep(0.05)    

except serial.SerialException as e:
    print(f"Error: Could not open port {PORT}. Is the Bluetooth paired and connected?")
except KeyboardInterrupt:
    print("\nExiting script...")
finally:
    if 'ser' in locals() and ser.is_open:
        ser.close()