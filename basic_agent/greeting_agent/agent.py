import datetime
from zoneinfo import ZoneInfo
from google.adk.agents import Agent
from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset
from google.adk.tools.mcp_tool.mcp_session_manager import SseConnectionParams



def get_current_time(city: str) -> dict:
    """Returns the current time in a specified city.

    Args:
        city (str): The name of the city for which to retrieve the current time.

    Returns:
        dict: status and result or error msg.
    """

    if city.lower() == "new york":
        tz_identifier = "America/New_York"
    else:
        return {
            "status": "error",
            "error_message": (
                f"Sorry, I don't have timezone information for {city}."
            ),
        }

    tz = ZoneInfo(tz_identifier)
    now = datetime.datetime.now(tz)
    report = (
        f'The current time in {city} is {now.strftime("%Y-%m-%d %H:%M:%S %Z%z")}'
    )
    return {"status": "success", "report": report}


root_agent = Agent(
    name="RecruitingAgent",
    model="gemini-2.0-flash",
    description=(
        "You are an recruting agent who will make the mcp tool work for you. You have access to tools that can help you to do resume parsing, linkedin profile parsing, and application processing. Use these tools to evaluate a candidate based on their resume and LinkedIn profile. "
    ),
    instruction=(
        '''You are a recruiting agent who will evaluate resume with Job Description in addition with LinkedIn and GitHub. You are provided with various tools to evaluate a job application. First you will fetch all the unprocessed applications. Parse the resume and evaluate based on the job description. After resume parsing you will get linkedIn and GitHub url in Resume. Parse both LinkedIn and GitHub. After everything is done save the information in db and at last update the application to processed state. You are provided with all the tools to perform the task, use those tools to make it happen.

Things you need to consider are if jd requires some years of experience then low and high of 2 will be best but not more than that. For example if Job Description states that candidate of 8 years of experience is required then candidate of 6 - 10 can be a best fit , so use this formula during evaluation.'''
    ),
    tools=[get_current_time,
           MCPToolset(
            # 2. Use SseConnectionParams with the server URL from Step 1.
            connection_params=SseConnectionParams(
                # Ensure this URL matches the one your MCP server is listening on.
                url='http://localhost:5090/sse'
            ),
            # Optional: Filter which tools from the MCP server are exposed
            # tool_filter=['list_directory', 'read_file']
        )
           ],
)