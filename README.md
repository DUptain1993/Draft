# GHOSTCREW Pentest Agent - Draft Documentation

This directory contains comprehensive API specifications and documentation for converting the GHOSTCREW Pentest Agent into a separate MCP (Model Context Protocol) project.

## Directory Structure

```
draft/
├── README.md                           # This file
├── pentest-agent-openapi-3.1.json     # OpenAPI 3.1 specification
├── pentest-agent-swagger.yaml         # Swagger/OpenAPI YAML format
├── TOOL_INVENTORY.json                # Complete tool inventory with paths
├── PROJECT_ANALYSIS.md                # Detailed project analysis
├── mcp-server/
│   ├── mcp-server-config.json         # GitHub MCP server configuration
│   ├── DEPLOYMENT.md                  # Deployment instructions
│   └── DOCKER_SETUP.md                # Docker containerization guide
├── burpsuite/
│   ├── BURPSUITE_INTEGRATION.md       # BurpSuite headless integration
│   ├── config.json                    # Sample BurpSuite configuration
│   └── burpsuite_wrapper.py           # Python wrapper for BurpSuite
├── docs/
│   ├── API_REFERENCE.md               # Complete API reference
│   ├── WORKFLOWS_GUIDE.md             # Workflow usage guide
│   └── KNOWLEDGE_BASE.md              # Knowledge base documentation
└── configs/
    ├── production.env.example         # Production environment template
    └── development.env.example        # Development environment template
```

## Overview

### What's Included

1. **OpenAPI 3.1 Specification** (`pentest-agent-openapi-3.1.json`)
   - Complete API endpoint definitions
   - Request/response schemas
   - Authentication mechanisms
   - Error handling specifications

2. **Swagger YAML** (`pentest-agent-swagger.yaml`)
   - Human-readable YAML format
   - Compatible with Swagger UI
   - Same comprehensive coverage as JSON spec

3. **Tool Inventory** (`TOOL_INVENTORY.json`)
   - All 25+ security tools cataloged
   - System paths documented
   - Command structures defined
   - MCP integration status

4. **BurpSuite Integration** (`burpsuite/BURPSUITE_INTEGRATION.md`)
   - Headless mode configuration
   - Command-line arguments
   - Proxy setup instructions
   - Integration patterns

5. **MCP Server Configuration** (`mcp-server/mcp-server-config.json`)
   - GitHub MCP server setup
   - All tool servers configured
   - Environment variables defined
   - Capability declarations

## Project Components

### Core Architecture

```
┌─────────────────────────────────────────────────────────┐
│                   GHOSTCREW Pentest Agent                │
├─────────────────────────────────────────────────────────┤
│                                                           │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐  │
│  │   Core       │  │  Workflow    │  │  Knowledge   │  │
│  │   Agent      │  │  Engine      │  │  Base        │  │
│  └──────────────┘  └──────────────┘  └──────────────┘  │
│                                                           │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐  │
│  │   Tool       │  │  Planner     │  │  Reporter    │  │
│  │   Manager    │  │              │  │              │  │
│  └──────────────┘  └──────────────┘  └──────────────┘  │
│                                                           │
├─────────────────────────────────────────────────────────┤
│                    MCP Integration Layer                  │
├─────────────────────────────────────────────────────────┤
│                                                           │
│  Security Tools (25+ tools via MCP stdio)                │
│  • nmap • nuclei • sqlmap • gobuster • ffuf              │
│  • httpx • masscan • hydra • metasploit • bloodhound     │
│  • crackmapexec • responder • bettercap • burpsuite      │
│  • and many more...                                       │
│                                                           │
└─────────────────────────────────────────────────────────┘
```

### Key Features

1. **AI-Powered Planning**
   - Gemini 1.5 Flash model integration
   - Dynamic phase-based execution
   - Strategic tool selection

2. **Automated Workflows**
   - 6 predefined workflows
   - Reconnaissance to exploitation
   - Customizable execution

3. **Knowledge Base (RAG)**
   - Exploit database
   - Shellcode library
   - Wordlist collection
   - Text-based search

4. **Comprehensive Tooling**
   - 25+ security tools
   - MCP stdio integration
   - Async execution
   - Result aggregation

5. **Professional Reporting**
   - JSON structured reports
   - Phase-based findings
   - Severity classification
   - Markdown export

## API Endpoints

### Core Endpoints

#### Pentest Execution
- `POST /pentest/run` - Execute full penetration test
- `POST /pentest/interactive` - Interactive mode with confirmations

#### Workflows
- `GET /workflows` - List available workflows
- `POST /workflows/{workflowId}/execute` - Execute specific workflow

#### Tools
- `GET /tools` - List available security tools
- `POST /tools/{toolName}/execute` - Execute specific tool

#### Knowledge Base
- `POST /knowledge-base/search` - Search security knowledge
- `GET /knowledge-base/exploits` - List exploit database

#### Reports
- `POST /reports/generate` - Generate pentest report
- `GET /reports/{reportId}` - Retrieve specific report

#### MCP Integration
- `GET /mcp/servers` - List MCP servers
- `GET /mcp/servers/{serverName}/tools` - List server tools

#### BurpSuite
- `POST /burpsuite/start` - Start BurpSuite headless
- `POST /burpsuite/scan` - Execute BurpSuite scan
- `POST /burpsuite/stop` - Stop BurpSuite instance

## Tools Catalog

### Network Scanning (6 tools)
- **nmap** - `/usr/bin/nmap` - Network mapper
- **masscan** - `/usr/bin/masscan` - High-speed scanner
- **amass** - `/snap/bin/amass` - Subdomain enumeration
- **assetfinder** - `~/go/bin/assetfinder` - Domain finder
- **waybackurls** - `~/go/bin/waybackurls` - Archive crawler
- **shuffledns** - `~/go/bin/shuffledns` - DNS bruteforcer

### Web Application (9 tools)
- **httpx** - `~/.local/bin/httpx` - HTTP probe
- **nuclei** - `~/go/bin/nuclei` - Vulnerability scanner
- **gobuster** - `/usr/bin/gobuster` - Directory fuzzer
- **ffuf** - `/usr/bin/ffuf` - Web fuzzer
- **katana** - `~/go/bin/katana` - Web crawler
- **arjun** - `~/.local/bin/arjun` - Parameter discovery
- **alterx** - `~/go/bin/alterx` - Wordlist generator
- **burpsuite** - BurpSuite Community v2025.10 (headless)
- **nikto** - `/usr/bin/nikto` - Web scanner

### Exploitation (5 tools)
- **sqlmap** - `~/.local/bin/sqlmap` - SQL injection
- **hydra** - `/usr/bin/hydra` - Password brute-forcer
- **metasploit** - `/usr/local/bin/msfconsole` - Framework
- **john** - `/usr/sbin/john` - Password cracker
- **hashcat** - `/usr/bin/hashcat` - Advanced cracking

### Network Exploitation (3 tools)
- **crackmapexec** - `~/.local/bin/crackmapexec` - Network pentest
- **responder** - `~/.local/bin/responder` - LLMNR poisoner
- **bettercap** - `/usr/bin/bettercap` - MITM framework

### Active Directory (1 tool)
- **bloodhound** - `/usr/local/bin/bloodhound-python` - AD enumeration

### SSL/TLS (2 tools)
- **sslscan** - `/usr/bin/sslscan` - SSL/TLS scanner
- **nikto** - `/usr/bin/nikto` - Web server scanner

### Cloud Security (1 tool)
- **scout-suite** - `~/.local/bin/scout` - Multi-cloud audit

## Workflows

### Available Workflows

1. **reconnaissance**
   - Comprehensive information gathering
   - 5 steps: nmap, assetfinder, port scan, fingerprinting, archive search

2. **web_application**
   - Web application security assessment
   - 6 steps: directory discovery, SQL injection, vulnerability scan, SSL/TLS, auth testing, file inclusion

3. **network_infrastructure**
   - Network-focused penetration testing
   - 6 steps: host discovery, service enumeration, vulnerability scanning, misconfiguration testing, exploitation, segmentation assessment

4. **full_penetration_test**
   - Complete methodology execution
   - 7 phases: port scan, version detection, web enumeration, vulnerability scanning, exploitation, post-exploitation, reporting

5. **quick_scan**
   - Fast security assessment
   - 4 steps: port scan, directory enum, SSL check, vulnerability scan

6. **comprehensive_scan**
   - Thorough security testing
   - 10 steps: network discovery, service enumeration, web testing, vulnerability scanning, SSL analysis, directory enumeration, SQL injection, auth testing, exploitation, reporting

## Converting to MCP Project

### Steps to Create Separate MCP Project

1. **Create New Repository**
   ```bash
   mkdir pentest-agent-mcp
   cd pentest-agent-mcp
   git init
   ```

2. **Copy Core Files**
   ```bash
   cp -r /home/MrFkry/PentestAgent/draft/* .
   cp -r /home/MrFkry/PentestAgent/core .
   cp -r /home/MrFkry/PentestAgent/workflows .
   cp -r /home/MrFkry/PentestAgent/rag .
   cp -r /home/MrFkry/PentestAgent/config .
   ```

3. **Setup MCP Server**
   ```bash
   cp mcp-server/mcp-server-config.json ./mcp.json
   # Edit mcp.json to use GitHub MCP server URL
   ```

4. **Create Dockerfile**
   ```dockerfile
   FROM python:3.11-slim

   WORKDIR /app
   COPY requirements.txt .
   RUN pip install -r requirements.txt

   COPY . .

   EXPOSE 8000
   CMD ["python", "main.py", "--mcp-mode"]
   ```

5. **Configure GitHub Actions**
   ```yaml
   # .github/workflows/publish.yml
   name: Publish MCP Server

   on:
     push:
       tags:
         - 'v*'

   jobs:
     publish:
       runs-on: ubuntu-latest
       steps:
         - uses: actions/checkout@v3
         - name: Build and push
           run: |
             docker build -t ghcr.io/mrfkry/pentest-agent-mcp:${{ github.ref_name }} .
             docker push ghcr.io/mrfkry/pentest-agent-mcp:${{ github.ref_name }}
   ```

6. **Update Package Configuration**
   - Edit `mcp-server-config.json` with proper URLs
   - Set version to match release tag
   - Configure environment variables

7. **Publish to GitHub Container Registry**
   ```bash
   docker build -t ghcr.io/mrfkry/pentest-agent-mcp:0.1.0 .
   docker push ghcr.io/mrfkry/pentest-agent-mcp:0.1.0
   ```

## Environment Variables

### Required Variables

```bash
# Gemini AI Model
export GEMINI_API_KEY="your-gemini-api-key"

# GitHub Integration (optional)
export GITHUB_TOKEN="ghp_your-github-token"

# Model Configuration
export MODEL_NAME="gemini-1.5-flash"
```

### Optional Variables

```bash
# Google Cloud Project (for Vertex AI)
export GOOGLE_CLOUD_PROJECT="your-project-id"

# Results Directory
export RESULTS_DIR="/home/MrFkry/PentestAgent/Results"

# Knowledge Base Path
export KNOWLEDGE_BASE_PATH="/home/MrFkry/PentestAgent/knowledge"
```

## Usage Examples

### Using OpenAPI Spec

```bash
# Import into Postman
# File > Import > Select pentest-agent-openapi-3.1.json

# Generate client code
npx @openapitools/openapi-generator-cli generate \
  -i pentest-agent-openapi-3.1.json \
  -g python \
  -o ./python-client

# View in Swagger UI
docker run -p 8080:8080 \
  -e SWAGGER_JSON=/spec/pentest-agent-openapi-3.1.json \
  -v $(pwd):/spec \
  swaggerapi/swagger-ui
```

### Using MCP Configuration

```bash
# Install in Claude Desktop
# Copy mcp-server/mcp-server-config.json to:
# - macOS: ~/Library/Application Support/Claude/mcp.json
# - Windows: %APPDATA%/Claude/mcp.json
# - Linux: ~/.config/Claude/mcp.json

# Or use with MCP CLI
mcp add pentest-agent mcp-server/mcp-server-config.json
```

### Using BurpSuite

```bash
# Download BurpSuite Community
wget -O burpsuite/burpsuite_community_v2025.10.jar \
  https://portswigger.net/burp/releases/download?product=community&version=2025.10&type=Jar

# Run headless
java -jar -Xmx2g burpsuite/burpsuite_community_v2025.10.jar \
  --project-file=burpsuite/project.burp \
  --config-file=burpsuite/config.json \
  --headless
```

## Next Steps

1. **Review Documentation**
   - Read all `.md` files in this directory
   - Understand API endpoints and schemas
   - Review tool configurations

2. **Test API Specifications**
   - Import OpenAPI spec into API testing tool
   - Validate endpoint definitions
   - Test request/response schemas

3. **Setup MCP Server**
   - Configure GitHub MCP server
   - Set environment variables
   - Test tool integrations

4. **Implement BurpSuite**
   - Download BurpSuite Community
   - Configure headless mode
   - Test proxy functionality

5. **Create Container Images**
   - Build Docker images
   - Push to GitHub Container Registry
   - Test container deployment

6. **Publish MCP Package**
   - Update package metadata
   - Publish to MCP registry
   - Create release documentation

## Resources

### Documentation Files

- `BURPSUITE_INTEGRATION.md` - BurpSuite setup and usage
- `TOOL_INVENTORY.json` - Complete tool catalog
- `mcp-server-config.json` - MCP server configuration

### External Resources

- [OpenAPI Specification](https://spec.openapis.org/oas/v3.1.0)
- [MCP Documentation](https://modelcontextprotocol.io)
- [BurpSuite Documentation](https://portswigger.net/burp/documentation)
- [GitHub Container Registry](https://docs.github.com/en/packages/working-with-a-github-packages-registry/working-with-the-container-registry)

## Support

For issues or questions:
- GitHub Issues: https://github.com/MrFkry/PentestAgent/issues
- Project Repository: https://github.com/MrFkry/PentestAgent

## License

This project is licensed under the MIT License. See LICENSE file for details.

---

**Last Updated:** 2025-10-20
**Version:** 0.1.0
**Author:** MrFkry
**Maintainer:** GHOSTCREW Team
