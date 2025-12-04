import os
from pathlib import Path

from mojelektro import Config, DEFAULT_BASE_URL, MojElektroClient


def load_dotenv(path: str = ".env") -> None:
    env_path = Path(path)
    if not env_path.exists():
        return
    for line in env_path.read_text().splitlines():
        stripped = line.strip()
        if not stripped or stripped.startswith("#") or "=" not in stripped:
            continue
        key, value = stripped.split("=", 1)
        if key and key not in os.environ:
            os.environ[key] = value


def main() -> None:
    load_dotenv()
    api_token = os.getenv("X_API_TOKEN")
    base_url = os.getenv("BASE_URL", DEFAULT_BASE_URL)
    identifikator = os.getenv("EIMM") or os.getenv("GSRN_MM")

    if not api_token or not identifikator:
        print("Set X_API_TOKEN and EIMM (or GSRN_MM) in .env.")
        return

    client = MojElektroClient(Config(api_token=api_token, base_url=base_url))
    mesto = client.get_merilno_mesto(identifikator)
    print(f"Naziv: {mesto.get('naziv')}")
    print(f"Naslov: {mesto.get('naslov')}")
    print(f"Merilne točke: {len(mesto.get('merilneTocke', []))}")


if __name__ == "__main__":
    main()
