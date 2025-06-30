from langchain_core.messages import AIMessage, HumanMessage
from langchain_openai import ChatOpenAI
from langchain.tools import tool
from langgraph.prebuilt import create_react_agent
from dotenv import load_dotenv


load_dotenv()

def main():
    model = ChatOpenAI(temperature=0)

    tools = []
    agent_executer = create_react_agent(model,tools)


    print("welcome to the AI Agent!")
    print("You can ask me anything, and I will try to help you.")

    while True:
        user_input = input("\nYou: ").strip()

        if user_input == "exit" or user_input == "quit":
            print("Exiting the AI Agent. Goodbye!")
            break

        print("\n Assistant: ",end="")

        for  chunk in agent_executer.stream(   #to make the agent type word by word and not put the entire test directly
            {"messages": [HumanMessage(content=user_input)]}
        ):
            if "agent" in chunk and "messages" in chunk["agent"]:
                for message in chunk["agent"]["messages"]:
                    print(message.content, end="")
        
        print()
            

if __name__ == "__main__":
    main()

