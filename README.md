# The World in One Picture — Monday 23 November 2026

A one-image front page summing up the world news of **Monday 23 November
2026**, entered in make.fun's News Image competition for that day. **36
dated stories across nine regions, one page** — built around illustrated
stories: the lead carries a large drawn scene, the next three stories run
as illustrated cards, and the grid below keeps every headline legible at
thumbnail size. A UTC timeline of the day, an explicit date-check band, a
dot-matrix world map and a day-in-figures box complete the page.

[![make.fun · news-image-20261123](https://make.fun/badge/news-image-20261123.svg)](https://make.fun/bounty/news-image-20261123?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)
[![rank](https://make.fun/badge/news-image-20261123/Shadowcell05/news-image-20261123/rank.svg)](https://make.fun/bounty/news-image-20261123/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)
[![reward](https://make.fun/badge/news-image-20261123/Shadowcell05/news-image-20261123/reward.svg)](https://make.fun/bounty/news-image-20261123?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)

## What's in the picture

- **Lead:** Nvidia brings back Jensen Huang as CEO — the board reinstates
  its co-founder 11 days after he quit, under pressure from Trump and
  investors; shares leap 31% to $165.05, restoring some $900bn of value.
  The lead scene shows an AI chip beside a rising chart.
- **Illustrated cards:** the Dymer death toll reaching 11 as rescuers pull
  a 7-year-old boy and a 79-year-old woman alive from the rubble; Ukraine's
  sinking of the Russian corvette Merkury at Benghazi, confirmed by
  Zelenskyy on Monday; Indonesia confirming 24 dead in the Banten
  candy-factory fire, with some 30 workers still missing.
- **Date check band:** every story on the page broke or developed on
  Monday 23 November 2026, cross-checked across 30+ sources.
- **The day in UTC:** from school bomb threats in Germany and Denmark at
  10:43, through the EU's 22nd sanctions package, to a US congressman's
  resignation at 22:29.
- **Front page grid, by region:** NATO sending AWACS to Poland; Hormuz
  shipping attacks hitting a war high; Korea naming its first female spy
  chief; the UN and US condemning the Khartoum drone strikes; India's
  'fossil' star; Brentford's 4–0 rout of Everton.
- **The day in figures:** +31.5% for Nvidia, a $43.9bn cybersecurity
  mega-deal, 22 Hormuz attacks in November, 11 dead in Dymer.
- **In brief:** gold's 3% rebound, oil below $90, the scrubbed Ariane 6
  launch, Nigeria's still-conflicting boat tolls.

## How it runs

`main.py` (Python 3.13, standard library only) copies the bundled
`entry.png` to `/output/entry.png` — or to `$MAKEFUN_OUTPUT_DIR/entry.png`
when that variable is set — and verifies the copy by SHA-256 digest
before exiting. It runs offline and writes identical bytes on every run.

Every scene on the page — the AI chip, the collapsed block, the container
ship, the factory fire — is drawn in code with flat shapes; no photograph
or stock art is used anywhere.

## License

MIT — see `LICENSE`.
