# GHOSTCREW Pentest Agent - Documentation Index

**📦 Complete MCP Conversion Package**

Generated: 2025-10-20 | Version: 0.1.0 | Total Lines: 5,855+

---

## 📖 Quick Navigation

| Document | Description | Lines | Priority |
|----------|-------------|-------|----------|
| **[README.md](README.md)** | Main documentation & getting started guide | ~800 | ⭐⭐⭐⭐⭐ |
| **[SUMMARY.md](SUMMARY.md)** | Executive summary of deliverables | ~650 | ⭐⭐⭐⭐⭐ |
| **[PROJECT_ANALYSIS.md](PROJECT_ANALYSIS.md)** | Comprehensive technical analysis | ~1,300 | ⭐⭐⭐⭐ |
| **[TOOL_INVENTORY.json](TOOL_INVENTORY.json)** | Complete tool catalog with paths | ~450 | ⭐⭐⭐⭐⭐ |

---

## 🔌 API Specifications

| Specification | Format | Use Case | Lines |
|---------------|--------|----------|-------|
| **[pentest-agent-openapi-3.1.json](pentest-agent-openapi-3.1.json)** | JSON | API development, automation | ~1,050 |
| **[pentest-agent-swagger.yaml](pentest-agent-swagger.yaml)** | YAML | Documentation, Swagger UI | ~900 |

### API Endpoints Overview

**Total Endpoints:** 13

1. **Pentest Operations** (2 endpoints)
   - `POST /pentest/run` - Execute penetration test
   - `POST /pentest/interactive` - Interactive mode

2. **Workflows** (2 endpoints)
   - `GET /workflows` - List available workflows
   - `POST /workflows/{workflowId}/execute` - Execute workflow

3. **Tools** (2 endpoints)
   - `GET /tools` - List security tools
   - `POST /tools/{toolName}/execute` - Execute tool

4. **Knowledge Base** (2 endpoints)
   - `POST /knowledge-base/search` - Search KB
   - `GET /knowledge-base/exploits` - List exploits

5. **Reports** (2 endpoints)
   - `POST /reports/generate` - Generate report
   - `GET /reports/{reportId}` - Retrieve report

6. **MCP Integration** (2 endpoints)
   - `GET /mcp/servers` - List MCP servers
   - `GET /mcp/servers/{serverName}/tools` - List tools

7. **BurpSuite** (3 endpoints)
   - `POST /burpsuite/start` - Start headless
   - `POST /burpsuite/scan` - Execute scan
   - `POST /burpsuite/stop` - Stop instance

---

## 🛠️ Integration Guides

### MCP Server Configuration

**Location:** `mcp-server/`

| File | Description | Lines |
|------|-------------|-------|
| **[mcp-server-config.json](mcp-server/mcp-server-config.json)** | GitHub MCP server configuration | ~650 |

**Servers Configured:** 26 tool servers + 3 core servers

**Key Features:**
- ✅ All 27 security tools configured
- ✅ stdio transport for all servers
- ✅ Environment variables defined
- ✅ Container runtime arguments
- ✅ GitHub Container Registry integration

### BurpSuite Integration

**Location:** `burpsuite/`

| File | Description | Lines |
|------|-------------|-------|
| **[BURPSUITE_INTEGRATION.md](burpsuite/BURPSUITE_INTEGRATION.md)** | Complete integration guide | ~850 |
| **[config.json](burpsuite/config.json)** | BurpSuite configuration | ~65 |

**Topics Covered:**
- Installation and setup
- Headless mode configuration
- Command-line arguments
- Proxy configuration
- Certificate management
- Integration patterns
- Troubleshooting

---

## ⚙️ Configuration Files

**Location:** `configs/`

| File | Environment | Lines |
|------|-------------|-------|
| **[production.env.example](configs/production.env.example)** | Production | ~160 |
| **[development.env.example](configs/development.env.example)** | Development | ~80 |

**Configuration Categories:**
- AI Model (Gemini API)
- GitHub Integration
- Application Paths
- MCP Server Settings
- Security & Authentication
- Tool Configuration
- BurpSuite Settings
- Logging & Monitoring
- Performance Tuning
- Feature Flags
- Network Configuration
- Advanced Settings

---

## 📊 Project Statistics

### Documentation Metrics

| Metric | Value |
|--------|-------|
| **Total Files** | 10 files |
| **Total Lines** | 5,855+ lines |
| **Markdown Files** | 5 files |
| **JSON Files** | 4 files |
| **YAML Files** | 1 file |
| **API Endpoints** | 13 endpoints |
| **Tools Documented** | 27 tools |
| **Workflows Defined** | 6 workflows |
| **MCP Servers** | 29 servers |

### Tools by Category

| Category | Count | Tools |
|----------|-------|-------|
| **Network Scanning** | 6 | nmap, masscan, amass, assetfinder, waybackurls, shuffledns |
| **Web Application** | 9 | nuclei, httpx, gobuster, ffuf, katana, arjun, alterx, burpsuite, nikto |
| **Exploitation** | 5 | sqlmap, hydra, metasploit, john, hashcat |
| **Network Exploitation** | 3 | crackmapexec, responder, bettercap |
| **Active Directory** | 1 | bloodhound |
| **SSL/TLS** | 2 | sslscan, nikto |
| **Cloud Security** | 1 | scout-suite |
| **Total** | **27** | |

### Workflows Coverage

| Workflow | Steps | Duration | Tools |
|----------|-------|----------|-------|
| reconnaissance | 5 | ~10 min | nmap, assetfinder, waybackurls |
| web_application | 6 | ~20 min | gobuster, sqlmap, nuclei, sslscan |
| network_infrastructure | 6 | ~15 min | nmap, nuclei |
| full_penetration_test | 7 | ~45 min | nmap, gobuster, nuclei |
| quick_scan | 4 | ~5 min | nmap, gobuster, sslscan, nuclei |
| comprehensive_scan | 10 | ~60 min | All categories |

---

## 🎯 Reading Guide

### For First-Time Users

**Start Here:**
1. **[SUMMARY.md](SUMMARY.md)** - Get overview of deliverables
2. **[README.md](README.md)** - Understand how to use documentation
3. **[TOOL_INVENTORY.json](TOOL_INVENTORY.json)** - Review available tools

### For API Developers

**Recommended Path:**
1. **[pentest-agent-openapi-3.1.json](pentest-agent-openapi-3.1.json)** - API specification
2. **[README.md](README.md)** - Integration examples
3. **[configs/](configs/)** - Environment setup

### For System Administrators

**Recommended Path:**
1. **[PROJECT_ANALYSIS.md](PROJECT_ANALYSIS.md)** - Architecture understanding
2. **[configs/production.env.example](configs/production.env.example)** - Production setup
3. **[mcp-server/mcp-server-config.json](mcp-server/mcp-server-config.json)** - MCP deployment

### For Security Practitioners

**Recommended Path:**
1. **[TOOL_INVENTORY.json](TOOL_INVENTORY.json)** - Available tools
2. **[README.md](README.md)** - Workflow examples
3. **[BURPSUITE_INTEGRATION.md](burpsuite/BURPSUITE_INTEGRATION.md)** - Advanced scanning

---

## 🚀 Quick Start Paths

### Path 1: API Development

```bash
# Import OpenAPI spec
curl -o pentest-agent-api.json \
  https://raw.githubusercontent.com/MrFkry/PentestAgent/main/draft/pentest-agent-openapi-3.1.json

# Generate Python client
npx @openapitools/openapi-generator-cli generate \
  -i pentest-agent-api.json \
  -g python \
  -o ./client

# Use client
python -c "from client import *; print('API Client Ready!')"
```

### Path 2: MCP Server Setup

```bash
# Copy MCP config
cp draft/mcp-server/mcp-server-config.json ~/mcp.json

# Set environment
export GEMINI_API_KEY="your-key"
export GITHUB_TOKEN="ghp_your-token"

# Test connection
mcp connect pentest-agent
```

### Path 3: Local Testing

```bash
# Setup environment
cp draft/configs/development.env.example .env
nano .env  # Edit with your values

# Install dependencies
pip install -r requirements.txt

# Run locally
python main.py --goal "Test scan" --target "scanme.nmap.org"
```

### Path 4: Docker Deployment

```bash
# Build image
docker build -t pentest-agent:latest .

# Run container
docker run --env-file .env -p 8000:8000 pentest-agent:latest

# Test API
curl http://localhost:8000/tools
```

---

## 📁 File Tree

```
draft/
├── INDEX.md                              # This file
├── README.md                             # Main guide
├── SUMMARY.md                            # Executive summary
├── PROJECT_ANALYSIS.md                   # Technical analysis
├── TOOL_INVENTORY.json                   # Tool catalog
├── pentest-agent-openapi-3.1.json       # OpenAPI spec
├── pentest-agent-swagger.yaml           # Swagger YAML
│
├── mcp-server/
│   └── mcp-server-config.json           # MCP configuration
│
├── burpsuite/
│   ├── BURPSUITE_INTEGRATION.md         # Integration guide
│   └── config.json                       # BurpSuite config
│
├── configs/
│   ├── production.env.example           # Production env
│   └── development.env.example          # Development env
│
└── docs/                                 # Future docs
```

---

## 🔗 Related Files (Outside Draft)

| Location | Description |
|----------|-------------|
| `/home/MrFkry/PentestAgent/core/` | Core modules |
| `/home/MrFkry/PentestAgent/workflows/` | Workflow engine |
| `/home/MrFkry/PentestAgent/rag/` | Knowledge base |
| `/home/MrFkry/PentestAgent/knowledge/` | KB content |
| `/home/MrFkry/PentestAgent/Results/` | Output directory |
| `/home/MrFkry/PentestAgent/mcp.json` | Active MCP config |

---

## ✅ Documentation Completeness

### Covered Topics

- ✅ API Specifications (OpenAPI 3.1 + Swagger)
- ✅ Tool Inventory (27 tools with paths)
- ✅ MCP Server Configuration (29 servers)
- ✅ BurpSuite Integration (Complete guide)
- ✅ Environment Configuration (Prod + Dev)
- ✅ Workflow Definitions (6 workflows)
- ✅ Architecture Analysis (Comprehensive)
- ✅ Deployment Models (4 models)
- ✅ Security Considerations (Full section)
- ✅ Performance Analysis (Benchmarks)

### Future Additions

- ⏳ API Reference (auto-generated from OpenAPI)
- ⏳ Workflow Guide (detailed usage)
- ⏳ Knowledge Base Documentation
- ⏳ Deployment Guide (step-by-step)
- ⏳ Troubleshooting Guide
- ⏳ Contributing Guide
- ⏳ Security Best Practices
- ⏳ Performance Tuning Guide

---

## 📞 Support & Resources

### Documentation

- **Project Repository:** https://github.com/MrFkry/PentestAgent
- **Issues:** https://github.com/MrFkry/PentestAgent/issues
- **Discussions:** https://github.com/MrFkry/PentestAgent/discussions

### External Resources

- **OpenAPI Spec:** https://spec.openapis.org/oas/v3.1.0
- **MCP Documentation:** https://modelcontextprotocol.io
- **BurpSuite Docs:** https://portswigger.net/burp/documentation
- **Gemini API:** https://ai.google.dev/docs
- **GitHub Container Registry:** https://docs.github.com/packages

### Community

- **Author:** MrFkry
- **Team:** GHOSTCREW
- **License:** MIT
- **Version:** 0.1.0

---

## 🎓 Learning Resources

### For Beginners

1. Read **[SUMMARY.md](SUMMARY.md)** for overview
2. Review **[TOOL_INVENTORY.json](TOOL_INVENTORY.json)** for available tools
3. Explore **[README.md](README.md)** for usage examples

### For Intermediate Users

1. Study **[PROJECT_ANALYSIS.md](PROJECT_ANALYSIS.md)** for architecture
2. Review **[pentest-agent-openapi-3.1.json](pentest-agent-openapi-3.1.json)** for API
3. Configure **[mcp-server-config.json](mcp-server/mcp-server-config.json)** for MCP

### For Advanced Users

1. Analyze core modules in `/core`
2. Customize workflows in `/workflows`
3. Extend knowledge base in `/knowledge`
4. Contribute to project on GitHub

---

## 📊 Version History

| Version | Date | Changes |
|---------|------|---------|
| 0.1.0 | 2025-10-20 | Initial draft documentation package |

---

## 🏆 Acknowledgments

- **OpenAPI Initiative** - For API specification standards
- **MCP Community** - For Model Context Protocol
- **PortSwigger** - For BurpSuite
- **Google** - For Gemini API
- **Security Tool Authors** - For amazing tools

---

**📚 Total Documentation: 5,855+ lines across 10 files**

**🎯 Ready for: API Development | MCP Deployment | Production Use**

---

*Generated with ❤️ by AI Assistant*
*For GHOSTCREW Pentest Agent Project*
*Version 0.1.0 | 2025-10-20*
