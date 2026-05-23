# How to know a prompt is good enough
We want to run each prompt through some evaluation steps to give it a score and be sure it is ready for production. Basically testing for prompts. We give the score by running the output through a grader. There are three types:
1. Code: We run any code through the output string, check length, specific words, syntax, etc. The hard part is coming up with a system that returns 1 to 10 based on these parameters.
2. Model: We run the output to another model, more flexible than code but requires more API calls. We can check if the output follows the general question of the prompt.
3. Human: Someone evaluates it, it takes a lot of time.
