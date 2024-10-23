from usbmonitor import USBMonitor
from usbmonitor.attributes import ID_MODEL_ID, ID_VENDOR_ID

from config.ConfigManager import ConfigManager


class DeviceManager:

    config = ConfigManager()
    vendor_id = config.get('footswitch_vendor_id')
    model_id = config.get('footswitch_model_id')

    MONITOR = USBMonitor(filter_devices=[{'ID_VENDOR_ID': vendor_id, 'ID_MODEL_ID': model_id}])

    @staticmethod
    def start_monitoring(on_connect, on_disconnect) -> None:
        DeviceManager.MONITOR.start_monitoring(on_connect=on_connect, on_disconnect=on_disconnect)

    def stop_monitoring(self) -> None:
        DeviceManager.MONITOR.stop_monitoring()

    @staticmethod
    def is_footswitch_connected() -> bool:
        devices = DeviceManager.get_all_current_devices()

        for device_id, model_id, vendor_id in devices:
            if vendor_id == vendor_id and model_id == model_id:
                return True

        return False

    @staticmethod
    def get_all_current_devices() -> list[tuple[str, str | tuple[str, ...], str | tuple[str, ...]]]:
        monitor = USBMonitor()
        devices_dict = monitor.get_available_devices()
        devices_list = [(key, value[ID_MODEL_ID], value[ID_VENDOR_ID]) for key, value in devices_dict.items()]
        return devices_list