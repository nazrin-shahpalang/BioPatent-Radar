# 🧬 BioPatent Radar

**AI-powered patent landscape analysis for bio-based & sustainable materials**

[![Live Dashboard](https://img.shields.io/badge/🔴_Live-Dashboard-FF4B4B?style=for-the-badge)](https://biopatent-radar.streamlit.app/)
![Python](https://img.shields.io/badge/Python-3.11-blue?style=flat-square)
![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-FF4B4B?style=flat-square)
![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)

## 🔗 [Explore the Live Dashboard →](https://biopatent-radar.streamlit.app/)

---

## Overview

**BioPatent Radar** turns a raw patent database search into an interactive technology landscape. Instead of reading through hundreds of individual patents one by one, this tool automatically groups them by underlying technical similarity — revealing which sub-technologies are emerging, which are saturated, and where the white space is.

The current case study focuses on **bio-based adhesives**, a fast-growing niche within sustainable materials, but the underlying pipeline is domain-agnostic and can be pointed at any technology area.

## ✨ Features

- **Automated data collection** — retrieves patent records programmatically via the [Lens.org](https://www.lens.org/) Patent Search API (title, abstract, classification, jurisdiction, publication date)
- **Semantic embeddings** — converts each patent's text into a 384-dimensional vector using `sentence-transformers`, capturing meaning rather than just keywords
- **Unsupervised clustering** — K-Means groups patents into interpretable technology sub-clusters, with optimal cluster count selected via the elbow method
- **Interactive landscape map** — a 2D (PCA-projected) visualization where each point is a patent, colored by cluster, with hover-to-preview details
- **Filterable patent explorer** — search and filter the full dataset by technology cluster, jurisdiction, and date

## 🧪 How It Works 
Lens.org API → Text Embeddings → K-Means Clustering → Interactive Dashboard
(retrieve) (understand) (group) (explore)

## 📊 Current Dataset

- **155 patents** on bio-based adhesives (2011–2026)
- Global coverage: EP, US, CN, WO, KR, and more
- **9 distinct technology clusters** identified, including lignin-based systems, plant-oil/soybean-based adhesives, wood composite & plywood applications, algae-based adhesives, and more

## 🛠️ Tech Stack

`Python` · `Lens.org API` · `sentence-transformers` · `scikit-learn` · `pandas` · `Plotly` · `Streamlit`

## 🧬 Part of a Larger Project Series

BioPatent Radar is the fourth project in an evolving AI-powered scientific & technology intelligence platform, building directly on **[PatentLens](https://github.com/nazrin-shahpalang/PatentLens-LLM-Patent-Intelligence)** — an LLM patent-report benchmarking tool. Together, these projects trace a path from single-patent LLM analysis toward full-scale, multi-patent technology intelligence.

## 🚀 Run Locally

```bash
git clone https://github.com/nazrin-shahpalang/BioPatent-Radar.git
cd BioPatent-Radar
pip install -r requirements.txt
streamlit run src/dashboard.py
```

## 👤 Author

**Nazrin Shahpalangova**
MSc Biological Resources, Hochschule Rhein-Waal (HSRW)
[GitHub](https://github.com/nazrin-shahpalang)
