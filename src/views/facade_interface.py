from abc import ABC, abstractmethod
from tkinter import Tk
from typing import Callable, Tuple


class FacadeInterface(ABC):

    @abstractmethod
    def start_mainloop(self) -> None:
        pass

    @abstractmethod
    def bind_buttons(
            self,
            start_command: Callable,
            end_command: Callable,
            clear_command: Callable,
    ) -> None:
        pass

    @abstractmethod
    def bind_footswitch(
            self,
            footswitch_key: str,
            footswitch_pressed: Callable,
            footswitch_released: Callable,
    ) -> None:
        pass

    @abstractmethod
    def bind_entry_constraints(
            self,
            validate_scan_and_animal_inputs: Callable,
            validate_experimenter_input: Callable,
    ) -> None:
        pass

    @abstractmethod
    def bind_sheet(self, on_sheet_modified: Callable) -> None:
        pass

    @abstractmethod
    def bind_close_window_button(self, on_close_window_button: Callable) -> None:
        pass

    @abstractmethod
    def activate_start_button(self) -> None:
        pass

    @abstractmethod
    def deactivate_start_button(self) -> None:
        pass

    @abstractmethod
    def activate_end_button(self) -> None:
        pass

    @abstractmethod
    def deactivate_end_button(self) -> None:
        pass

    @abstractmethod
    def get_user_inputs(self) -> Tuple[str, str, str]:
        pass

    @abstractmethod
    def enable_user_inputs(self) -> None:
        pass

    @abstractmethod
    def disable_user_inputs(self) -> None:
        pass

    @abstractmethod
    def reset_user_inputs(self) -> None:
        pass

    @abstractmethod
    def add_start_time(self, start_time: str) -> None:
        pass

    @abstractmethod
    def add_end_time(self, end_time: str) -> None:
        pass

    @abstractmethod
    def set_sheet(self, data: list[list[str]]) -> None:
        pass

    @abstractmethod
    def append_empty_row(self) -> None:
        pass

    @abstractmethod
    def sheet_scroll_down(self) -> None:
        pass

    @abstractmethod
    def display_footswitch_released_icon(self) -> None:
        pass

    @abstractmethod
    def display_footswitch_pressed_icon(self) -> None:
        pass

    @abstractmethod
    def display_footswitch_disconnected(self) -> None:
        pass

    @abstractmethod
    def display_footswitch_connected(self) -> None:
        pass

    @abstractmethod
    def display_error(self, content: str) -> None:
        pass

    @abstractmethod
    def display_success(self, content: str) -> None:
        pass

    @abstractmethod
    def clear_msg(self) -> None:
        pass

    @abstractmethod
    def reset_view(self) -> None:
        pass

    @abstractmethod
    def get_sheet_content(self) -> object:
        pass

    @abstractmethod
    def get_root(self) -> Tk:
        pass