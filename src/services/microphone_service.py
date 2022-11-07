from services.bluetooth_service import BluetoothService
from services.door_service import DoorService
from services.console_service import print_microphone
from services.database_service import DatabaseService

import gtts
import speech_recognition as sr
import time


class MicrophoneService:

    def __init__(self, bluetooth_service: BluetoothService) -> None:
        self.b_service: BluetoothService = bluetooth_service
        self.db_service: DatabaseService = self.b_service.db_service
        self.d_service: DoorService = DoorService(self.db_service)

    def match_word(self, word: str) -> None:
        print_microphone('Received word: %s' % word)

        addresses: list = []
        for device in self.b_service.devices_in_range:
            addresses.append(device.get('bd_addr'))

        if len(addresses) == 0:
            print_microphone('No Bluetooth devices in the near!')
            return

        for current in self.db_service.get_commands_for_bd_addresses(addresses):
            user_id: int = current.get('user_id')
            if current.get('cmd_open') == word:
                self.d_service.open(user_id)
            elif current.get('cmd_close') == word:
                self.d_service.close(user_id)
            elif current.get('cmd_lock') == word:
                self.d_service.lock(user_id)
            elif current.get('cmd_unlock') == word:
                self.d_service.unlock(user_id)
            else:
                print_microphone(f'No match with user {user_id}!')

    def get_audio(self):
        r = sr.Recognizer()
        mic = sr.Microphone(device_index=1)
        with mic as source:
            print("You can talk now")
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source)
            said = ''

            try:
                said = r.recognize_google(audio)
                print(said)
            except Exception as e:
                print("Exception: " + str(e))
        return said.lower()

    def listen(self):
        while True:
            text = self.get_audio()
            if "close" in text:
                print_microphone("Heard word 'close'")
            time.sleep(1)
