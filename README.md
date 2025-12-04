# Moj Elektro Python Client

Typed Python client for the Moj Elektro REST API. Provides sync and async helpers for meter readings, metering point details, reading qualities, and reading types.

API docs: https://docs.informatika.si/mojelektro/api/

## Quickstart

```bash
git clone git@github.com:psvent/Moj-Elektro-API-Client.git
cd Moj-Elektro-API-Client
python3 -m venv .venv
source .venv/bin/activate
cp .env.example .env  # fill in X_API_TOKEN and IDs
pip install -e .[dev]
python examples/meter_readings.py
```

## Installation

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -e .[dev]
```

Alternatively, install via the pinned requirements file:

```bash
pip install -r requirements.txt
```

## Configuration

Use the API token header (`X-API-TOKEN`) and optionally override the base URL. For local/manual testing, copy `.env.example` to `.env` and fill in:

- `X_API_TOKEN`: your API token
- `BASE_URL`: defaults to `https://api-test.informatika.si/mojelektro/v1`
- `EIMM`: enotni identifikator merilnega mesta
- `GSRN_MT`: GSRN merilne tocke
- `GSRN_MM`: GSRN merilnega mesta

## Usage

### Sync

```python
from mojelektro import Config, MojElektroClient

config = Config(api_token="your-token")
client = MojElektroClient(config)

readings = client.get_meter_readings(
    usage_point="123456789012345678",
    start_time="2024-01-01",
    end_time="2024-01-02",
    option=["ReadingType=32.0.2.4.1"],
)
print(readings["usagePoint"])
```

### Async

```python
import asyncio
from mojelektro import Config, MojElektroClient


async def main() -> None:
    client = MojElektroClient(Config(api_token="your-token"))
    qualities = await client.aget_reading_qualities()
    print(len(qualities))


asyncio.run(main())
```

## Testing

```bash
source .venv/bin/activate
python -m pytest
```

Tests run against mocked HTTP responses; no real API calls are made.

### Git hooks: run tests before commit/push

Enable the shared hooks once per clone to block commits (and pushes) when pytest fails (uses `python3`/`python` on your PATH, so activate your venv first):

```bash
git config core.hooksPath .githooks
```

## Examples

Run any example with your venv active:

- `python examples/meter_readings.py`
- `python examples/merilno_mesto.py`
- `python examples/merilna_tocka.py`
- `python examples/reading_qualities.py`
- `python examples/reading_types.py`

## Building a package

Build source and wheel distributions (creates `dist/`):

```bash
source .venv/bin/activate
python -m pip install build
python -m build
```
