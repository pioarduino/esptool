# test/elf2image fixtures

Committed ELF inputs for `elf2image` tests.
Licensing: see [`../LICENSE`](../LICENSE).

## With accompanying in-tree source

| ELF                           | Source                                                                                 |
|-------------------------------|----------------------------------------------------------------------------------------|
| `esp32c6-appdesc.elf`         | [`esp32c6-appdesc/`](esp32c6-appdesc/) — `make`, then commit the ELF (sources CC0-1.0) |
| `esp32-too-many-sections.elf` | [`esp32-too-many-sections/`](esp32-too-many-sections/) — same                          |

`--ram-only-header` edge cases are built at test time by
[`../elf_builder.py`](../elf_builder.py) (layouts in `test_imagegen.py`);
they are not IDF images.

## Other ELFs (no in-tree rebuild)

| ELF                                                                                                   | Notes                                     |
|-------------------------------------------------------------------------------------------------------|-------------------------------------------|
| `esp32-app-template.elf`, `esp32-bootloader.elf`                                                      | ESP-IDF builds used as regression goldens |
| `esp32-zephyr.elf`                                                                                    | Zephyr                                    |
| `esp8266-nonossdkv12-example.elf`, `esp8266-nonossdkv20-at-v2.elf`, `esp8266-nonosssdk20-iotdemo.elf` | NONOS SDK era samples                     |
| `esp8266-openrtos-blink-v2.elf`                                                                       | OpenRTOS blink sample                     |

Keep these static unless intentionally updating coverage.
