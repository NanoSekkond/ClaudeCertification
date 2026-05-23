import datetime
import inspect
import json
from BuildingWithClaudeAPI.AccessingClaudeAPI.claude_api import json_chat
from anthropic.types import ToolParam

def create_tool_json_schema(function):
    response = json_chat(
        f"""Write a valid JSON schema spec for tool calling this function:
        <function>
        {inspect.getsource(function)}
        </function>
        The JSON should follow the following format:
        <output_format>
        {{
            "name" : "function_name",
            "description" : "What the function does in 3 lines max",
            "input_schema" : "The actual input schema JSON object"
        }}
        </output_format>""",
    "", 1.0)
    with open(f"./BuildingWithClaudeAPI/ToolUse/{function.__name__}_schema.json", "w") as f:
        json.dump(json.loads(response), f, indent=4)

def get_tool_json_schema(function):
    with open(f"./BuildingWithClaudeAPI/ToolUse/{function.__name__}_schema.json", "r") as f:
        content = json.load(f)
    return ToolParam(content)

def get_current_datetime(date_format="%Y-%m-%d %H:%M:%S"):
    if not date_format:
        raise ValueError("date_format cannot be empty.")
    return datetime.now().strftime(date_format)

def main():
    pass

if __name__ == "__main__":
    main()