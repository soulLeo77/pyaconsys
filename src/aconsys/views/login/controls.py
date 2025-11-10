from uiautomation import WindowControl

LOGIN_WINDOW = WindowControl(searchDepth=1, Name="Acceso al Sistema")

USERNAME_EDIT = LOGIN_WINDOW.EditControl(
    AutomationId="", searchDepth=1
)  # Need find username identifier
PASSWORD_EDIT = LOGIN_WINDOW.EditControl(AutomationId="3", searchDepth=1)
CONNECT_BUTTON = LOGIN_WINDOW.ButtonControl(Name="Conectar", searchDepth=1)
