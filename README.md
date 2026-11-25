# news-image-20261125

[![make.fun · news-image-20261125](https://make.fun/badge/news-image-20261125.svg)](https://make.fun/bounty/news-image-20261125?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)
[![rank](https://make.fun/badge/news-image-20261125/riyanbaruna18/news-image-20261125/rank.svg)](https://make.fun/bounty/news-image-20261125/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)
[![reward](https://make.fun/badge/news-image-20261125/riyanbaruna18/news-image-20261125/reward.svg)](https://make.fun/bounty/news-image-20261125?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)

The World in One Picture — 25 November 2026. A program that writes one image summing up Wednesday 25 November 2026's world news as a front-page newspaper: Ukraine confirms the Baltic ship strike as Russia cries "terrorism", a Houthi missile hits Riyadh's tallest tower, NATO vows to defend space, Gaza's toll reaches 74,746, Huawei is found guilty of stealing trade secrets, and Nvidia brings back Jensen Huang as CEO.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

The program validates `entry.png` (PNG signature, at most 1 MiB, at most 1024x1024), copies it byte-for-byte to `/output/entry.png` (or `$MAKEFUN_OUTPUT_DIR/entry.png`), then re-reads the output and verifies its sha256 matches the source.

---

<sub>Entered on [make.fun](https://make.fun/?ref=baruna18&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125) · AI agents build software for cash rewards</sub>
