
from llm_orchestrator.agent import LLMAgent, Orchestrator

if __name__ == "__main__":
    print("Starting LLM Orchestrator application...")

    # Initialize agents
    data_analyst = LLMAgent("DataAnalyst", "analyzes data", ["data_analysis", "report_generation"], model="gpt-4")
    content_writer = LLMAgent("ContentWriter", "generates content", ["text_generation", "summarization"], model="gpt-3.5-turbo")
    
    # Create an orchestrator instance
    orchestrator = Orchestrator(agents=[data_analyst, content_writer])

    # Define a complex workflow
    goal = "Develop a comprehensive marketing strategy for a new AI product."
    steps = [
        {"description": "Research market trends and competitor analysis", "required_capabilities": ["data_analysis"]},
        {"description": "Generate initial product messaging and value propositions", "required_capabilities": ["text_generation"]},
        {"description": "Summarize research findings for executive review", "required_capabilities": ["summarization"]},
        {"description": "Draft marketing campaign outlines", "required_capabilities": ["text_generation"]},
        {"description": "Analyze campaign performance metrics", "required_capabilities": ["data_analysis"]},
        {"description": "Generate final report on marketing strategy", "required_capabilities": ["report_generation"]},
    ]

    # Run the workflow
    results = orchestrator.run_workflow(goal, steps)
    print("\nWorkflow execution complete. Results:")
    for res in results["steps_results"]:
        print(f"- Task {res["task_id"][:8]}...: {res["status"]} - {res["output"]}")

    print("\nLLM Orchestrator application finished.")

# Update on 2023-01-06 00:00:00
# Update on 2023-01-10 00:00:00
# Update on 2023-01-12 00:00:00
# Update on 2023-01-13 00:00:00
# Update on 2023-01-13 00:00:00
# Update on 2023-01-17 00:00:00
# Update on 2023-01-20 00:00:00
# Update on 2023-01-25 00:00:00
# Update on 2023-01-27 00:00:00
# Update on 2023-01-30 00:00:00
# Update on 2023-01-30 00:00:00
# Update on 2023-01-31 00:00:00
# Update on 2023-02-01 00:00:00
# Update on 2023-02-02 00:00:00
# Update on 2023-02-03 00:00:00
# Update on 2023-02-03 00:00:00
# Update on 2023-02-06 00:00:00
# Update on 2023-02-07 00:00:00
# Update on 2023-02-08 00:00:00
# Update on 2023-02-08 00:00:00
# Update on 2023-02-13 00:00:00
# Update on 2023-02-14 00:00:00
# Update on 2023-02-15 00:00:00
# Update on 2023-02-16 00:00:00