from langchain_openai import ChatOpenAI
from langchain.prompts.chat import (
    HumanMessagePromptTemplate,
    ChatPromptTemplate,
)
from langchain.chains import LLMChain

from langchain.prompts.chat import (
    SystemMessagePromptTemplate,
)

system_template = SystemMessagePromptTemplate.from_template(
    """
    You are an expert computer programmer, review the user provided code, and summarize its functionality. 
    If applicable, identify potential improvements and suggest corrections, explaining them briefly.
    Find potential security issues in the code and suggest resolutions.
    If the code is well-written, express appreciation.

    If there are multiple files to review, add a header representing each file and follow up with respective review.

    Make the code easier to read and maintain!

    Restrict your responses to code review requests, if a user asks anything other than code reviews, reject the request politely!
    """
)


# Create the LLM and prompt templates
llm = ChatOpenAI(temperature=0, model_name="gpt-4-1106-preview")

user_template = HumanMessagePromptTemplate.from_template("{user_prompt}")
template = ChatPromptTemplate.from_messages([system_template, user_template])
chain = LLMChain(llm=llm, prompt=template)


def get_code_review(user_prompt):
    """Retrieves a code review from the LLM based on the user's prompt."""
    return chain.invoke({"user_prompt": user_prompt}).get(
        "text", "No review available."
    )
