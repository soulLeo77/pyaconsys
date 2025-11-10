import uiautomation as auto
from loguru import logger

from ...base.window import TopLevelWindow

MAIN_WINDOW = auto.WindowControl(RegexName="ACONSYS")


class MainWindow(TopLevelWindow):
    _window = MAIN_WINDOW

    def _navigate_to_menu_option(self, menu_name: str, option_name: str) -> None:
        """
        Abre una opción de menú (ej. 'Tablas' - 'Centro de Costos') desde la ventana principal.
        Funciona para menús clásicos de ACONSYS.
        """
        logger.info(f"Abrir menú '{menu_name}' - '{option_name}'...")

        self._window.SetActive()
        self._window.SetTopmost(True)
        logger.debug("Ventana principal activada y al frente.")

        menu_bar = self._window.MenuBarControl(searchDepth=1, AutomationId="MenuBar")
        logger.debug("Barra de menú encontrada.")

        menu_item = menu_bar.MenuItemControl(searchDepth=1, Name=menu_name)
        logger.debug(f"Menú '{menu_name}' encontrado, abriendo...")
        assert menu_item.GetInvokePattern().Invoke()
        logger.debug(f"Menú '{menu_name}' invocado correctamente.")

        tablas_menu = self._window.MenuControl(searchDepth=1, Name=menu_name)
        logger.debug(f"Submenú '{menu_name}' desplegado correctamente.")

        option_item = tablas_menu.MenuItemControl(searchDepth=1, Name=option_name)
        logger.debug(f"Opción '{option_name}' encontrada, ejecutando...")
        assert option_item.GetInvokePattern().Invoke()
        logger.success(f"'{menu_name} - {option_name}' abierto correctamente.")

    def download_centro_costos_file(self, file_name: str) -> None:
        ventana = self._window.WindowControl(Name="Mantenimiento de Centro de Costos")
        logger.debug(f"dentro de {ventana}")

        panel = ventana.PaneControl(searchDepth=1, ClassName="ImFrame3DWndClass")
        logger.debug(f"dentro de {panel}")

        imprimir = panel.ButtonControl(searchDepth=1, Name="Imprimir")
        assert imprimir.GetInvokePattern().Invoke()
        logger.debug(f"click hecho en {imprimir}")

        ventana_imprimir = auto.WindowControl(searchDepth=1, Name="Imprimir")
        logger.debug(f"Dentro de {ventana_imprimir}")

        panel_imprimir = ventana_imprimir.PaneControl(ClassName="SHELLDLL_DefView")
        logger.debug(f"Dentro de {panel_imprimir}")

        pdf_seleccionar = panel_imprimir.ListControl(Name="Vista de carpetas")
        logger.debug(f"Dentro de {pdf_seleccionar}")

        clic_pdf = pdf_seleccionar.ListItemControl(
            searchDepth=1, Name="Microsoft Print to PDF"
        )
        assert clic_pdf.GetSelectionItemPattern()
        logger.debug(f"click hecho en {clic_pdf}")

        clic_pdf_imprimir = ventana_imprimir.ButtonControl(
            searchDepth=1, Name="Imprimir"
        )
        assert clic_pdf_imprimir.GetInvokePattern().Invoke()
        logger.debug(f"CLick en {clic_pdf_imprimir}")

        ventana_principal = self._window.PaneControl(
            searchDepth=1, Name="Área de trabajo"
        )
        logger.debug(f"dentro de {ventana_principal}")

        ventana = ventana_principal.WindowControl(
            searchDepth=1, ClassName="ThunderRT6FormDC"
        )
        logger.debug(f"dentro de {ventana}")

        ventana_panel = ventana.PaneControl(searchDepth=1, Name="")
        logger.debug(f"dentro de {ventana_panel}")

        barra_principal = ventana_panel.TextControl(searchDepth=1, Name="")
        logger.debug(f"dentro de {barra_principal}")

        barra_oficial = barra_principal.PaneControl(searchDepth=1, Name="")
        logger.debug(f"dentro de {barra_oficial}")
        # TIENE VARIOS00000 HERMANOS
        barra_herramientas = barra_oficial.ToolBarControl(
            searchDepth=1, AutomationId="203"
        )  # ID PODRIA CAMBIAR
        logger.debug(f"dentro de {barra_herramientas}")

        icono_exportar = barra_herramientas.ButtonControl(
            searchDepth=1, Name="Exportar informe"
        )
        assert icono_exportar.GetInvokePattern().Invoke()
        logger.debug(f"Clic en icono de {icono_exportar}")

        ventana_export = self._window.WindowControl(searchDepth=1, Name="Export")
        logger.debug(f"dentro de {ventana_export}")

        ok_export = ventana_export.ButtonControl(searchDepth=1, Name="OK")
        assert ok_export.GetInvokePattern().Invoke()
        logger.debug(f"click en  {ok_export}")

        ok_export2 = self._window.WindowControl(searchDepth=1, Name="Export Options")
        logger.debug(f"dentro de {ok_export2}")

        clic_export2 = ok_export2.ButtonControl(searchDepth=1, Name="OK")
        assert clic_export2.GetInvokePattern().Invoke()
        logger.debug(f"click en {clic_export2}")

        ventana_guardar = self._window.WindowControl(
            searchDepth=1, Name="Choose export file"
        )
        logger.debug(f"Dentro de {ventana_guardar}")

        cuadro_nombre_pdf = ventana_guardar.PaneControl(
            searchDepth=1, Name="RptTablasComunConta"
        )
        logger.debug(f"dentro de {cuadro_nombre_pdf}")

        nombre_pdf = cuadro_nombre_pdf.ComboBoxControl(searchDepth=1, Name="Nombre:")
        logger.debug(f"dentro de {nombre_pdf}")

        rellenar_nombre = nombre_pdf.EditControl(searchDepth=1, Name="Nombre:")

        rellenar_nombre.GetValuePattern().SetValue(file_name)
        logger.debug(f"se escribio dentro de {rellenar_nombre}")

        guardar = ventana_guardar.ButtonControl(searchDepth=1, Name="Guardar")
        assert guardar.GetInvokePattern().Invoke()

        logger.debug(f"se dio clic a {guardar}")
