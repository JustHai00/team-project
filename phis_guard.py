# ==============================================
# PHISHGUARD — Part 1: Collect Information
# ==============================================

# We need these tools built into Python
import json
import os
import re
from typing import Dict

# This is where we will save reports later
DATA_FILE = "phishguard_reports.json"

# ──────────────────────────────────────────────
# Function: Collect Report from User
# ──────────────────────────────────────────────
def collect_report() -> Dict:
    """Ask user for email details and return them"""
    
    # Print welcome header
    print("\n" + "=" * 50)
    print("       PHISHGUARD — Report Suspicious Email")
    print("=" * 50)
    print("Answer the questions below.\n")

    # Ask each piece of info
    print("📌 1. Sender")
    sender_email = input("  Sender email   : ").strip()
    sender_name  = input("  Sender name    : ").strip()

    print("\n📌 2. Email Content")
    subject = input("  Email subject  : ").strip()
    body    = input("  Email message  : ").strip()

    print("\n📌 3. Links & Attachments")
    print("  (Separate multiple with comma , )")
    links_text  = input("  Links found    : ").strip()
    attach_text = input("  Attachments    : ").strip()

    print("\n📌 4. Extra Info")
    suspicion = input("  Why suspicious? : ").strip()
    actions   = input("  Actions taken  : ").strip().lower()

    # Clean up lists (remove empty entries)
    links = [item.strip() for item in links_text.split(",") if item.strip()]
    files = [item.strip() for item in attach_text.split(",") if item.strip()]

    # Check: did they type the minimum needed?
    errors = []
    if not body:
        errors.append("⚠️  Please type the email message — it's needed!")
    if not sender_email and not sender_name:
        errors.append("⚠️  Need at least sender email OR name")

    # If something missing → show error, stop
    if errors:
        print("\n" + "-" * 50)
        for msg in errors:
            print(msg)
        print("-" * 50)
        return {}  # return empty = failed

    # All good → put everything into one neat package
    print("\n✅ Information collected successfully!\n")
    return {
        "sender_email": sender_email,
        "sender_name":  sender_name,
        "subject":      subject,
        "body":         body,
        "links":        links,
        "attachments":  files,
        "suspicion":    suspicion,
        "actions":      actions
    }

# ──────────────────────────────────────────────
# MAIN — Run Part 1
# ──────────────────────────────────────────────
def main():
    print("\n===== PART 1 TEST =====")
    
    # Call our function to get report
    report = collect_report()
    
    # If we got data → show it back to check
    if report:
        print("📋 Here's what you entered:\n")
        for key, value in report.items():
            print(f"  {key}: {value}")
        print("\n✅ PART 1 WORKS PERFECTLY!")

# Start the program
if __name__ == "__main__":
    main()