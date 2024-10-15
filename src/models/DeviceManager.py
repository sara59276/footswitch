from usbmonitor import USBMonitor
from usbmonitor.attributes import ID_MODEL_ID, ID_VENDOR_ID, ID_MODEL_FROM_DATABASE

from constants.footswitch_ids import FOOTSWITCH_FS22PM_MODEL_ID, FOOTSWITCH_FS22PM_VENDOR_ID


class DeviceManager:

    @staticmethod
    def is_footswitch_plugged_in() -> bool:
        devices = DeviceManager.get_all_current_devices()

        for device_id, model_id, vendor_id in devices:
            if model_id == FOOTSWITCH_FS22PM_MODEL_ID and vendor_id == FOOTSWITCH_FS22PM_VENDOR_ID:
                return True

        return False

    @staticmethod
    def get_all_current_devices():
        monitor = USBMonitor()
        devices_dict = monitor.get_available_devices()

        devices_list = [(key, value[ID_MODEL_ID], value[ID_VENDOR_ID]) for key, value in devices_dict.items()]

        print("devices list:\n", devices_list)

        return devices_list