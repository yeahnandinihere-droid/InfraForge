import shutil
import subprocess
from pathlib import Path
import streamlit as st
from infraforge.core.terraform_engine import (
    find_terraform,
    run_terraform,
    validate_terraform
)
st.set_page_config(
    page_title="InfraForge",
    page_icon="⚒️",
    layout="wide"
)

st.title("⚒️ InfraForge")
st.subheader("Infrastructure. Forged entirely through code.")

st.markdown(
    "A code-first platform for provisioning, configuring, "
    "and managing cloud infrastructure."
)

st.divider()

st.header("Environment Overview")

terraform_path = find_terraform()

col1, col2 = st.columns(2)

with col1:
    st.metric("InfraForge Version", "0.1.0")

with col2:
    if terraform_path:
        st.success("Terraform detected")
    else:
        st.warning("Terraform not found")

if terraform_path:
    st.caption(f"Terraform location: {terraform_path}")

st.divider()

st.divider()

st.header("Configuration Validator")

project_dir = st.text_input(
    "Terraform Project Directory",
    value="examples/first-project"
)
if st.button("Validate Terraform Project"):
    try:
        result = validate_terraform(project_dir)

        if result.returncode == 0:
            st.success("Terraform configuration is valid!")
            st.text(result.stdout.strip())
        else:
            st.error("Terraform validation failed.")
            st.text(result.stdout.strip() or result.stderr.strip())

    except Exception as error:
        st.error(str(error)) 