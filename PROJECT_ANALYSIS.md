# GHOSTCREW Pentest Agent - Comprehensive Project Analysis

## Executive Summary

The GHOSTCREW Pentest Agent is a sophisticated AI-powered penetration testing framework that orchestrates 25+ security tools through the Model Context Protocol (MCP). It combines strategic AI planning with automated workflow execution, knowledge base integration, and comprehensive reporting capabilities.

**Version:** 0.1.0
**Platform:** Linux (6.14.0-1017-gcp)
**Primary Language:** Python 3.x
**AI Model:** Google Gemini 1.5 Flash
**Architecture:** Async-based, MCP-integrated, Phase-driven

---

## Table of Contents

1. [Project Architecture](#project-architecture)
2. [Core Components](#core-components)
3. [MCP Integration](#mcp-integration)
4. [Tool Ecosystem](#tool-ecosystem)
5. [Workflow System](#workflow-system)
6. [Knowledge Base](#knowledge-base)
7. [Security Considerations](#security-considerations)
8. [Performance Analysis](#performance-analysis)
9. [Deployment Models](#deployment-models)
10. [Future Enhancements](#future-enhancements)

---

## Project Architecture

### High-Level Architecture

```
┌───────────────────────────────────────────────────────────────────┐
│                    GHOSTCREW Pentest Agent                         │
│                         (Main Application)                         │
└───────────────────────────────────────────────────────────────────┘
                              │
                              ├─ main.py (Entry Point)
                              │
    ┌─────────────────────────┼─────────────────────────┐
    │                         │                         │
    ▼                         ▼                         ▼
┌─────────┐            ┌──────────┐             ┌────────────┐
│  Core   │            │ Workflows│             │     UI     │
│ Module  │            │  Module  │             │   Module   │
└─────────┘            └──────────┘             └────────────┘
    │                         │                         │
    ├─ pentest_agent.py      ├─ workflow_engine.py     ├─ menu_system.py
    ├─ tool_manager.py        ├─ workflow_definitions.py├─ conversation_manager.py
    ├─ planner.py             └─ workflow_runner.py     └─
    ├─ reporter.py
    └─ knowledge_base.py
                              │
    ┌─────────────────────────┼─────────────────────────┐
    │                         │                         │
    ▼                         ▼                         ▼
┌─────────┐            ┌──────────┐             ┌────────────┐
│  RAG    │            │  Config  │             │ Reporting  │
│ Module  │            │  Module  │             │   Module   │
└─────────┘            └──────────┘             └────────────┘
    │                         │                         │
    └─ knowledge_base.py      ├─ app_config.py          └─ generators.py
                              └─ constants.py
                              │
    ┌─────────────────────────┴─────────────────────────┐
    │                  MCP Integration Layer              │
    │                    (stdio transport)                │
    └───────────────────────────────────────────────────┘
                              │
         ┌───────────────────┼───────────────────┐
         │                   │                   │
         ▼                   ▼                   ▼
    ┌────────┐          ┌────────┐          ┌────────┐
    │Network │          │  Web   │          │ Exploit│
    │ Tools  │          │ Tools  │          │ Tools  │
    └────────┘          └────────┘          └────────┘
    • nmap              • nuclei            • sqlmap
    • masscan           • httpx             • hydra
    • amass             • gobuster          • metasploit
    • etc.              • ffuf              • etc.
                        • burpsuite
```

### Technology Stack

| Layer | Technologies |
|-------|-------------|
| **AI/ML** | Google Gemini 1.5 Flash, LangChain, Ollama |
| **Backend** | Python 3.x, asyncio, FastAPI, uvicorn |
| **Integration** | MCP 1.6.0, stdio transport |
| **Storage** | JSON (structured), Text files (knowledge base) |
| **Security Tools** | 25+ tools (nmap, nuclei, sqlmap, etc.) |
| **UI** | CLI with colorama, interactive menus |

---

## Core Components

### 1. PentestAgent (core/pentest_agent.py)

**Purpose:** Central orchestrator for penetration testing operations

**Key Features:**
- Phase-based execution (reconnaissance → reporting)
- Interactive and automated modes
- Tool manager integration
- Knowledge base utilization
- Comprehensive reporting

**Execution Phases:**
1. **Reconnaissance** - Information gathering
2. **Enumeration** - Service and application discovery
3. **Vulnerability Assessment** - Security flaw identification
4. **Exploitation** - Vulnerability exploitation
5. **Post-Exploitation** - Privilege escalation, persistence
6. **Reporting** - Findings documentation

**Code Highlights:**
```python
async def run_pentest(self, goal: str, target: str):
    for phase in self.planner.phases:
        plan = self.planner.create_plan_for_current_phase(target)
        await self.execute_plan(plan)
        self.planner.advance_to_next_phase()

    report_path = self.reporter.generate_report(engagement_summary)
```

### 2. ToolManager (core/tool_manager.py)

**Purpose:** Unified interface for security tool execution

**Capabilities:**
- Tool discovery and validation
- Command construction and execution
- Async process management
- Result aggregation and storage
- Timeout handling

**Tool Definition Structure:**
```python
{
    "nmap": {
        "path": "/usr/bin/nmap",
        "requires_sudo": True,
        "phases": ["reconnaissance", "enumeration"],
        "commands": {
            "port_scan": ["-sS", "-sV", "-O", "-A", "-p-"]
        }
    }
}
```

**Execution Flow:**
1. Validate tool availability
2. Construct command with arguments
3. Execute async subprocess
4. Capture stdout/stderr
5. Store results in JSON
6. Return execution record

### 3. Planner (core/planner.py)

**Purpose:** Strategic planning and phase management

**Responsibilities:**
- Phase progression control
- Tool selection for phases
- Dynamic plan creation
- Knowledge base integration

**Planning Strategy:**
```python
def create_plan_for_current_phase(self, target: str):
    tools_for_phase = tool_manager.get_tools_for_phase(current_phase)
    plan = []
    for tool in tools_for_phase:
        for command_type in tool.commands:
            plan.append({
                "tool": tool_name,
                "command_type": command_type,
                "target": target
            })
    return plan
```

### 4. Reporter (core/reporter.py)

**Purpose:** Findings collection and report generation

**Features:**
- Phase-based finding organization
- JSON structured reports
- Timestamp tracking
- Result aggregation

**Report Structure:**
```json
{
  "engagement_summary": {
    "goal": "...",
    "target": "...",
    "start_time": 123456789
  },
  "phases": {
    "reconnaissance": [...],
    "enumeration": [...],
    "vulnerability_assessment": [...]
  }
}
```

### 5. WorkflowEngine (workflows/workflow_engine.py)

**Purpose:** Automated workflow execution

**Capabilities:**
- Direct command execution
- Result analysis
- Target normalization (URL vs hostname)
- Workflow logging
- Progress tracking

**Workflow Execution:**
```python
async def run_automated_workflow(self, workflow, target):
    for step in workflow['steps']:
        command = step['command'].format(target=target)
        normalized = self._normalize_command_for_target(command, target)
        result = await self._execute_command(normalized)
        self.tool_results.append(result)
```

### 6. KnowledgeBase (rag/knowledge_base.py)

**Purpose:** Security knowledge storage and retrieval

**Features:**
- Text-based search (no embeddings)
- Multi-format support (JSON, TXT, etc.)
- Chunking and indexing
- Relevance scoring
- Metadata tracking

**Search Algorithm:**
- Exact phrase matching (highest score)
- Individual word matching
- Proximity scoring
- Sentence-level relevance

---

## MCP Integration

### Configuration Structure

The project uses `mcp.json` for MCP server configuration with the following structure:

```json
{
  "servers": [
    {
      "name": "tool-name",
      "params": {
        "command": "/path/to/tool",
        "args": ["stdio"],
        "env": {
          "PATH": "..."
        }
      },
      "cache_tools_list": true
    }
  ]
}
```

### MCP Transport

**Transport Type:** stdio (Standard Input/Output)

**Advantages:**
- Simple integration
- No network overhead
- Direct process communication
- Secure by default

**Communication Flow:**
```
Client → MCP Server → Tool Process → stdout/stderr → MCP Server → Client
```

### Configured MCP Servers

| Category | Tools | Count |
|----------|-------|-------|
| Network Scanning | nmap, masscan, amass, assetfinder, etc. | 6 |
| Web Application | nuclei, httpx, gobuster, ffuf, etc. | 9 |
| Exploitation | sqlmap, hydra, metasploit, etc. | 5 |
| Network Exploitation | crackmapexec, responder, bettercap | 3 |
| Active Directory | bloodhound | 1 |
| SSL/TLS | sslscan, nikto | 2 |
| Cloud Security | scout-suite | 1 |
| **Total** | | **27** |

---

## Tool Ecosystem

### Tool Categories and Paths

#### 1. Network Scanning Tools

| Tool | Path | Description | Sudo Required |
|------|------|-------------|---------------|
| nmap | `/usr/bin/nmap` | Network mapper and port scanner | Yes |
| masscan | `/usr/bin/masscan` | High-speed port scanner | Yes |
| amass | `/snap/bin/amass` | In-depth subdomain enumeration | No |
| assetfinder | `~/go/bin/assetfinder` | Find domains and subdomains | No |
| waybackurls | `~/go/bin/waybackurls` | Fetch URLs from archives | No |
| shuffledns | `~/go/bin/shuffledns` | DNS resolution with bruteforce | No |

#### 2. Web Application Tools

| Tool | Path | Description | Sudo Required |
|------|------|-------------|---------------|
| nuclei | `~/go/bin/nuclei` | Vulnerability scanner with templates | No |
| httpx | `~/.local/bin/httpx` | Fast HTTP probe | No |
| gobuster | `/usr/bin/gobuster` | Directory/DNS brute-forcer | No |
| ffuf | `/usr/bin/ffuf` | Fast web fuzzer | No |
| katana | `~/go/bin/katana` | Fast crawler | No |
| arjun | `~/.local/bin/arjun` | HTTP parameter discovery | No |
| alterx | `~/go/bin/alterx` | Subdomain wordlist generator | No |
| burpsuite | Java JAR | Web security platform (headless) | No |

#### 3. Exploitation Tools

| Tool | Path | Description | Sudo Required |
|------|------|-------------|---------------|
| sqlmap | `~/.local/bin/sqlmap` | SQL injection tool | No |
| hydra | `/usr/bin/hydra` | Password brute-forcer | No |
| metasploit | `/usr/local/bin/msfconsole` | Exploitation framework | No |
| john | `/usr/sbin/john` | Password cracker | No |
| hashcat | `/usr/bin/hashcat` | Advanced password recovery | No |

#### 4. Network Exploitation Tools

| Tool | Path | Description | Sudo Required |
|------|------|-------------|---------------|
| crackmapexec | `~/.local/bin/crackmapexec` | Network pentesting | No |
| responder | `~/.local/bin/responder` | LLMNR/NBT-NS poisoner | Yes |
| bettercap | `/usr/bin/bettercap` | Network attack framework | Yes |

#### 5. Specialized Tools

| Tool | Path | Description | Sudo Required |
|------|------|-------------|---------------|
| bloodhound | `/usr/local/bin/bloodhound-python` | AD enumeration | No |
| sslscan | `/usr/bin/sslscan` | SSL/TLS scanner | No |
| scout-suite | `~/.local/bin/scout` | Multi-cloud auditing | No |

### Tool Execution Patterns

1. **Subprocess-based** - Direct command execution via asyncio
2. **MCP stdio** - Communication through MCP protocol
3. **Headless mode** - Tools like BurpSuite run without GUI
4. **Privileged execution** - sudo wrapper for tools requiring elevation

---

## Workflow System

### Available Workflows

#### 1. Reconnaissance Workflow

**Steps:** 5
**Duration:** ~5-10 minutes
**Tools:** nmap, assetfinder, waybackurls

**Sequence:**
1. Comprehensive reconnaissance (nmap vuln scan)
2. Subdomain discovery (assetfinder)
3. Port scanning (nmap top 1000)
4. Technology fingerprinting (nmap scripts)
5. Historical data gathering (waybackurls)

#### 2. Web Application Workflow

**Steps:** 6
**Duration:** ~15-20 minutes
**Tools:** gobuster, sqlmap, nuclei, sslscan

**Sequence:**
1. Directory discovery (gobuster)
2. SQL injection testing (sqlmap)
3. Vulnerability scanning (nuclei CVEs)
4. SSL/TLS analysis (sslscan)
5. Authentication testing (nuclei auth templates)
6. File vulnerability testing (nuclei file templates)

#### 3. Network Infrastructure Workflow

**Steps:** 6
**Duration:** ~10-15 minutes
**Tools:** nmap, nuclei

**Sequence:**
1. Network range scanning (nmap ping scan)
2. Service enumeration (nmap full port scan)
3. Vulnerability scanning (nuclei)
4. Misconfiguration testing (nmap scripts)
5. Exploitation attempts (nuclei)
6. Segmentation assessment (nmap)

#### 4. Full Penetration Test Workflow

**Steps:** 7
**Duration:** ~30-45 minutes
**Tools:** nmap, gobuster, nuclei

**Sequence:**
1. Phase 1: Quick port scan
2. Phase 2: Service version detection
3. Phase 3: Web service discovery
4. Phase 4: Focused vulnerability scanning
5. Phase 5: Targeted exploitation
6. Phase 6: Post-exploitation enumeration
7. Phase 7: Report compilation

#### 5. Quick Scan Workflow

**Steps:** 4
**Duration:** ~5 minutes
**Tools:** nmap, gobuster, sslscan, nuclei

**Sequence:**
1. Quick port scan (top 1000)
2. Basic directory enumeration
3. SSL/TLS check
4. Common vulnerability scan

#### 6. Comprehensive Scan Workflow

**Steps:** 10
**Duration:** ~45-60 minutes
**Tools:** All categories

**Sequence:**
1. Network discovery
2. Service enumeration
3. Web application testing
4. Vulnerability scanning
5. SSL/TLS analysis
6. Directory enumeration
7. SQL injection testing
8. Authentication testing
9. Exploitation attempts
10. Report generation

### Workflow Execution Engine

**Features:**
- Async execution
- Result tracking
- Error handling
- Progress logging
- Target normalization
- Output analysis

**Result Storage:**
```
Results/
├── workflows/
│   └── workflow_log.json
├── scans/
│   └── tool_command_timestamp.json
├── vulnerabilities/
│   └── nuclei_scan_timestamp.json
└── reports/
    └── pentest_report_timestamp.json
```

---

## Knowledge Base

### Structure

```
knowledge/
├── exploits/           # Exploit codes and PoCs
│   ├── web/
│   ├── network/
│   ├── windows/
│   ├── linux/
│   ├── macos/
│   └── mobile/
├── shellcodes/         # Shellcode payloads
│   ├── x86/
│   ├── x64/
│   ├── arm/
│   └── mips/
├── wordlists/          # Custom wordlists
│   ├── dns.txt
│   ├── directories.txt
│   ├── passwords.txt
│   └── usernames.txt
├── tools/              # Tool documentation
└── other/              # Miscellaneous resources
```

### Search Capabilities

**Algorithm:**
1. **Exact phrase matching** - Score: +10.0
2. **Word matching** - Score: +1.5 per word
3. **Proximity bonus** - Score: +3.0 if words within 100 chars
4. **Sentence relevance** - Score: +0.5 per matching sentence

**Example Query:**
```python
kb = Kb("/home/MrFkry/PentestAgent/knowledge/exploits")
results = kb.search("SQL injection vulnerability", max_results=5)

# Returns:
# [
#   {
#     "content": "...",
#     "score": 15.5,
#     "metadata": {"filename": "sql_injection.txt", ...}
#   },
#   ...
# ]
```

### Integration Points

1. **Planner** - Enriches tool selection with KB data
2. **Workflows** - References exploits and techniques
3. **Reporter** - Includes relevant documentation
4. **UI** - Provides context-aware suggestions

---

## Security Considerations

### Authentication & Authorization

**Current State:** Local execution, no auth required

**Recommendations for Production:**
1. Implement API key authentication
2. Use JWT tokens for session management
3. Role-based access control (RBAC)
4. GitHub token for MCP integration

### Tool Execution Safety

**Implemented:**
- Timeout mechanisms (default 300s)
- Sudo requirement flags
- Command validation
- Process isolation

**Recommendations:**
1. Sandboxed execution environments
2. Resource limits (CPU, memory)
3. Network isolation options
4. Audit logging

### Data Protection

**Current:**
- Results stored in local JSON files
- No encryption at rest
- Basic file permissions

**Recommendations:**
1. Encrypt sensitive results
2. Secure credential storage
3. PII redaction in reports
4. Retention policies

### Network Security

**Current:**
- Direct tool execution
- No proxy by default
- BurpSuite proxy available

**Recommendations:**
1. VPN/tunnel support
2. Traffic encryption
3. Rate limiting
4. IP whitelisting

---

## Performance Analysis

### Execution Times (Approximate)

| Workflow | Duration | Tools Used | Parallel Execution |
|----------|----------|------------|-------------------|
| Quick Scan | 5 min | 4 | Partial |
| Reconnaissance | 10 min | 5 | Yes |
| Web Application | 20 min | 6 | Partial |
| Network Infrastructure | 15 min | 6 | Partial |
| Full Pentest | 45 min | 10+ | Partial |
| Comprehensive | 60 min | All | Partial |

### Resource Usage

**Memory:**
- Base agent: ~100 MB
- Per tool: 50-500 MB
- BurpSuite: 2-4 GB
- Total peak: ~5 GB

**CPU:**
- Agent: Low (< 10%)
- Tools: Varies (10-100% per tool)
- Concurrent tools: Limited by system

**Disk:**
- Results: ~10-100 MB per engagement
- Knowledge base: ~500 MB
- Logs: ~50 MB per session

### Optimization Opportunities

1. **Parallel Execution** - Run independent tools concurrently
2. **Result Caching** - Avoid redundant scans
3. **Incremental Scanning** - Resume interrupted workflows
4. **Smart Scheduling** - Prioritize critical tools

---

## Deployment Models

### 1. Local Execution (Current)

**Pros:**
- Full control
- No network latency
- Direct tool access

**Cons:**
- Single machine limitations
- No scalability
- Manual setup

### 2. Docker Container

**Pros:**
- Portable
- Consistent environment
- Easy distribution

**Cons:**
- Requires privileged mode for some tools
- Volume mounts for results
- Network configuration

**Example Dockerfile:**
```dockerfile
FROM python:3.11-slim

RUN apt-get update && apt-get install -y \
    nmap masscan gobuster sqlmap hydra nikto \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000
CMD ["python", "main.py"]
```

### 3. Kubernetes Deployment

**Pros:**
- Scalable
- High availability
- Resource management

**Cons:**
- Complex setup
- Networking challenges
- Tool compatibility

**Components:**
- Deployment: Agent pods
- Services: API exposure
- PersistentVolumes: Results storage
- ConfigMaps: Tool configurations

### 4. GitHub MCP Server

**Pros:**
- Centralized management
- Version control
- CI/CD integration

**Cons:**
- GitHub dependency
- Network requirement
- Token management

**Setup:**
1. Publish container to GHCR
2. Configure MCP server in `mcp.json`
3. Set environment variables
4. Deploy to GitHub infrastructure

---

## Future Enhancements

### Planned Features

1. **Advanced AI Integration**
   - Multi-model support (GPT-4, Claude, etc.)
   - Reasoning chains for complex scenarios
   - Automated decision trees

2. **Enhanced Workflows**
   - Visual workflow builder
   - Custom workflow creation UI
   - Workflow sharing/marketplace

3. **Improved Reporting**
   - PDF generation
   - HTML interactive reports
   - CVSS scoring integration
   - Executive summaries

4. **Tool Expansion**
   - Additional 50+ tools
   - Custom tool plugins
   - Tool recommendation engine

5. **Collaboration Features**
   - Team workspaces
   - Real-time collaboration
   - Shared knowledge bases

6. **Compliance & Standards**
   - OWASP Top 10 mapping
   - MITRE ATT&CK integration
   - NIST framework alignment
   - PCI DSS, HIPAA reporting

7. **API Enhancements**
   - GraphQL support
   - WebSocket for real-time updates
   - Batch operations
   - Webhook integrations

8. **Security Improvements**
   - Zero-trust architecture
   - Hardware security module (HSM) support
   - Advanced audit logging
   - Compliance reporting

---

## Conclusion

The GHOSTCREW Pentest Agent represents a sophisticated integration of AI-powered planning with traditional penetration testing tools. Its modular architecture, comprehensive MCP integration, and extensive tool support make it a powerful platform for security assessment automation.

**Key Strengths:**
- ✓ Comprehensive tool integration (25+ tools)
- ✓ AI-powered strategic planning
- ✓ Flexible workflow system
- ✓ Knowledge base integration
- ✓ Professional reporting

**Areas for Improvement:**
- Authentication and authorization
- Scalability and distributed execution
- Advanced reporting formats
- Tool result correlation
- Real-time collaboration

**Recommended Next Steps:**
1. Implement API authentication
2. Create Docker deployment
3. Publish to GitHub Container Registry
4. Develop comprehensive test suite
5. Enhance documentation

---

**Last Updated:** 2025-10-20
**Version:** 0.1.0
**Analyzed By:** AI Assistant
**Contact:** MrFkry / GHOSTCREW Team
