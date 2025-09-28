import datetime
from zoneinfo import ZoneInfo
from google.adk.agents import Agent
from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset
from google.adk.tools.mcp_tool.mcp_session_manager import SseConnectionParams
from google.adk.agents import SequentialAgent

from .subagents.resume_scorer.agent import resume_scorer_agent
from .subagents.linkedin_finder.agent import linkedin_finder_agent
from .subagents.summarizer.agent import summarizer_agent
from .subagents.notifier.agent import notifier_agent
root_agent = SequentialAgent(
    name="HiringAgent",
    description=(
        "Agent to assist with the hiring process."
    ),
    sub_agents=[
       resume_scorer_agent,
       linkedin_finder_agent,
       summarizer_agent,
       notifier_agent
    ],
)