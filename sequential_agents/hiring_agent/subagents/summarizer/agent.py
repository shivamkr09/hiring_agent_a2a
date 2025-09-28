import datetime
from zoneinfo import ZoneInfo
from google.adk.agents import LlmAgent
from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset
from google.adk.tools.mcp_tool.mcp_session_manager import SseConnectionParams




summarizer_agent = LlmAgent(
    name="SummarizerAgent",
    model="gemini-2.0-flash",
    instruction="""You are an expert hiring assistant.
    Your task is to summarize the provided information and determine if the candidate is a good fit for the job.

    **Resume Score:**
    {+resume_score}

    **LinkedIn Profile:**
    {+linkedin_url}

    **Job Description:**
    {+job_description}

    **Summary:**
    Provide a brief summary of the candidate's qualifications and a recommendation on whether to proceed with the hiring process.
    
    **Output:**
    Provide a summary and a "Fit" or "No Fit" recommendation.
    """,
    description="Summarizes candidate information and provides a hiring recommendation.",
    output_key="summary",
)
