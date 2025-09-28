import datetime
from zoneinfo import ZoneInfo
from google.adk.agents import LlmAgent
from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset
from google.adk.tools.mcp_tool.mcp_session_manager import SseConnectionParams



linkedin_finder_agent = LlmAgent(
    name="LinkedInFinderAgent",
    model="gemini-2.0-flash",
    instruction="""You are an expert at finding LinkedIn profiles.
    Your task is to find the LinkedIn profile URL for the given candidate name and company.

    **Candidate Name:**
    {+candidate_name}

    **Company:**
    {+company}

    **Output:**
    Provide only the LinkedIn profile URL.
    If you cannot find the profile, output "Not Found".
    """,
    description="Finds a candidate's LinkedIn profile.",
    output_key="linkedin_url",
)
