import speech_recognition as sr

from services.bluetooth_service import BluetoothService
from services.console_service import print_microphone
from services.database_service import DatabaseService
from services.door_service import DoorService


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

    def listen(self) -> None:
        if len(self.b_service.devices_in_range) == 0:
            return

        print_microphone('You can talk now:')
        input_text = MicrophoneService._get_audio()
        for word in input_text.split():
            self.match_word(word)

    @staticmethod
    def _get_audio() -> str:
        r = sr.Recognizer()
        mic = sr.Microphone(device_index=1)
        with mic as source:
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source)
            said = ''

            try:
                said = r.recognize_google(audio)
            except Exception as e:
                print("Exception: " + str(e))
        return said.lower()
