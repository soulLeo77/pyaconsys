from uiautomation import WindowControl

from ...base.window import TopLevelWindow
from .controls import MAIN_WINDOW


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

        menu_tables = self._window.MenuControl(searchDepth=1, Name=menu_name)

        option_item = menu_tables.MenuItemControl(searchDepth=1, Name=option_name)
        assert option_item.GetInvokePattern().Invoke()

    def download_centro_costos_file(self, file_name: str) -> None:
        window = self._window.WindowControl(
            Name="Mantenimiento de Centro de Costos", searchDepth=1
        )

        panel = window.PaneControl(searchDepth=1, ClassName="ImFrame3DWndClass")

        print_button = panel.ButtonControl(searchDepth=1, Name="Imprimir")
        assert print_button.GetInvokePattern().Invoke()

        print_window = WindowControl(searchDepth=1, Name="Imprimir")

        print_panel = print_window.PaneControl(
            ClassName="SHELLDLL_DefView", searchDepth=1
        )

        select_box_pdf = print_panel.ListControl(
            Name="Vista de carpetas", searchDepth=1
        )

        item_pdf_click = select_box_pdf.ListItemControl(
            searchDepth=1, Name="Microsoft Print to PDF"
        )
        assert item_pdf_click.GetSelectionItemPattern()

        inner_print_button = print_window.ButtonControl(searchDepth=1, Name="Imprimir")
        assert inner_print_button.GetInvokePattern().Invoke()

        main_window = self._window.PaneControl(searchDepth=1, Name="Área de trabajo")

        window = main_window.WindowControl(searchDepth=1, ClassName="ThunderRT6FormDC")

        panel_window = window.PaneControl(searchDepth=1, Name="")

        main_bar = panel_window.TextControl(searchDepth=1, Name="")

        oficial_bar = main_bar.PaneControl(searchDepth=1, Name="")
        # Has many siblings
        toolbar = oficial_bar.ToolBarControl(
            searchDepth=1, AutomationId="203"
        )  # ID could change

        export_icon = toolbar.ButtonControl(searchDepth=1, Name="Exportar informe")
        assert export_icon.GetInvokePattern().Invoke()

        export_window = self._window.WindowControl(searchDepth=1, Name="Export")

        ok_export_button = export_window.ButtonControl(searchDepth=1, Name="OK")
        assert ok_export_button.GetInvokePattern().Invoke()

        export_options = self._window.WindowControl(
            searchDepth=1, Name="Export Options"
        )

        second_ok_export_button = export_options.ButtonControl(searchDepth=1, Name="OK")
        assert second_ok_export_button.GetInvokePattern().Invoke()

        save_window = self._window.WindowControl(
            searchDepth=1, Name="Choose export file"
        )

        pdf_name_chart = save_window.PaneControl(
            searchDepth=1, Name="RptTablasComunConta"
        )

        select_pdf_name = pdf_name_chart.ComboBoxControl(searchDepth=1, Name="Nombre:")

        input_pdf_name = select_pdf_name.EditControl(searchDepth=1, Name="Nombre:")

        input_pdf_name.GetValuePattern().SetValue(file_name)

        save_button = save_window.ButtonControl(searchDepth=1, Name="Guardar")
        assert save_button.GetInvokePattern().Invoke()
