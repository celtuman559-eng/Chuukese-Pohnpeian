# Chuukese-Pohnpeian Parallel Corpus & Data Pipeline

## 📌 Project Overview
This repository contains a structured, machine-readable conversational parallel corpus comparing **Chuukese** and **Pohnpeian**, two low-resource Austronesian languages native to Micronesia.

In modern Natural Language Processing (NLP) and AI translation systems, these dialects suffer from acute data scarcity. This project establishes a relational data architecture designed to aid text-normalization, intent classification, and translation model validation workflows.

## 🛠️ Data Architecture (`database.json`)
The phrases are modeled relationally using structured metadata hooks to maximize utility for data science pipelines:
- `concept_id`: Unique primary key mapping the universal semantic concept.
- `semantic_category`: Groups data by thematic conversational domains.
- `dialogue_type`: Classifies token strings as statements, questions, or answers to map conversational flows.
- `linguistic_overlap`: Documents phonetic and root cognate historical developments.

## 🚀 Technical Features
- **Data Engineering Hygiene:** Structured JSON schema format designed for seamless injection into training arrays, vector spaces, or Pandas DataFrames.
- **Automated Validation:** Includes a Python preprocessing utility (`pipeline.py`) to parse, sort, and inspect dialogue tokens programmatically.

## 📈 Running the Pipeline
To run the automated analysis pipeline, execute the following script in your local environment:
```bash
python pipeline.py
```
