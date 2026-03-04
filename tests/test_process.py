from pathlib import Path

from pydantic import SecretStr

from aconsys.views.login.window import LoginWindow


def test_go_to_compras_view(
    executable_file: Path,
    username: str,
    password: SecretStr,
    compras_data: dict[str, str],
) -> None:
    login_window = LoginWindow(executable_file)
    main_window = login_window.login(username, password)
    main_window.change_work_period("12")

    ruc: str = compras_data["ruc"]
    serie: str = compras_data["serie"]
    comprobante: str = compras_data["comprobante"]
    account_number: str = compras_data["account_number"]

    success = main_window.register_purchase_one_by_one(
        receipt_number="01",
        supplier_number=ruc,
        currency_type="01",
        receipt_type="01",
        issue_date="01/11/2025",
        concept="ALQUILER DISPENSADOR NEO",
        serie=serie,
        receipt_number_from_invoice=comprobante,
        account_number=account_number,
        sale_value="106.0",
        has_detraction=True,
        type_detraction="003",
        payment_date="3/01/2024",
        constancia_number="12345678",
        aconsys_date="01/12/2025",
    )

    print(success)

    print(success)
