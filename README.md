# Public Sentiment Analyzer

An end-to-end NLP pipeline that scrapes public feedback from government consultation portals, processes it through a large language model, and surfaces sentiment trends to support civic decision-making.

---

## Overview

Government agencies collect thousands of public submissions through online consultation platforms, but manually reviewing this volume of qualitative feedback is impractical. This project automates that analysis — scraping raw submissions, cleaning and structuring the data, and applying an LLM to classify sentiment and extract thematic patterns across responses.

**Key question answered:** What does the public actually think, and where do opinions cluster?

---

## Features

- **Automated data collection** — scrapes public consultation submissions from target portals
- **Data cleaning pipeline** — handles encoding issues, deduplication, and normalization
- **LLM-powered sentiment classification** — labels responses as positive, negative, or neutral with confidence scores
- **Thematic extraction** — identifies recurring topics and concerns across the corpus
- **Trend visualization** — charts sentiment distribution and topic frequency

---

## Tech Stack

| Layer | Tools |
|---|---|
| Scraping | JavaScript  |
| Data processing | `pandas`, `numpy` |
| LLM inference | Ollama |
| Visualization | `matplotlib`, `seaborn` |

---

## Getting Started

### Prerequisites

- Python 3.9+
- Ollama

## Results

<img width="545" height="445" alt="Screenshot 2026-06-14 134445" src="https://github.com/user-attachments/assets/92b5ca64-47c8-40b1-8160-e5865d1006f0" />

Eliminated 73 racist or bigoted comments from the submissions.


---

## Methodology

1. **Scraping** — Submissions are collected via HTTP requests with rate-limiting to respect server load. HTML is parsed with BeautifulSoup to extract the text body of each response.

2. **Preprocessing** — Text is lowercased, stripped of HTML artifacts, and deduplicated. Short or uninformative responses (< 10 tokens) are filtered out.

3. **LLM Classification** — Each submission is passed to the LLM with a structured prompt asking for a sentiment label and a one-sentence rationale. Responses are parsed and stored alongside the original text.

4. **Aggregation** — Results are grouped and visualized to show distribution of sentiment and frequency of recurring themes.

---

## Limitations & Future Work

- Scraping logic is portal-specific and may require updates if site structure changes
- LLM classification reflects the model's priors and may misclassify nuanced or sarcastic text
- Future: fine-tune a smaller model on labeled civic feedback for lower-cost inference
- Future: add support for multilingual submissions (English/French for Canadian portals)

---

## Author

**Motasim** — BSc Physics & Computer Science, McGill University  
[GitHub](https://github.com/Motasim0109)
