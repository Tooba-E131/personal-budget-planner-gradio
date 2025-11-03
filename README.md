# Personal Budget Planner – Gradio Application

**Author:** Tooba Edhi  
**Course:** OIM 7502 – Spring 2025  
**Library Demonstrated:** Gradio  
**Project Type:** Midterm Individual Project

---

## Overview

This project demonstrates how the **Gradio** Python library can be used to convert a Python function into an **interactive, web-based budgeting tool** without requiring any front-end development.

The application allows users to:

- Enter monthly income and expenses across key categories
- Automatically calculate **total expenses**
- Determine **remaining savings**
- Classify spending as **Overspending**, **Break-even**, or **Healthy Savings**
- View a **pie chart visualization** of spending distribution
- **Download a personalized PDF summary report**

This app highlights how data science logic can be made **accessible and interpretable** to non-technical users.

---

## Live Demo (Permanent Hosting)

Run the app instantly:

 **https://huggingface.co/spaces/Toobaaaa/personal-budget-planner**

---


## Why Gradio?

In many data science workflows, models or analysis tools remain within Jupyter notebooks, where only technical users can interact with them.  

**Gradio bridges this gap** by enabling:

- Quick prototyping and interactive experimentation
- Simple web-based sharing of analytical tools
- Stakeholder collaboration without requiring code knowledge

This makes Gradio ideal for **communicating insights**, testing ideas, and refining tools before production-level development.

---

## Core Logic

The app takes five user inputs:

| Input | Description |
|------|-------------|
| `income` | Total monthly earnings |
| `housing` | Rent or mortgage cost |
| `food` | Monthly food/grocery expenses |
| `transport` | Travel/commute expenses |
| `other` | Miscellaneous variable spending |

It outputs:

| Output | Description |
|--------|-------------|
| `total_expenses` | Sum of all expenses |
| `savings` | Difference between income and expenses |
| `status_message` | Interpretation of spending behavior |
| `pie_chart` | Visual breakdown of category spending |
| `pdf_file` | Downloadable summary report (generated automatically) |

---

## User Interface

The UI is built using Gradio’s `gr.Blocks()` layout system and includes:

- Slider controls for each spending category
- A text summary window displaying the budget status
- A chart showing spending allocation
- A file download button for the final report

No HTML, CSS, or JavaScript is required.

---

## Presentation Slides
You can view or download the presentation slides used for this project here:

**[Download the Presentation (PPTX)](https://github.com/Tooba-E131/personal-budget-planner-gradio/blob/main/Gradio_Tooba%20Edhi.pptx)**

---

## Running the App Locally

1. Clone the repository:

```bash
git clone https://github.com/Tooba-E131/personal-budget-planner-gradio.git
cd personal-budget-planner-gradio
pip install -r requirements.txt
python budget_app.py

---
## Project Resources

**Live Web App:**  
https://huggingface.co/spaces/Toobaaaa/personal-budget-planner

**Presentation Slides (PPTX):**  
https://github.com/Tooba-E131/personal-budget-planner-gradio/blob/main/Gradio_Tooba%20Edhi.pptx

**Source Code Repository:**  
https://github.com/Tooba-E131/personal-budget-planner-gradio
