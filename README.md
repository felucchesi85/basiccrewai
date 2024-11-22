
# Labs Multi-Agent System

## Overview

This project implements a multi-agent system designed to perform tasks such as web scraping, data analysis, and job description generation. The agents interact with each other and the environment to achieve these goals efficiently.

## Agent Interaction and Communication Architecture

### Agent Roles and Tasks

1. **Online Researcher**
   - **Role:** Investigates topics online.
   - **Task:** Gather information and pass findings to the Blog Manager.
   - **Integration:** Uses `TavilySearchResults` and `process_search_tool` for data collection.

2. **Blog Manager**
   - **Role:** Writes and optimizes blog articles.
   - **Task:** Transform research findings into a blog post.
   - **Integration:** Utilizes SEO tools and editing capabilities.

3. **Social Media Manager**
   - **Role:** Creates social media content.
   - **Task:** Convert blog drafts into tweets.
   - **Integration:** Leverages social media tools for engagement optimization.

4. **Content Marketing Manager**
   - **Role:** Oversees content quality and publication.
   - **Task:** Review and approve content for publication.
   - **Integration:** Ensures compliance with content standards.

### Communication Architecture

- **Message Passing:** Agents communicate through a message-passing system, ensuring asynchronous and efficient data exchange.
- **Central Coordinator:** A central coordinator manages task assignments and monitors agent performance.

![Agent Communication Diagram](path/to/communication_diagram.png)

## Setup and Execution Instructions

### Required Dependencies

- Python 3.12+
- OpenAI API Key
- LangChain API Key
- Tavily API Key

### Installation

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/EurekaLabs/multi-agent-system.git
   cd multi-agent-system
   ```

2. **Install Dependencies:**
   ```bash
   poetry install
   ```

3. **Environment Configuration:**
   - Create a `.env` file in the root directory with the following content:
     ```
     OPENAI_API_KEY=your_openai_api_key
     LANGCHAIN_TRACING_V2=true
     LANGCHAIN_ENDPOINT=https://api.smith.langchain.com
     LANGCHAIN_API_KEY=your_langchain_api_key
     LANGCHAIN_PROJECT=your_project_name
     TAVILY_API_KEY=your_tavily_api_key
     ```

### Running the Project

1. **Start the System:**
   ```bash
   poetry run python app/multiagent.py
   ```

2. **Monitor Agent Activity:**
   - Use the logging system to track agent interactions and performance.

## Functional Example

### Workflow: Scraping, Analysis, Job Description

1. **Scraping:**
   - The Online Researcher scrapes data from specified sources and sends it to the Blog Manager.

2. **Analysis:**
   - The Blog Manager analyzes the data, creating a structured draft.

3. **Job Description:**
   - The Social Media Manager converts the draft into a job description and posts it on social media platforms.

![Workflow Diagram](path/to/workflow_diagram.png)

## Cost Considerations

- **API Usage:** Be aware of the costs associated with using the OpenAI, LangChain, and Tavily APIs. Monitor usage to optimize costs.
- **Infrastructure:** Consider the costs of hosting and maintaining the system, especially if scaling is required.

## Conclusion

This documentation provides a comprehensive guide for setting up and running the multi-agent system. By following the steps outlined, developers can easily understand and contribute to the project.
=======
