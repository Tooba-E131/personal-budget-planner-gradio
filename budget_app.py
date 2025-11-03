#!/usr/bin/env python
# coding: utf-8

# In[ ]:


"""
Name:       Tooba Edhi
Library:    Gradio
URL:        https://www.gradio.app/
Description:
This demo shows how to build an interactive budgeting tool with Gradio.
Users enter their monthly income and expenses and the app returns a savings summary,
a pie chart visualization, and a downloadable PDF report.
"""


# In[ ]:


import tempfile
import gradio as gr
import matplotlib.pyplot as plt
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet


# In[15]:


def budget_summary(income, housing, food, transport, other):
    """Compute budget summary, create PDF report, and return chart + file."""
    income, housing, food, transport, other = map(
        float, [income, housing, food, transport, other]
    )
    total_expenses = housing + food + transport + other
    savings = income - total_expenses

    # Summary text
    summary = (
        f"**Monthly Income:** ${income:,.2f}\n"
        f"**Total Expenses:** ${total_expenses:,.2f}\n"
        f"**Remaining (Savings):** ${savings:,.2f}\n\n"
    )

    if savings < 0:
        summary += "*You are spending more than you earn.* Consider reducing expenses.\n"
    elif savings < income * 0.1:
        summary += "You are saving a little — try to increase savings.\n"
    else:
        summary += "Great! You are saving a healthy amount.\n"

    # Recommendation logic
    recommended_savings = income * 0.20
    needed = recommended_savings - savings

    if savings < recommended_savings:
        summary += (
            f"\n**Goal Recommendation:** Try to save ~20% (${recommended_savings:,.2f}).\n"
            f"To meet this goal, reduce expenses by about **${needed:,.2f}**."
        )
    else:
        summary += "\nYou are meeting the recommended 20% savings threshold."

    # Creating PDF
    tmp_pdf = tempfile.NamedTemporaryFile(delete=False, suffix=".pdf")
    doc = SimpleDocTemplate(tmp_pdf.name, pagesize=letter)
    styles = getSampleStyleSheet()
    story = [
        Paragraph("Personal Budget Report", styles["Title"]),
        Spacer(1, 12),
    ]
    for line in summary.split("\n"):
        if line.strip():
            story.append(Paragraph(line, styles["BodyText"]))
            story.append(Spacer(1, 6))
    doc.build(story)

    # Creating Pie Chart
    labels = ["Housing", "Food", "Transportation", "Other Expenses", "Savings"]
    sizes = [housing, food, transport, other, max(savings, 0)]

    fig, ax = plt.subplots()
    ax.pie(sizes, labels=labels, autopct="%1.1f%%", startangle=90)
    ax.set_title("Monthly Budget Breakdown")
    plt.tight_layout()

    return summary, fig, tmp_pdf.name


# Gradio Interface (UI)
with gr.Blocks(theme=gr.themes.Soft(primary_hue="indigo", neutral_hue="gray")) as demo:

    gr.Markdown(
        "<h1 style='text-align: center; margin-bottom: -10px;'> Personal Budget Planner</h1>"
    )
    gr.Markdown(
        "<p style='text-align: center; color: #cfcfcf;'>Visualize your monthly spending, understand your savings, and download a personalized financial summary.</p>"
    )

    with gr.Row():
        with gr.Column(scale=1):
            with gr.Group():
                income = gr.Slider(1000, 10000, value=3000, label="Monthly Income ($)")
                housing = gr.Slider(0, 6000, value=1200, label="Housing / Rent ($)")
                food = gr.Slider(0, 2000, value=400, label="Food ($)")
                transport = gr.Slider(0, 1000, value=200, label="Transportation ($)")
                other = gr.Slider(0, 2000, value=300, label="Other Expenses ($)")
            
            btn = gr.Button("Calculate Budget", variant="primary")

        with gr.Column(scale=1):
            result_text = gr.Markdown()
            chart_output = gr.Plot()
            download_pdf = gr.File(label="Download Budget Report (PDF)")

    btn.click(
        budget_summary,
        inputs=[income, housing, food, transport, other],
        outputs=[result_text, chart_output, download_pdf]
    )

demo.launch(share=True)


# In[26]:


get_ipython().system('jupyter nbconvert --to script "Budget Calculator Advanced.ipynb" --output app.py')

