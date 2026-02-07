from aconsys.views.login.window import LoginWindow


def test_go_to_compras_view(executable_file, username, password) -> None:
    login_window = LoginWindow(executable_file)
    main_window = login_window.login(username, password)
    main_window.change_work_period("12")
    success = main_window.register_purchase_one_by_one(
        receipt_number="01",
        supplier_number="20193681655",
        currency_type="01",
        receipt_type="01",
        issue_date="01/11/2025",
        concept="ALQUILER DISPENSADOR NEO",
        serie="F009",
        receipt_number_from_invoice="79021",
        account_number="4211103",
        sale_value="106.0",
        has_detraction=True,
        type_detraction="003",
        payment_date="3/01/2024",
        constancia_number="12345678",
        aconsys_date="01/12/2025",
    )

    print(success)
