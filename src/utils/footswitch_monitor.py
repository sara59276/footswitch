from usbmonitor import USBMonitor
from usbmonitor.attributes import ID_MODEL_ID, ID_VENDOR_ID
from config.config_manager import ConfigManager

class FootswitchMonitor:

    def __init__(self):
        self.config = ConfigManager()
        self.vendor_id = self.config.get('footswitch_vendor_id')
        self.model_id = self.config.get('footswitch_model_id')
        self.monitor = USBMonitor(filter_devices=[{'ID_VENDOR_ID': self.vendor_id, 'ID_MODEL_ID': self.model_id}])

    def start_monitoring(self, on_connect, on_disconnect) -> None:
        self.monitor.start_monitoring(on_connect=on_connect, on_disconnect=on_disconnect)

    def stop_monitoring(self) -> None:
        self.monitor.stop_monitoring()

    def is_footswitch_connected(self) -> bool:
        devices = self.get_all_current_devices()
        return any(vendor_id == self.vendor_id and model_id == self.model_id
                   for _, model_id, vendor_id in devices)

    def get_all_current_devices(self) -> list[tuple[str, str | tuple[str, ...], str | tuple[str, ...]]]:
        monitor = USBMonitor()
        devices_dict = monitor.get_available_devices()
        return [(key, value[ID_MODEL_ID], value[ID_VENDOR_ID]) for key, value in devices_dict.items()]