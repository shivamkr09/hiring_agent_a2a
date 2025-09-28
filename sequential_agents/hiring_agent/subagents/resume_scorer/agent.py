import datetime
from zoneinfo import ZoneInfo
from google.adk.agents import LlmAgent
from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset
from google.adk.tools.mcp_tool.mcp_session_manager import SseConnectionParams



resume_scorer_agent = LlmAgent(
    name="ResumeScorerAgent",
    model="gemini-2.0-flash",
    instruction="""You are an expert resume scorer. 
    Your task is to score the provided resume against the given job description.
    The score should be an integer between 0 and 100.
    
    **Resume:**
    {+resume}
    
    **Job Description:**
    {+job_description}
    
    **Scoring Criteria:**
    1.  **Skills Match:** How well do the candidate's skills match the job requirements?
    2.  **Experience Match:** How relevant is the candidate's experience to the job?
    3.  **Education Match:** Does the candidate's education meet the job requirements?
    
    **Output:**
    Provide only the integer score.
    """,
    description="Scores a resume against a job description.",
    output_key="resume_score",
)
