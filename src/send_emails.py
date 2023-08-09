from gmail_draft_creator import create_draft, send_drafts_from_csv

create_draft(
    "ryanstout@gmail.com",
    "Hey, how's it going?\n\n2nd line for testing.",
    template_params={"name": "Ryan"},
    subject="Test subject",
)
