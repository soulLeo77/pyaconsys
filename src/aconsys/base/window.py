from uiautomation import WindowControl


class BaseWindow:
    """Clase base para manejar ventana de ACONSYS."""

    _window: WindowControl

    @classmethod
    def exists(cls) -> bool:
        window = cls._window
        return window.Exists(maxSearchSeconds=0)

    @classmethod
    def wait_for(cls, timeout: int = 15) -> None:
        window = cls._window
        assert window.Exists(timeout)
        return None

    @classmethod
    def close(cls) -> None:
        if not cls.exists():
            return None
        window = cls._window
        window_pattern = window.GetWindowPattern()
        assert window_pattern.Close()
        return None

    @classmethod
    def set_active(cls) -> None:
        window = cls._window
        if window.IsOffscreen:
            assert window.SetActive()
        return None


class TopLevelWindow(BaseWindow):
    """Ventana principal"""

    @classmethod
    def set_topmost(cls) -> None:
        window = cls._window
        if not window.IsTopmost():
            assert window.SetTopmost()
        return None

    @classmethod
    def wait_for(cls, timeout: int = 15) -> None:
        super().wait_for(timeout)
        cls.set_active()
        return cls.set_topmost()
