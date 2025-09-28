from google.adk.agents import LlmAgent

notifier_agent = LlmAgent(
    name="NotifierAgent",
    model="gemini-2.0-flash",
    instruction="""You are a helpful assistant.
    Your task is to draft two emails: one to the candidate who has been shortlisted, and another to HR.

    **Candidate Name:**
    {+candidate_name}

    **Candidate Email:**
    {+candidate_email}

    **HR Email:**
    {+hr_email}

    **Job Title:**
    {+job_title}

    **Output:**
    Provide two separate email drafts.
    """,
    description="Notifies the candidate and HR about the shortlisting.",
    output_key="notifications",
)
