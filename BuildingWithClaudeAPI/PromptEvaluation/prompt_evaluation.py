import json
import re
from BuildingWithClaudeAPI.AccessingClaudeAPI.claude_api import json_chat, chat

def generate_dataset():
    dataset = json_chat(
        """Generate me a json file that has 5 sample user inputs for a prompt. The inputs should be asking for help with a specific regex. The json output should look like this:
        [
            {
                "input" : "What regex should I use to remove all double spaces in a string?",
                "test_cases" : ["hello  world   ", "hi I'm  a     text"],
                "outputs" : ["hello world ", "hi I'm a text"],
                "task" : "Substitution" or "Matching" or "Validation",
                "replacement" : " " or "*" only if the task is "Substitution"
            }
        ]""",
    "", 1.0)
    with open("./BuildingWithClaudeAPI/PromptEvaluation/dataset.json", "w") as f:
        json.dump(json.loads(dataset), f, indent=4)

def run_prompt(prompt, test_case):
    prompt = f"{prompt}\n{test_case["input"]}"
    output = chat([], prompt, "", 1.0)
    return output

def run_testcase(prompt, test_case):
    output = run_prompt(prompt, test_case)
    score = grade_by_code(test_case, output)
    return {
        "output" : output,
        "test_case" : test_case,
        "score" : score
    }

def run_eval(prompt):
    results = []
    with open("./BuildingWithClaudeAPI/PromptEvaluation/dataset.json", "r") as f:
        dataset = json.load(f)
    for test_case in dataset:
        result = run_testcase(prompt, test_case)
        results.append(result)
    return results

def grade_by_model(test_case, output):
    # This is a bit too insane for my liking, I ain't doing this.
    pass

def grade_by_code(test_case, output):
    score = validate_regex(output, test_case)
    return score

def validate_regex(output, test_case):
    try:
        pattern = re.compile(output.strip())
    except re.error:
        return 0

    task = test_case["task"]
    correct = 0

    for test_input, expected in zip(test_case["test_cases"], test_case["outputs"]):
        if task == "Validation":
            result = bool(pattern.fullmatch(test_input.strip()))
            correct += result == expected

        elif task == "Matching":
            result = pattern.findall(test_input)
            correct += result == expected

        elif task == "Substitution":
            replacement = test_case.get("replacement", "")
            result = pattern.sub(replacement, test_input)
            correct += result == expected

    return (correct / len(test_case["test_cases"])) * 10

def grade_output(regex_str, test_case):
    try:
        pattern = re.compile(regex_str.strip())
    except re.error:
        return 0

    task = test_case["task"]
    correct = 0

    for test_input, expected in zip(test_case["test_cases"], test_case["outputs"]):
        if task == "Validation":
            result = bool(pattern.fullmatch(test_input.strip()))
            correct += result == expected

        elif task == "Matching":
            result = pattern.findall(test_input)
            correct += result == expected

        elif task == "Substitution":
            result = pattern.sub(" ", test_input)  # Claude needs to provide replacement too, see note
            correct += result == expected

    return (correct / len(test_case["test_cases"])) * 10

def prompt_test_v1():
    prompt = """Please solve the following task:"""
    results = run_eval(prompt)
    print(json.dumps(results, indent=4))
    avg = sum(r["score"] for r in results) / len(results)
    print(f"Average score: {avg:.2f}")

def prompt_test_v2():
    prompt = """You will be giving a regex related problem, solve the issue and output ONLY the regex string without comments, it should compile to python re package. Do not add backticks or any kind of markdown format, just the string."""
    results = run_eval(prompt)
    print(json.dumps(results, indent=4))
    avg = sum(r["score"] for r in results) / len(results)
    print(f"Average score: {avg:.2f}")

def main():
    prompt_test_v2()

if __name__ == "__main__":
    main()