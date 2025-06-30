from langchain_community.chat_models import ChatOllama
from langchain_core.messages import HumanMessage, AIMessage
from langgraph.prebuilt import create_react_agent

def main():
    model = ChatOllama(model="llama3")  # No API key needed

    tools = []
    agent_executer = create_react_agent(model, tools)

    print("welcome to the AI Agent!")
    print("You can ask me anything, and I will try to help you.")

    while True:
        user_input = input("\nYou: ").strip()
        if user_input.lower() in ["exit", "quit"]:
            print("Exiting the AI Agent. Goodbye!")
            break

        print("\n Assistant: ", end="")
        try:
            for chunk in agent_executer.stream({"messages": [HumanMessage(content=user_input)]}):
                if "agent" in chunk and "messages" in chunk["agent"]:
                    for message in chunk["agent"]["messages"]:
                        print(message.content, end="")
        except Exception as e:
            print(f"\n[Error] {e}")

        print()

if __name__ == "__main__":
    main()
