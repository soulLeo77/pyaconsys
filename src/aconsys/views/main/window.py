import uiautomation as auto

from ...base.window import TopLevelWindow

MAIN_WINDOW = auto.WindowControl(RegexName="ACONSYS")


class MainWindow(TopLevelWindow):
    _window = MAIN_WINDOW

    def _navigate_to_menu_option(self, menu_name: str, option_name: str) -> None:
        """
        Opens a menu option (e.g. 'Tablas' - 'Centro de Costos') from the main window.
        It works for classic menus of ACONSYS.
        """
        self._window.SetActive()
        self._window.SetTopmost(True)

        menu_bar = self._window.MenuBarControl(searchDepth=1, AutomationId="MenuBar")

        menu_item = menu_bar.MenuItemControl(searchDepth=1, Name=menu_name)
        assert menu_item.GetInvokePattern().Invoke()

        tablas_menu = self._window.MenuControl(searchDepth=1, Name=menu_name)

        option_item = tablas_menu.MenuItemControl(searchDepth=1, Name=option_name)
        assert option_item.GetInvokePattern().Invoke()

    def download_centro_costos_file(self, file_name: str) -> None:
        ventana = self._window.WindowControl(Name="Mantenimiento de Centro de Costos")

        panel = ventana.PaneControl(searchDepth=1, ClassName="ImFrame3DWndClass")

        imprimir = panel.ButtonControl(searchDepth=1, Name="Imprimir")
        assert imprimir.GetInvokePattern().Invoke()

        ventana_imprimir = auto.WindowControl(searchDepth=1, Name="Imprimir")

        panel_imprimir = ventana_imprimir.PaneControl(ClassName="SHELLDLL_DefView")

        pdf_seleccionar = panel_imprimir.ListControl(Name="Vista de carpetas")

        clic_pdf = pdf_seleccionar.ListItemControl(
            searchDepth=1, Name="Microsoft Print to PDF"
        )
        assert clic_pdf.GetSelectionItemPattern()

        clic_pdf_imprimir = ventana_imprimir.ButtonControl(
            searchDepth=1, Name="Imprimir"
        )
        assert clic_pdf_imprimir.GetInvokePattern().Invoke()

        ventana_principal = self._window.PaneControl(
            searchDepth=1, Name="Área de trabajo"
        )

        ventana = ventana_principal.WindowControl(
            searchDepth=1, ClassName="ThunderRT6FormDC"
        )

        ventana_panel = ventana.PaneControl(searchDepth=1, Name="")

        barra_principal = ventana_panel.TextControl(searchDepth=1, Name="")

        barra_oficial = barra_principal.PaneControl(searchDepth=1, Name="")
        # TIENE VARIOS00000 HERMANOS
        barra_herramientas = barra_oficial.ToolBarControl(
            searchDepth=1, AutomationId="203"
        )  # ID PODRIA CAMBIAR

        icono_exportar = barra_herramientas.ButtonControl(
            searchDepth=1, Name="Exportar informe"
        )
        assert icono_exportar.GetInvokePattern().Invoke()

        ventana_export = self._window.WindowControl(searchDepth=1, Name="Export")

        ok_export = ventana_export.ButtonControl(searchDepth=1, Name="OK")
        assert ok_export.GetInvokePattern().Invoke()

        ok_export2 = self._window.WindowControl(searchDepth=1, Name="Export Options")

        clic_export2 = ok_export2.ButtonControl(searchDepth=1, Name="OK")
        assert clic_export2.GetInvokePattern().Invoke()

        ventana_guardar = self._window.WindowControl(
            searchDepth=1, Name="Choose export file"
        )

        cuadro_nombre_pdf = ventana_guardar.PaneControl(
            searchDepth=1, Name="RptTablasComunConta"
        )

        nombre_pdf = cuadro_nombre_pdf.ComboBoxControl(searchDepth=1, Name="Nombre:")

        rellenar_nombre = nombre_pdf.EditControl(searchDepth=1, Name="Nombre:")

        rellenar_nombre.GetValuePattern().SetValue(file_name)

        guardar = ventana_guardar.ButtonControl(searchDepth=1, Name="Guardar")
        assert guardar.GetInvokePattern().Invoke()
