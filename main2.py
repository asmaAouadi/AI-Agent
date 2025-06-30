from langchain_community.chat_models import ChatOllama
from langchain_core.messages import HumanMessage
from langgraph.prebuilt import create_react_agent
import threading

# Agents
fast_agent = create_react_agent(ChatOllama(model="phi3"), tools=[])
slow_agent = create_react_agent(ChatOllama(model="llama3"), tools=[])

def run_slow_agent(user_input):
    response = slow_agent.invoke({"messages": [HumanMessage(content=user_input)]})
    print("\n[Background Insight]", response["agent"]["messages"][0].content)

def main():
    print("Multi-Agent AI is ready.")
    while True:
        user_input = input("\nYou: ").strip()
        if user_input in ["exit", "quit"]:
            break

        print("\nFast Agent: ", end="")
        response = fast_agent.invoke({"messages": [HumanMessage(content=user_input)]})
        print(response["agent"]["messages"][0].content)


        threading.Thread(target=run_slow_agent, args=(user_input,), daemon=True).start()

if __name__ == "__main__":
    main()
