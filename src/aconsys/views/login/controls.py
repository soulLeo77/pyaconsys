from uiautomation import WindowControl

LOGIN_WINDOW = WindowControl(searchDepth=1, Name="Acceso al Sistema")

USERNAME_EDIT = LOGIN_WINDOW.EditControl(AutomationId="") # Falta encontrar el identificador del username
PASSWORD_EDIT = LOGIN_WINDOW.EditControl(AutomationId="3")
CONNECT_BUTTON = LOGIN_WINDOW.ButtonControl(Name="Conectar")
