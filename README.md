# UAP Reporting — Methodology Lab

**Explore online:** [Open the interactive browser companion](https://luckygithub777.github.io/uap-reporting-methodology-lab/). The hosted companion explains the ideas; the Python CLI and tests remain separate source tools.

An educational teaching kit with an interactive online companion for analyzing **report records**, rather than claiming to verify physical events. It provides synthetic-record generation, elementary statistics, and guides to date interpretation, sampling limits and responsible conclusions.

## Try it

Python 3.10+; no external dataset or account required.

```bash
python -c "from sightings_analysis.synthetic_data import generate_rows; print(len(generate_rows(rows=20, seed=9)))"
python -m unittest discover -s tests -v
```

All generated reports are **fictional**. Trends in fabricated data cannot establish actual events, causes, geographic risks, or population prevalence. The code uses no telemetry or data uploads.

**License and attribution:** The included MIT [LICENSE](LICENSE) preserves the original contributors' copyright notice. [MANIFEST.sha256](MANIFEST.sha256) records the exact released source files.
