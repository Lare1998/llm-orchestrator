import os
import json
from typing import List, Dict, Any, Optional
from datetime import datetime

# Placeholder for an actual LLM API client (e.g., OpenAI, Anthropic)
class LLMClient:
    def __init__(self, api_key: str, model_name: str = "gpt-4.1-mini"):
        self.api_key = api_key
        self.model_name = model_name
        # In a real scenario, initialize the actual LLM client here
        print(f"LLMClient initialized with model: {self.model_name}")

    def generate_response(self, prompt: str, temperature: float = 0.7, max_tokens: int = 150) -> str:
        """
        Simulates generating a response from an LLM.
        In a real implementation, this would call the LLM API.
        """
        print(f"[LLM Call] Prompt: {prompt[:100]}...")
        # Dummy response for demonstration
        if "summarize" in prompt.lower():
            return f"Summary of the provided text: {prompt[-50:]}..."
        elif "question" in prompt.lower():
            return f"Answer to your question: The current date is {datetime.now().strftime('%Y-%m-%d')}."
        else:
            return f"LLM response to: {prompt[:50]}... (simulated)"

class Agent:
    """
    Base class for an LLM-powered agent within the orchestration framework.
    """
    def __init__(self, name: str, description: str, llm_client: LLMClient):
        self.name = name
        self.description = description
        self.llm_client = llm_client
        self.history: List[Dict[str, str]] = []
        print(f"Agent \'{self.name}\' initialized.")

    def process_message(self, message: str) -> str:
        """
        Processes an incoming message and generates a response using the LLM.
        """
        self.history.append({"role": "user", "content": message})
        prompt = self._construct_prompt(message)
        response = self.llm_client.generate_response(prompt)
        self.history.append({"role": "agent", "content": response})
        return response

    def _construct_prompt(self, user_message: str) -> str:
        """
        Constructs the prompt for the LLM based on agent's role and conversation history.
        """
        system_message = f"You are {self.name}, a {self.description}."
        conversation_context = "\n".join([f"{msg['role']}: {msg['content']}" for msg in self.history])
        return f"{system_message}\n\nConversation History:\n{conversation_context}\n\nUser: {user_message}\nAgent:"

class Workflow:
    """
    Manages the orchestration of multiple agents to complete a task.
    """
    def __init__(self):
        self.agents: Dict[str, Agent] = {}
        self.task_log: List[Dict[str, Any]] = []
        print("Workflow initialized.")

    def add_agent(self, agent: Agent):
        """
        Adds an agent to the workflow.
        """
        if agent.name in self.agents:
            logger.warning(f"Agent \'{agent.name}\' already exists and will be overwritten.")
        self.agents[agent.name] = agent
        print(f"Agent \'{agent.name}\' added to workflow.")

    def run_task(self, initial_prompt: str, agent_sequence: List[str], max_iterations: int = 5) -> str:
        """
        Executes a task by passing messages sequentially through a defined agent sequence.
        """
        current_message = initial_prompt
        self.task_log.append({"timestamp": str(datetime.now()), "event": "Task Started", "initial_prompt": initial_prompt})
        print(f"[Workflow] Starting task with initial prompt: {initial_prompt}")

        for i in range(max_iterations):
            if not agent_sequence:
                logger.error("Agent sequence is empty. Cannot run task.")
                break

            current_agent_name = agent_sequence[i % len(agent_sequence)] # Cycle through agents
            if current_agent_name not in self.agents:
                logger.error(f"Agent \'{current_agent_name}\' not found in workflow. Skipping.")
                continue

            agent = self.agents[current_agent_name]
            print(f"[Workflow] Passing message to agent \'{agent.name}\'...")
            response = agent.process_message(current_message)
            self.task_log.append({
                "timestamp": str(datetime.now()),
                "event": "Agent Interaction",
                "agent": agent.name,
                "input": current_message,
                "output": response
            })
            current_message = response
            print(f"[Workflow] Agent \'{agent.name}\' responded: {response[:70]}...")

        self.task_log.append({"timestamp": str(datetime.now()), "event": "Task Finished", "final_output": current_message})
        print(f"[Workflow] Task finished. Final output: {current_message[:100]}...")
        return current_message

    def get_task_log(self) -> List[Dict[str, Any]]:
        """
        Returns the log of the executed task.
        """
        return self.task_log

if __name__ == "__main__":
    # Initialize LLM Client (using a dummy API key for demonstration)
    llm_client = LLMClient(api_key="dummy_key")

    # Create agents
    research_agent = Agent("Researcher", "an expert in finding and synthesizing information", llm_client)
    writer_agent = Agent("Writer", "a creative content generator", llm_client)
    editor_agent = Agent("Editor", "a meticulous proofreader and refiner", llm_client)

    # Create a workflow
    workflow = Workflow()
    workflow.add_agent(research_agent)
    workflow.add_agent(writer_agent)
    workflow.add_agent(editor_agent)

    # Define agent sequence for a task
    agent_sequence = ["Researcher", "Writer", "Editor"]

    # Run a task
    final_result = workflow.run_task(
        initial_prompt="Research the latest trends in AI ethics and write a short report.",
        agent_sequence=agent_sequence,
        max_iterations=3
    )

    print("\n--- Final Task Result ---")
    print(final_result)
    print("\n--- Task Log ---")
    for entry in workflow.get_task_log():
        print(json.dumps(entry, indent=2))
