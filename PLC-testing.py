import snap7
from snap7.util import *
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Credentials and connection settings from .env file
plc_ip = os.getenv('PLC_IP')
plc_rack = int(os.getenv('PLC_RACK'))
plc_slot = int(os.getenv('PLC_SLOT'))
plc_user = os.getenv('PLC_USER')
plc_password = os.getenv('PLC_PASSWORD')

# A simple function to print the status of the PLC
def check_plc_status(client):
    status = client.get_cpu_state()
    print(f"CPU Status: {status}")

# Main management function
def manage_plc():
    client = snap7.client.Client()
    try:
        # Connect to the PLC
        client.connect(plc_ip, plc_rack, plc_slot)
        
        # Check if we are connected, this does not actually check the credentials but establishes a connection.
        if client.get_connected():
            print("Connected to PLC.")
            
            # Here you can add your PLC management code, for example:
            # Reading or writing to DBs, checking CPU state, etc.
            check_plc_status(client)

            # Remember to handle the security aspect and validate credentials as needed.
            # snap7 does not support direct user authentication, this is usually handled by the PLC itself.
            
        else:
            print("Connection failed.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        client.disconnect()

if __name__ == "__main__":
    manage_plc()
