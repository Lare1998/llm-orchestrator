
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
# Update on 2023-02-20 00:00:00
# Update on 2023-02-20 00:00:00
# Update on 2023-02-22 00:00:00
# Update on 2023-02-23 00:00:00
# Update on 2023-02-24 00:00:00
# Update on 2023-02-27 00:00:00
# Update on 2023-02-28 00:00:00
# Update on 2023-02-28 00:00:00
# Update on 2023-02-28 00:00:00
# Update on 2023-03-03 00:00:00
# Update on 2023-03-03 00:00:00
# Update on 2023-03-06 00:00:00
# Update on 2023-03-06 00:00:00
# Update on 2023-03-09 00:00:00
# Update on 2023-03-10 00:00:00
# Update on 2023-03-10 00:00:00
# Update on 2023-03-13 00:00:00
# Update on 2023-03-13 00:00:00
# Update on 2023-03-13 00:00:00
# Update on 2023-03-15 00:00:00
# Update on 2023-03-16 00:00:00
# Update on 2023-03-17 00:00:00
# Update on 2023-03-22 00:00:00
# Update on 2023-03-27 00:00:00
# Update on 2023-03-27 00:00:00
# Update on 2023-03-28 00:00:00
# Update on 2023-03-29 00:00:00
# Update on 2023-03-30 00:00:00
# Update on 2023-03-31 00:00:00
# Update on 2023-03-31 00:00:00
# Update on 2023-03-31 00:00:00
# Update on 2023-04-03 00:00:00
# Update on 2023-04-03 00:00:00
# Update on 2023-04-04 00:00:00
# Update on 2023-04-05 00:00:00
# Update on 2023-04-05 00:00:00
# Update on 2023-04-06 00:00:00
# Update on 2023-04-10 00:00:00
# Update on 2023-04-11 00:00:00
# Update on 2023-04-11 00:00:00
# Update on 2023-04-13 00:00:00
# Update on 2023-04-17 00:00:00
# Update on 2023-04-18 00:00:00
# Update on 2023-04-19 00:00:00
# Update on 2023-04-20 00:00:00
# Update on 2023-04-21 00:00:00
# Update on 2023-04-25 00:00:00
# Update on 2023-04-26 00:00:00
# Update on 2023-04-26 00:00:00
# Update on 2023-04-28 00:00:00
# Update on 2023-04-28 00:00:00
# Update on 2023-05-03 00:00:00
# Update on 2023-05-03 00:00:00
# Update on 2023-05-03 00:00:00
# Update on 2023-05-04 00:00:00
# Update on 2023-05-09 00:00:00
# Update on 2023-05-11 00:00:00
# Update on 2023-05-16 00:00:00
# Update on 2023-05-17 00:00:00
# Update on 2023-05-18 00:00:00
# Update on 2023-05-18 00:00:00
# Update on 2023-05-18 00:00:00
# Update on 2023-05-23 00:00:00
# Update on 2023-05-24 00:00:00
# Update on 2023-05-25 00:00:00
# Update on 2023-05-29 00:00:00
# Update on 2023-06-01 00:00:00
# Update on 2023-06-05 00:00:00
# Update on 2023-06-07 00:00:00
# Update on 2023-06-08 00:00:00
# Update on 2023-06-08 00:00:00
# Update on 2023-06-12 00:00:00
# Update on 2023-06-12 00:00:00