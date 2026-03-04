"""Test fixtures."""

from os import environ
from pathlib import Path

from dotenv import load_dotenv
from pydantic import SecretStr
from pytest import fixture

load_dotenv()


@fixture(scope="session")
def executable_file() -> Path:
    """Path to the Aconsys executable file."""
    return Path(environ["ACONSYS_EXECUTABLE_FILE_PATH"])


@fixture(scope="session")
def server() -> str:
    """Address of the Aconsys server."""
    return environ["ACONSYS_SERVER"]


@fixture(scope="session")
def database() -> str:
    """Database name for the Aconsys server."""
    return environ["ACONSYS_DATABASE"]


@fixture(scope="session")
def username() -> str:
    """Username for the Aconsys server."""
    return environ["ACONSYS_USERNAME"]


@fixture(scope="session")
def password() -> SecretStr:
    """Password for the Aconsys server."""
    return SecretStr(environ["ACONSYS_PASSWORD"])


@fixture(scope="session")
def compras_data() -> dict[str, str]:
    return {
        "ruc": environ["COMPRAS_RUC_TEST"],
        "serie": environ["COMPRAS_SERIE_TEST"],
        "comprobante": environ["COMPRAS_COMPROBANTE_TEST"],
        "account_number": environ["COMPRAS_ACCOUNT_NUMBER_TEST"],
    }


@fixture(scope="session")
def alquileres_data() -> dict[str, str]:
    return {
        "ruc": environ["ALQUILERES_RUC_TEST"],
        "serie": environ["ALQUILERES_SERIE_TEST"],
        "comprobante": environ["ALQUILERES_COMPROBANTE_TEST"],
        "first_account_number": environ["FIRST_ALQUILERES_ACCOUNT_NUMBER_TEST"],
        "second_account_number": environ["SECOND_ALQUILERES_ACCOUNT_NUMBER_TEST"],
    }
