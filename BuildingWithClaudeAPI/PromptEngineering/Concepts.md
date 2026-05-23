# Basic improvements
1. Be clear and direct, specially on the first line. Simple words and specific action.
2. Be specific, make a list of guidelines of points the agent should take into account. These can be steps to follow or qualities the output should have.
    1. Use qualities most of the time.
    2. On more complex problems with multiple paths to take it's better to provide guidance.
3. Add examples of input and outputs, ideally wrap them in XML tags (more on that later). Try to explain why the output is good for that input.
- Oneshot prompting: One example.
- Multishot prompting: Multiple examples.

# XML tags
On prompts where you insert data externally it's better to wrap it around tags to define structure. Example:

```
Could you make a summary of the following paper?

<paper_content>
{paper.content}
</paper_content>

Here are my class notes:
<class_notes>
{class_notes}
</class_notes>

Try to include the following:
1. Main concepts.
2. Link it with my notes.
3. Explain deeply the main proofs show in the paper.
```

We define a clear limit between my notes and the paper content.