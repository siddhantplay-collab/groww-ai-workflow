# Groww AI Workflow - Milestone 5

## Project Overview
An AI-powered workflow that turns raw customer reviews into actionable product insights and ready-to-use support communication for the Groww app.

## Identified Fee Issue
Based on the analysis of recent 1-3 star reviews, the system identified recurring user confusion regarding **Depository Participant (DP) Charges**. Users who expect "zero brokerage" are confused when ₹15.93 (₹13.5 + GST) is automatically deducted upon selling stocks, perceiving it as a hidden fee.

## Where MCP Approval Happens
The Model Context Protocol (MCP) approval step occurs directly in the Streamlit user interface. After the LLM generates the "Weekly Product Pulse" and the "Customer Fee Explainer", a human-in-the-loop (Product/Support Manager) must review the text and explicitly click the **"Approve and Execute Actions"** button.

Once approved, the system executes two simulated MCP actions:
1. Appends the approved documentation to an internal workspace (`Internal_Product_Notes.md`).
2. Generates an email draft via a parameterized `mailto:` link for the support team.

## How to Run Locally
1. Install requirements:
   `pip install streamlit pandas openai`
2. Run the application:
   `python -m streamlit run app.py`

## Source List
1. https://groww.in/pricing
2. https://groww.in/help/
3. https://play.google.com/store/apps/details?id=com.nextbillion.groww
4. https://www.cdslindia.com/
