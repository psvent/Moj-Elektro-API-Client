import os
from datetime import datetime
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
    usage_point = (
        os.getenv("USAGE_POINT")
        or os.getenv("GSRN_MM")
        or os.getenv("EIMM")
        or os.getenv("GSRN_MT")
    )
    current_year = datetime.now().year
    start_time = os.getenv("START_TIME", f"{current_year}-12-01")
    end_time = os.getenv("END_TIME", f"{current_year}-12-04")
    option = os.getenv(
        "OPTION", "ReadingType=32.0.2.4.1.2.12.0.0.0.0.0.0.0.0.3.72.0"
    )

    if not api_token or not usage_point:
        print("Set X_API_TOKEN and a usage point (USAGE_POINT/GSRN_MM/EIMM/GSRN_MT) in .env.")
        return

    client = MojElektroClient(Config(api_token=api_token, base_url=base_url))
    readings = client.get_meter_readings(
        usage_point=usage_point,
        start_time=start_time,
        end_time=end_time,
        option=[option] if option else None,
    )
    blocks = readings.get("intervalBlocks", [])
    total_readings = sum(len(b.get("intervalReadings", [])) for b in blocks)
    print(f"Fetched {len(blocks)} interval blocks / {total_readings} readings")
    if blocks and blocks[0].get("intervalReadings"):
        first = blocks[0]["intervalReadings"][0]
        print(f"First reading: {first.get('timestamp')} -> {first.get('value')}")


if __name__ == "__main__":
    main()
