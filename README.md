# genpark-ai-sdr-website-visitor-pipeline-qualifier-skill

![Python 3.9+](https://img.shields.io/badge/python-3.9%2B-blue) ![License MIT](https://img.shields.io/badge/license-MIT-green) ![MCP Compatible](https://img.shields.io/badge/MCP-Compatible-purple) ![GenPark AI](https://img.shields.io/badge/GenPark-AI--Agent--Skill-orange)

> **GenPark AI Agent Skill** -- AI SDR agent that de-anonymizes visitors, scores fit & triggers outreach sequences (Clara AI style)

## Quick Start
```python
python example_usage.py
```

## 📊 Agentic Architecture Flowchart
```mermaid
graph LR
  User([User / AI Agent]) -->|JSON Request| Skill[GenPark AI Skill]
  Skill -->|Execution Logic| CoreEngine[Core Processing Engine]
  CoreEngine -->|Structured Output| User
```

## 🔌 MCP (Model Context Protocol) Integration
```bash
python mcp_server.py
```
