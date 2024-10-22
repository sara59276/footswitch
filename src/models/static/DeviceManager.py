from usbmonitor import USBMonitor
from usbmonitor.attributes import ID_MODEL_ID, ID_VENDOR_ID

from constants.footswitch_device import FOOTSWITCH_FS22PM_PRODUCT_ID_STR, FOOTSWITCH_FS22PM_VENDOR_ID_STR


class DeviceManager:

    MONITOR = USBMonitor(filter_devices=[{'ID_VENDOR_ID': FOOTSWITCH_FS22PM_VENDOR_ID_STR, 'ID_MODEL_ID': FOOTSWITCH_FS22PM_PRODUCT_ID_STR}])

    @staticmethod
    def start_monitoring(on_connect, on_disconnect) -> None:
        DeviceManager.MONITOR.start_monitoring(on_connect=on_connect, on_disconnect=on_disconnect)

    def stop_monitoring(self) -> None:
        DeviceManager.MONITOR.stop_monitoring()

    @staticmethod
    def is_footswitch_connected() -> bool:
        devices = DeviceManager.get_all_current_devices()

        for device_id, model_id, vendor_id in devices:
            if model_id == FOOTSWITCH_FS22PM_PRODUCT_ID_STR and vendor_id == FOOTSWITCH_FS22PM_VENDOR_ID_STR:
                return True

        return False

    @staticmethod
    def get_all_current_devices() -> list[tuple[str, str | tuple[str, ...], str | tuple[str, ...]]]:
        monitor = USBMonitor()
        devices_dict = monitor.get_available_devices()
        devices_list = [(key, value[ID_MODEL_ID], value[ID_VENDOR_ID]) for key, value in devices_dict.items()]
        return devices_list