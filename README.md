# 🛠️ High-Level to Low-Level Architecture Pipeline

## 📌 Project Description

This project is a prototype of an **AI-assisted automation tool** that simplifies the transformation of **high-level business requirements** into **low-level technical specifications**. The tool helps developers and product teams structure ideas into:

- Functional modules
- Database schemas
- Pseudocode logic

It provides a structured starting point for system architecture and software design.

---

## 🎯 Objective

- To automate the process of converting high-level English requirements into:
  - Module breakdowns
  - JSON-formatted database schemas
  - Python-style pseudocode

---

## 🏗️ Folder Structure

High-Level-to-Low-Level-Architecture-Pipeline/
│
├── main.py # Entry point: accepts input and runs the pipeline
├── requirement_parser.py # Logic to extract modules, schema, and pseudocode
├── utils.py # File-saving utility functions
├── output_modules.txt # Auto-generated: List of functional modules
├── output_schema.json # Auto-generated: Basic database schema
├── output_pseudocode.py # Auto-generated: Generated pseudocode
└── README.md # Project documentation

---
**Code Output** :
<img width="1765" height="718" alt="Screenshot 2025-07-19 065150" src="https://github.com/user-attachments/assets/8a1149d9-b472-4829-9b3a-4a19adcef53f" />

---
## ⚙️ How It Works

1. **User Input**  
   The tool prompts the user to enter a high-level requirement in plain English.

2. **Processing Logic**  
   The logic in `requirement_parser.py` simulates a breakdown of the requirement into:
   - Subsystems or modules
   - Database table-like schemas
   - Key function pseudocode

3. **Output Files**  
   Using `utils.py`, all generated outputs are saved as separate files:
   - `output_modules.txt` — list of functional modules.
   - `output_schema.json` — dictionary of entity structures.
   - `output_pseudocode.py` — basic logic for core functionalities.

---

## 🧪 Example

**Input Prompt:** : Build a task management system where users can create, assign, and track tasks.

---
**Generated Outputs:**

- `output_modules.txt`
- `output_schema.json`
- output_pseudocode.py

---
✅ Features
CLI-based user interaction

Static logic (can be upgraded to AI/LLM models)

Generates separate files for modularity

Clean and extendable architecture

---
🧠 Future Enhancements
Integrate with LLMs (e.g., OpenAI, Hugging Face)

Convert output to PDF or Markdown documentation

Web UI using Flask or Streamlit

Add testing and error handling

---

👨‍💻 Author
Sahil Tuli
BCA Student | Aspiring Data Scientist
LinkedIn • Portfolio

---
📄 License
This project is licensed under the MIT License.

---
