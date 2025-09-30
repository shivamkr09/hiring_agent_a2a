import datetime
from zoneinfo import ZoneInfo
from google.adk.agents import LlmAgent
from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset
from google.adk.tools.mcp_tool.mcp_session_manager import SseConnectionParams



linkedin_finder_agent = LlmAgent(
    name="LinkedInFinderAgent",
    model="gemini-2.0-flash",
    instruction="""You are an expert at finding LinkedIn profiles.
    Your task is to find the LinkedIn profile URL for the given candidate name and company and use the tools to parse the linked profile of the candidate and then return summary of it.

    **Candidate Name:**
    {+candidate_name}

    **Company:**
    {+company}

    **Output:**
    Provide a summary of the LinkedIn profile.
    If you cannot find the profile, output "Not Found".
    """,
    description="Finds a candidate's LinkedIn profile and use the tools to parse the linked profile of the candidate and then return summary of it",
    output_key="summary of linked profile",
    tools=[
        MCPToolset(
            # 2. Use SseConnectionParams with the server URL from Step 1.
            connection_params=SseConnectionParams(
                # Ensure this URL matches the one your MCP server is listening on.
                url='https://mcpserver-flight-delay-predictor-xeow.onrender.com/sse'
            ),
        )
    ]
)
