import streamlit as st
import json
import urllib.parse

st.set_page_config(page_title="Groww AI Insights", layout="wide")

st.title("🚀 Groww: Review Intelligence & Support Workflow")
st.write("This dashboard transforms raw customer feedback into internal product updates and support documentation.")

# Load the generated JSON payload
try:
    with open('final_mcp_payload.json', 'r', encoding='utf-8') as f:
        payload = json.load(f)
except Exception as e:
    st.error(f"Error loading final_mcp_payload.json: {e}")
    st.stop()

# Layout outputs
col1, col2 = st.columns(2)

with col1:
    st.header("1️⃣ Weekly Product Pulse")
    st.info("Internal summary for the Product Team.")
    st.markdown(payload['weekly_pulse'])

with col2:
    st.header("2️⃣ Customer Fee Explainer")
    st.info("Standardized snippet for the Support Team.")
    st.markdown(payload['explanation_bullets'])

st.divider()

# MCP Approval Gate
st.header("🛡️ MCP Approval Gate")
st.write("Click below to approve these generated insights and log them to internal tools.")

if st.button("✅ Approve & Execute Actions", type="primary"):
    # Append to local markdown file
    with open("Internal_Product_Notes.md", "a", encoding="utf-8") as doc:
        doc.write(f"\n\n---\n## Workspace Entry: {payload['date']}\n")
        doc.write(payload['weekly_pulse'] + "\n")
        doc.write("\n### Approved Support Explainer:\n")
        doc.write(payload['explanation_bullets'] + "\n")

    # Mailto link
    subject = f"Weekly Product Pulse + Customer Clarification — {payload['date']}"
    body = f"Hello Team,\n\n{payload['weekly_pulse']}\n\n---\n\n{payload['explanation_bullets']}"
    mailto_link = f"mailto:support-team@groww.in?subject={urllib.parse.quote(subject)}&body={urllib.parse.quote(body)}"

    st.success("✔️ **MCP Action 1 Complete:** Appended to `Internal_Product_Notes.md`.")
    st.success("✔️ **MCP Action 2 Complete:** Email draft generated.")
    st.markdown(f"### 📧 [**Click here to open the Email Draft**]({mailto_link})")
    st.balloons()