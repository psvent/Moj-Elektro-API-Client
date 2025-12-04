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

    if not api_token:
        print("Set X_API_TOKEN in .env.")
        return

    client = MojElektroClient(Config(api_token=api_token, base_url=base_url))
    reading_types = client.get_reading_types()
    print(f"Reading types: {len(reading_types)} entries")
    if reading_types:
        first = reading_types[0]
        print(f"First: {first.get('naziv')} ({first.get('readingType')})")


if __name__ == "__main__":
    main()
