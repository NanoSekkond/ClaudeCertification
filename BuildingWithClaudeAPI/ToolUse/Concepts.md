# Tools
A tool is a program Claude knows the existence of and can call if it thinks will be useful for the answer. A tool can be an executable or even just a function.

## Tools functions
The names and parameters should be descriptive. Validate the parameters and on error throw a descriptive error since Claude might try to call the tool again after reading the error.

## Fine Grained Tool Calling
When generating JSON the anthropic API waits for the JSON to be valid before sending it during streaming. This means that streaming is not as smooth as it should, to fix this we enable Fine Grained Tool Calling. However now we have to validate the JSON before use.

## Built in Tools

### Text Editor Tool
A tool already integrated into Claude, it has the schema, not the function. This means that if we provide an implementation of Read, Write, Create and Delete then Claude should be able to use them. We still send a small schema that then gets turned into a bigger one inside of the Claude API.

### Web Search Tool
A tool already integrated into Claude, it has the schema and the implementation already. We still send a small schema that then gets turned into a bigger one inside of the Claude API. We can add a parameter of allowed_domains so Claude searches only there.