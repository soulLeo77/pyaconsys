from pathlib import Path
from subprocess import Popen

from loguru import logger

from ...base.window import TopLevelWindow
from ..main.window import MainWindow
from .controls import CONNECT_BUTTON, LOGIN_WINDOW, PASSWORD_EDIT, USERNAME_EDIT


class LoginWindow(TopLevelWindow):
    """Maneja el inicio de sesión en la aplicación ACONSYS."""

    _window = LOGIN_WINDOW
    _executable_file: Path
    _popen: Popen | None = None

    def __init__(self, executable_file_path: Path | str) -> None:
        self._executable_file: Path = Path(executable_file_path)
        if not self._executable_file.is_file():
            raise ValueError("Ruta al ejecutable inválida.")
        return super().__init__()

    def login(self, usename: str, password: str) -> MainWindow:
        """Inicia sesión en ACONSYS."""
        if MainWindow.exists():
            return MainWindow()

        if not self.exists():
            logger.info(f"Ejecutando ACONSYS: {self._executable_file}")
            self._popen = Popen(self._executable_file)

        self.wait_for()
        logger.info("Ventana de acceso detectada. Ingresando contraseña...")

        username_edit = USERNAME_EDIT.GetValuePattern()
        username_edit.SetValue(usename)

        password_edit = PASSWORD_EDIT.GetValuePattern()
        password_edit.SetValue(password)

        connect_btn = CONNECT_BUTTON.GetInvokePattern()
        connect_btn.Invoke()

        if self.exists():
            raise RuntimeError(
                "Error en el inicio de sesión (contraseña incorrecta o ventana no respondió)."
            )

        logger.success("Inicio de sesión exitoso.")
        return MainWindow()
