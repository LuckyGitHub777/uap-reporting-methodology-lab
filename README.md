# UAP Reporting — Methodology Lab

An offline educational kit for critically examining **report records**, not proof of any underlying physical phenomenon. It includes a deterministic generator for fictional UAP report records, reusable elementary statistics, and guidance on date semantics, sample limitations, and responsible interpretation.

Try it with Python 3.10+:

```bash
python -c "from sightings_analysis.synthetic_data import generate_rows; print(len(generate_rows(rows=20, seed=9)))"
python -m unittest discover -s tests -v
```

All generated records are **synthetic**, not witness testimony, research observations, or independently verified events. A pattern in fabricated reports does not establish a physical event, mechanism, causation, geographic risk or real-world prevalence. No external dataset, account, tracker or upload is used.

**License/attribution:** The included original MIT `LICENSE` credits UFO/UAP Sightings Analysis contributors. This is an isolated history-free learning subset, not a publication of the original private repository or personal research. See `MANIFEST.sha256` for the exact source package.
