# BurpSuite Community v2025.10 Headless Integration

## Overview

This document provides comprehensive information on integrating BurpSuite Community v2025.10 in headless mode with the GHOSTCREW Pentest Agent.

## Installation

### Download BurpSuite Community

```bash
# Navigate to project root
cd /home/MrFkry/PentestAgent

# Create burpsuite directory
mkdir -p burpsuite

# Download BurpSuite Community v2025.10 (example - replace with actual download)
wget -O burpsuite/burpsuite_community_v2025.10.jar \
  https://portswigger.net/burp/releases/download?product=community&version=2025.10&type=Jar

# Verify download
ls -lh burpsuite/burpsuite_community_v2025.10.jar
```

### Requirements

- Java Runtime Environment (JRE) 11 or higher
- Minimum 2GB RAM allocated to Java
- Write permissions for project directories

```bash
# Check Java version
java -version

# Should output: openjdk version "11" or higher
```

## Headless Mode Configuration

### Basic Headless Launch

```bash
# Launch BurpSuite in headless mode with REST API
java -jar -Xmx2g \
  /home/MrFkry/PentestAgent/burpsuite/burpsuite_community_v2025.10.jar \
  --project-file=/home/MrFkry/PentestAgent/burpsuite/project.burp \
  --config-file=/home/MrFkry/PentestAgent/burpsuite/config.json \
  --unpause-spider-and-scanner \
  --headless
```

### Configuration File Structure

Create `/home/MrFkry/PentestAgent/burpsuite/config.json`:

```json
{
  "proxy": {
    "request_listeners": [
      {
        "certificate_mode": "per_host",
        "listen_mode": "all_interfaces",
        "listener_port": 8080,
        "running": true,
        "support_invisible_proxying": true
      }
    ]
  },
  "scanner": {
    "active_scanning_engine": {
      "number_of_threads": 10
    },
    "audit_optimization": {
      "skip_ineffective_checks": true
    }
  },
  "spider": {
    "max_link_depth": 5,
    "max_duration": 0,
    "number_of_threads": 10
  }
}
```

## REST API Integration

BurpSuite Community headless mode doesn't include the full REST API, but can be extended with the following:

### Alternative: BurpSuite Pro API

For full REST API functionality, consider BurpSuite Professional. The GHOSTCREW agent is designed to work with both.

### Community Edition Workarounds

Since Community Edition has limited API support, we use command-line arguments and file-based communication:

#### 1. Project File Monitoring

```python
# Python integration example
import subprocess
import json
import time
from pathlib import Path

class BurpSuiteHeadless:
    def __init__(self, jar_path, project_dir):
        self.jar_path = jar_path
        self.project_dir = Path(project_dir)
        self.process = None

    def start(self, port=8080):
        """Start BurpSuite in headless mode"""
        project_file = self.project_dir / "project.burp"
        config_file = self.project_dir / "config.json"

        cmd = [
            "java",
            "-jar",
            "-Xmx2g",
            self.jar_path,
            f"--project-file={project_file}",
            f"--config-file={config_file}",
            "--unpause-spider-and-scanner",
            "--headless"
        ]

        self.process = subprocess.Popen(
            cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )

        return {
            "status": "started",
            "pid": self.process.pid,
            "proxy_port": port
        }

    def stop(self):
        """Stop BurpSuite"""
        if self.process:
            self.process.terminate()
            self.process.wait(timeout=10)
            return {"status": "stopped"}

    def get_status(self):
        """Check if BurpSuite is running"""
        if self.process and self.process.poll() is None:
            return {"status": "running", "pid": self.process.pid}
        return {"status": "stopped"}
```

## Command-Line Arguments Reference

### Essential Arguments

| Argument | Description | Example |
|----------|-------------|---------|
| `--project-file` | Path to Burp project file | `--project-file=/path/to/project.burp` |
| `--config-file` | Path to configuration JSON | `--config-file=/path/to/config.json` |
| `--headless` | Run without GUI | `--headless` |
| `--unpause-spider-and-scanner` | Auto-start scanning | `--unpause-spider-and-scanner` |
| `-Xmx` | Maximum Java heap size | `-Xmx2g` |

### Advanced Arguments

| Argument | Description | Example |
|----------|-------------|---------|
| `--diagnostics` | Enable diagnostic logging | `--diagnostics` |
| `--disable-auto-update` | Disable auto-updates | `--disable-auto-update` |
| `--user-config-file` | User-specific configuration | `--user-config-file=/path/to/user.json` |

## Proxy Configuration

### System-Wide Proxy Setup

```bash
# Set environment variables for tools to use Burp proxy
export http_proxy="http://127.0.0.1:8080"
export https_proxy="http://127.0.0.1:8080"
export HTTP_PROXY="http://127.0.0.1:8080"
export HTTPS_PROXY="http://127.0.0.1:8080"
```

### Tool-Specific Proxy Configuration

```bash
# Example: Use Burp with curl
curl --proxy http://127.0.0.1:8080 -k https://example.com

# Example: Use Burp with nuclei
nuclei -u https://example.com -proxy http://127.0.0.1:8080

# Example: Use Burp with sqlmap
sqlmap -u "https://example.com/page?id=1" --proxy=http://127.0.0.1:8080
```

## Scanning Workflows

### 1. Passive Scanning

```bash
# Start Burp in passive mode
java -jar -Xmx2g burpsuite_community_v2025.10.jar \
  --project-file=passive_scan.burp \
  --config-file=passive_config.json \
  --headless
```

### 2. Active Scanning (Pro Only)

Active scanning requires BurpSuite Professional. For Community Edition, use passive scanning and manual testing.

### 3. Spider/Crawler

```json
{
  "spider": {
    "mode": "modern",
    "max_link_depth": 10,
    "max_duration": 3600,
    "thread_count": 10,
    "case_sensitive": false,
    "detect_custom_not_found_responses": true
  }
}
```

## Integration with GHOSTCREW Agent

### Tool Manager Integration

Add to `/home/MrFkry/PentestAgent/core/tool_manager.py`:

```python
"burpsuite": {
    "path": "/usr/bin/java",
    "jar_path": "/home/MrFkry/PentestAgent/burpsuite/burpsuite_community_v2025.10.jar",
    "requires_sudo": False,
    "description": "Web application security testing platform",
    "phases": ["enumeration", "vulnerability_assessment"],
    "commands": {
        "passive_proxy": [
            "-jar", "-Xmx2g",
            "/home/MrFkry/PentestAgent/burpsuite/burpsuite_community_v2025.10.jar",
            "--project-file=/home/MrFkry/PentestAgent/burpsuite/project.burp",
            "--config-file=/home/MrFkry/PentestAgent/burpsuite/passive_config.json",
            "--headless"
        ],
        "spider": [
            "-jar", "-Xmx2g",
            "/home/MrFkry/PentestAgent/burpsuite/burpsuite_community_v2025.10.jar",
            "--project-file=/home/MrFkry/PentestAgent/burpsuite/spider_project.burp",
            "--config-file=/home/MrFkry/PentestAgent/burpsuite/spider_config.json",
            "--unpause-spider-and-scanner",
            "--headless"
        ]
    }
}
```

### MCP Server Configuration

Add to `/home/MrFkry/PentestAgent/mcp.json`:

```json
{
  "name": "burpsuite",
  "params": {
    "command": "/usr/bin/java",
    "args": [
      "-jar",
      "-Xmx2g",
      "/home/MrFkry/PentestAgent/burpsuite/burpsuite_community_v2025.10.jar",
      "--headless",
      "--project-file=/home/MrFkry/PentestAgent/burpsuite/mcp_project.burp",
      "--config-file=/home/MrFkry/PentestAgent/burpsuite/mcp_config.json"
    ],
    "env": {
      "JAVA_HOME": "/usr/lib/jvm/java-11-openjdk-amd64",
      "PATH": "/usr/bin:/bin"
    }
  },
  "cache_tools_list": false
}
```

## Certificate Management

### Export Burp CA Certificate

```bash
# Certificate is auto-generated in project directory
# Location: burpsuite/cacert.der

# Convert to PEM format for system trust
openssl x509 -inform DER \
  -in burpsuite/cacert.der \
  -out burpsuite/cacert.pem

# Install certificate (Ubuntu/Debian)
sudo cp burpsuite/cacert.pem /usr/local/share/ca-certificates/burp-ca.crt
sudo update-ca-certificates
```

### Configure Tools to Trust Burp Certificate

```bash
# For Python requests
export REQUESTS_CA_BUNDLE=/home/MrFkry/PentestAgent/burpsuite/cacert.pem

# For curl
curl --cacert /home/MrFkry/PentestAgent/burpsuite/cacert.pem https://example.com

# For wget
wget --ca-certificate=/home/MrFkry/PentestAgent/burpsuite/cacert.pem https://example.com
```

## Results and Reporting

### Export Burp Results

Since headless mode has limited export options, use project file analysis:

```bash
# Results are stored in project file
# Use Burp GUI to open and export reports later:
java -jar burpsuite_community_v2025.10.jar \
  --project-file=/home/MrFkry/PentestAgent/burpsuite/project.burp
```

### Programmatic Access (Limited)

Community Edition doesn't provide REST API for results. Consider:

1. Using Burp Extender API (requires Java plugin development)
2. Parsing project file (Burp uses SQLite internally)
3. Upgrading to Burp Professional for full REST API

## Troubleshooting

### Common Issues

#### 1. Java Heap Space Error

```bash
# Increase heap size
java -jar -Xmx4g burpsuite_community_v2025.10.jar --headless
```

#### 2. Port Already in Use

```bash
# Check what's using port 8080
sudo lsof -i :8080

# Kill process or use different port in config
```

#### 3. Project File Locked

```bash
# Remove lock file
rm burpsuite/project.burp.lock
```

#### 4. Certificate Errors

```bash
# Regenerate certificate by deleting existing
rm burpsuite/cacert.der
# Restart Burp to regenerate
```

## Performance Optimization

### Memory Configuration

```bash
# For small targets (< 100 pages)
-Xmx1g

# For medium targets (100-1000 pages)
-Xmx2g

# For large targets (> 1000 pages)
-Xmx4g or more
```

### Threading Configuration

```json
{
  "spider": {
    "number_of_threads": 10
  },
  "scanner": {
    "active_scanning_engine": {
      "number_of_threads": 10
    }
  }
}
```

## Security Considerations

1. **Bind to localhost only** in production environments
2. **Use authentication** if exposing proxy port
3. **Encrypt project files** containing sensitive data
4. **Rotate certificates** periodically
5. **Monitor resource usage** to prevent DoS

## Additional Resources

- Official Documentation: https://portswigger.net/burp/documentation
- Burp Extensions: https://portswigger.net/bappstore
- Community Forum: https://forum.portswigger.net/

## License Notes

BurpSuite Community Edition is free for non-commercial use. For commercial pentesting, consider upgrading to Professional Edition which includes:

- REST API
- Active scanning
- Scanner customization
- Advanced reporting
- Commercial license

## File Paths Summary

| File/Directory | Path | Purpose |
|----------------|------|---------|
| BurpSuite JAR | `/home/MrFkry/PentestAgent/burpsuite/burpsuite_community_v2025.10.jar` | Main application |
| Project Files | `/home/MrFkry/PentestAgent/burpsuite/*.burp` | Scan projects |
| Configuration | `/home/MrFkry/PentestAgent/burpsuite/*.json` | Burp settings |
| CA Certificate | `/home/MrFkry/PentestAgent/burpsuite/cacert.der` | SSL interception cert |
| Logs | `/home/MrFkry/PentestAgent/burpsuite/logs/` | Diagnostic logs |

---

**Last Updated:** 2025-10-20
**Version:** 1.0.0
**Maintainer:** GHOSTCREW Team
