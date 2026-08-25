# LangGraph Agentic AI

A practical learning repository for building **agentic AI applications with LangGraph, LangChain, and Python**.

This repository explores the core concepts required to design, build, debug, and extend stateful AI workflows. The projects progress from a basic conversational chatbot to human-in-the-loop workflows, debugging techniques, and multi-agent systems.

The goal is to understand **how agentic AI applications are structured internally**, rather than simply using pre-built abstractions.

---

## Overview

Modern AI applications often require more than a single prompt sent to an LLM.

Real-world applications may need to:

* Maintain conversation state
* Execute multiple steps
* Call tools
* Make decisions based on intermediate results
* Pause and request human input
* Resume execution
* Coordinate multiple agents
* Handle failures and debugging
* Maintain predictable application workflows

**LangGraph** provides a framework for building these kinds of stateful, controllable workflows.

This repository provides progressively structured examples to understand these concepts through practical implementations.

---

## Learning Path

The repository is organized as a progressive learning path:

```text
┌───────────────────────┐
│  1. Basic Chatbot     │
│  Graph & State Basics │
└───────────┬───────────┘
            │
            ▼
┌───────────────────────┐
│  2. Human Assistance  │
│  Human-in-the-Loop    │
└───────────┬───────────┘
            │
            ▼
┌───────────────────────┐
│  3. Debugging         │
│  Debug & Understand   │
│  Agent Execution      │
└───────────┬───────────┘
            │
            ▼
┌───────────────────────┐
│  4. Agents            │
│  Multi-Agent Systems  │
└───────────────────────┘
```

Each section builds on concepts introduced earlier.

---

# Projects

## 1. Basic Chatbot

**Directory:** `1-BasicChatbot/`

This project introduces the fundamentals of creating a conversational workflow using LangGraph.

The focus is on understanding the basic building blocks required to construct a graph-based AI application.

### Concepts

* LangGraph fundamentals
* Graph-based workflows
* State management
* Messages
* Nodes
* Edges
* Conversational interaction
* Basic LLM integration

### Files

```text
1-BasicChatbot/
└── 1-basicchatbot.ipynb
```

The notebook provides an interactive environment for experimenting with the concepts.

---

## 2. Human Assistance

**Directory:** `2-HumanAssistance/`

This project explores **human-in-the-loop AI workflows**.

Not every decision should be completely automated. In many applications, an AI system needs to pause execution, request human input or approval, and then continue processing.

LangGraph makes these types of workflows possible by allowing execution to be controlled and resumed.

### Concepts

* Human-in-the-loop workflows
* Interrupting graph execution
* Human approval
* State persistence
* Resuming workflows
* Combining automated and human decisions

### Files

```text
2-HumanAssistance/
└── humanintheloop.ipynb
```

This section demonstrates how AI systems can be designed with humans as part of the execution loop.

---

## 3. Debugging

**Directory:** `3-Debugging/`

This section focuses on understanding and debugging agentic workflows.

As AI applications become more complex, debugging becomes increasingly important. A workflow may contain multiple nodes, decisions, state transitions, and model calls.

Understanding what happens during graph execution is essential when developing reliable agentic applications.

### Concepts

* Agent execution
* Graph execution
* Debugging workflows
* Understanding intermediate states
* LangGraph development configuration
* Agent application structure

### Files

```text
3-Debugging/
├── agent.py
├── debugging.ipynb
└── langgraph.json
```

The `agent.py` file contains the agent implementation, while the notebook provides an interactive environment for exploring the debugging concepts.

The `langgraph.json` file provides LangGraph-specific project configuration.

---

## 4. Agents

**Directory:** `4-Agents/`

This section moves toward more advanced agentic architectures.

Instead of relying on a single AI agent, multiple agents can be designed to work together, with each agent responsible for a particular role or task.

### Concepts

* AI agents
* Multiple agents
* Agent collaboration
* Task delegation
* Agent coordination
* Multi-agent workflows
* Structured agent architectures

### Files

```text
4-Agents/
└── multiaiagent.ipynb
```

This project demonstrates the foundation of building systems where multiple AI agents can participate in a larger workflow.

---

# Core Concepts Covered

Throughout the repository, the projects explore several important concepts in agentic AI development.

## Graph-Based Workflows

LangGraph represents application logic as a graph.

A graph generally consists of:

```text
State
  │
  ▼
Node
  │
  ▼
Decision
  │
  ├──────────► Node A
  │
  └──────────► Node B
```

This approach makes complex workflows easier to reason about because individual operations can be represented as separate nodes.

---

## State Management

State is one of the most important concepts in LangGraph.

Instead of treating every model call as an isolated operation, the application can maintain information throughout the workflow.

For example:

```text
User Input
    │
    ▼
State
    │
    ▼
LLM Processing
    │
    ▼
Updated State
    │
    ▼
Next Node
```

This allows applications to maintain context across multiple steps.

---

## Nodes

A node represents a unit of work within a graph.

Depending on the application, a node could:

* Call an LLM
* Execute business logic
* Process data
* Call a tool
* Ask for human input
* Delegate a task
* Produce an intermediate result

Breaking an application into nodes makes the workflow easier to understand, test, and extend.

---

## Edges

Edges determine how execution moves between nodes.

A simple workflow might look like:

```text
START
  │
  ▼
Agent
  │
  ▼
Tool
  │
  ▼
Agent
  │
  ▼
END
```

Conditional edges can also be used when the next step depends on the current state.

---

## Human-in-the-Loop

Human-in-the-loop systems allow an AI workflow to stop at specific points and wait for human intervention.

A simplified workflow can be represented as:

```text
User Request
     │
     ▼
AI Processing
     │
     ▼
Human Review
     │
     ├── Approve ──► Continue
     │
     └── Reject ───► Revise
```

This pattern is particularly useful when decisions require human judgment, approval, or oversight.

---

## Agents

An AI agent can be viewed as a system capable of deciding what actions should be performed to accomplish a goal.

A simplified agent workflow can look like:

```text
User Goal
    │
    ▼
Agent
    │
    ├──► Reason
    │
    ├──► Choose Action
    │
    ├──► Use Tool
    │
    └──► Continue
           │
           ▼
        Result
```

LangGraph provides a structured way to represent and control these workflows.

---

## Multi-Agent Systems

Complex tasks can sometimes be divided among multiple specialized agents.

For example:

```text
                  ┌───────────────┐
                  │   Supervisor  │
                  └───────┬───────┘
                          │
              ┌───────────┼───────────┐
              ▼           ▼           ▼
        ┌──────────┐ ┌──────────┐ ┌──────────┐
        │ Research │ │ Analysis │ │  Writer  │
        │  Agent   │ │  Agent   │ │  Agent   │
        └──────────┘ └──────────┘ └──────────┘
              │           │           │
              └───────────┼───────────┘
                          ▼
                       Result
```

Each agent can have a specific responsibility while the overall workflow coordinates their execution.

---

# Repository Structure

```text
LangGraph_Agentic/
│
├── 1-BasicChatbot/
│   └── 1-basicchatbot.ipynb
│
├── 2-HumanAssistance/
│   └── humanintheloop.ipynb
│
├── 3-Debugging/
│   ├── agent.py
│   ├── debugging.ipynb
│   └── langgraph.json
│
├── 4-Agents/
│   └── multiaiagent.ipynb
│
├── src/
│   └── langgraph_agentic/
│       └── __init__.py
│
├── .gitignore
├── .python-version
├── README.md
├── main.py
├── pyproject.toml
├── requirements.txt
└── uv.lock
```

---

# Technology Stack

The repository is primarily built with the following technologies:

| Technology              | Purpose                                   |
| ----------------------- | ----------------------------------------- |
| **Python**              | Primary programming language              |
| **LangGraph**           | Stateful AI and agentic workflows         |
| **LangChain**           | LLM application framework                 |
| **LangChain Community** | Community integrations and components     |
| **Jupyter Notebook**    | Interactive experimentation and learning  |
| **uv**                  | Python package and environment management |
| **Git**                 | Version control                           |
| **GitHub**              | Source code hosting                       |

---

# Requirements

Before running the projects, make sure the following are installed:

* Python
* Git
* `uv`
* Jupyter Notebook or a compatible IDE
* Required LLM/API credentials where applicable

The project uses a Python virtual environment and dependency management through `uv`.

---

# Getting Started

## 1. Clone the Repository

```bash
git clone https://github.com/Anipireddy-Pavan/LangGraph_Agentic.git
```

Move into the project directory:

```bash
cd LangGraph_Agentic
```

---

## 2. Create the Virtual Environment

Using `uv`:

```bash
uv venv
```

On Windows:

```bash
.venv\Scripts\activate
```

After activation, your terminal should indicate that the virtual environment is active.

For example:

```text
(LangGraph_Agentic) C:\LangGraph_Agentic>
```

---

## 3. Install Dependencies

The repository includes a `pyproject.toml` and `uv.lock`, so the recommended approach is:

```bash
uv sync
```

This installs the dependencies defined for the project and uses the lock file to provide reproducible package versions.

Alternatively, dependencies can be installed from `requirements.txt`:

```bash
uv pip install -r requirements.txt
```

---

# Running the Projects

The projects are primarily provided as Jupyter notebooks.

Start Jupyter from the project root:

```bash
jupyter notebook
```

Then open the desired notebook.

Recommended order:

```text
1-BasicChatbot
      ↓
2-HumanAssistance
      ↓
3-Debugging
      ↓
4-Agents
```

Following this order provides a gradual progression from basic LangGraph concepts to more advanced agentic workflows.

---

# Environment Variables

AI applications commonly require API credentials for the underlying model provider.

For local development, credentials should be stored in environment variables rather than hard-coded into Python files.

For example:

```text
MODEL_API_KEY=your_api_key
```

The exact environment variables depend on the model provider used by the individual project.

### Important

Never commit API keys, passwords, tokens, or other secrets to Git.

A local `.env` file can be used for development when appropriate, and sensitive files should be excluded through `.gitignore`.

---

# Development Workflow

A typical workflow for extending this repository is:

```text
1. Create or modify a project
          ↓
2. Install/update dependencies
          ↓
3. Run the notebook or application
          ↓
4. Test the workflow
          ↓
5. Debug graph execution
          ↓
6. Commit changes
          ↓
7. Push to GitHub
```

For example:

```bash
git status
git add .
git commit -m "Add new LangGraph workflow"
git push
```

---

# Why LangGraph?

Traditional LLM applications often follow a simple pattern:

```text
Input → LLM → Output
```

Agentic applications frequently require more control:

```text
                    ┌───────────────┐
                    │     Input     │
                    └───────┬───────┘
                            ▼
                    ┌───────────────┐
                    │     Agent     │
                    └───────┬───────┘
                            ▼
                    ┌───────────────┐
                    │ Decision/Tool │
                    └───────┬───────┘
                            ▼
                    ┌───────────────┐
                    │ Updated State │
                    └───────┬───────┘
                            │
                  ┌─────────┴─────────┐
                  ▼                   ▼
              Continue              Human
                  │                 Review
                  └─────────┬─────────┘
                            ▼
                         Result
```

LangGraph is useful when an application requires explicit control over:

* State
* Execution flow
* Conditional routing
* Tool usage
* Human intervention
* Agent coordination
* Long-running workflows

This repository focuses on understanding those building blocks through practical examples.

---

# Learning Objectives

After working through this repository, you should have a better understanding of:

* How LangGraph applications are structured
* How graph-based workflows operate
* How state is passed through a workflow
* How nodes and edges control execution
* How conversational applications maintain context
* How human-in-the-loop workflows can be implemented
* How to inspect and debug agentic workflows
* How individual AI agents can be structured
* How multiple agents can collaborate
* How to organize LangGraph projects using Python
* How to manage Python dependencies with `uv`

# Contributing

Contributions, improvements, and suggestions are welcome.

If you would like to contribute:

1. Fork the repository.
2. Create a feature branch.
3. Make your changes.
4. Test your changes.
5. Commit your changes.
6. Open a pull request.

Example:

```bash
git checkout -b feature/new-agent
git add .
git commit -m "Add new agent workflow"
git push origin feature/new-agent
```

---

# Author

**Anipireddy Pavan**

GitHub:
https://github.com/Anipireddy-Pavan

---

# License

This repository is intended primarily for **educational and learning purposes**.

If you plan to use or distribute the code in a production environment, review and add an appropriate open-source license to the repository.

---

## Repository Goal

The main objective of this repository is to build a strong practical foundation in **LangGraph and Agentic AI development** by progressing from simple workflows to increasingly sophisticated AI agent architectures.

```text
Learn
  ↓
Build
  ↓
Debug
  ↓
Experiment
  ↓
Extend
  ↓
Build Production-Ready Agents
```
