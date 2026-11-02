## Langchain expression language (LCEL)
This is predefined workflow for simple workflow.

`chain = prompt | llm` ==> `chain.invoke(formatter_dictionary)` will inject formatter dictionary to prompt and result to llm.

## Langgraph
1. Unlike LCEL, workflow is dynamic and based on user query context.
2. A node a specific function that performs a specific operation --> it also updates the GraphState.
3. Key components
    - Node
    - Edge --> (Normal, Conditional)
    - State
### Reducer in Langraph
Suppose four agents independently produce findings. We might want to append all their findings into one shared list instead of one agent overwriting another's result. LangGraph reducers allow us to define that behavior.

## TypedDict
1. It does static type checking but no runtime validation.
2. At runtime this is simple dictionary only.
3. Mostly used in IDE type checks and better coding experience.
