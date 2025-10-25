#!/usr/bin/env python3
"""
BurpSuite Community Headless Wrapper
Provides Python interface for BurpSuite headless operations
"""

import subprocess
import json
import time
import signal
import os
from pathlib import Path
from typing import Optional, Dict, Any, List


class BurpSuiteHeadless:
    """
    Python wrapper for BurpSuite Community headless mode.
    
    Usage:
        burp = BurpSuiteHeadless(
            jar_path="/path/to/burpsuite.jar",
            project_dir="/path/to/projects"
        )
        
        burp.start(port=8080)
        burp.get_status()
        burp.stop()
    """
    
    def __init__(
        self,
        jar_path: str,
        project_dir: str,
        java_path: str = "/usr/bin/java",
        heap_size: int = 2048
    ):
        """
        Initialize BurpSuite wrapper.
        
        Args:
            jar_path: Path to BurpSuite JAR file
            project_dir: Directory for BurpSuite projects
            java_path: Path to Java executable
            heap_size: Java heap size in MB
        """
        self.jar_path = Path(jar_path)
        self.project_dir = Path(project_dir)
        self.java_path = java_path
        self.heap_size = heap_size
        self.process: Optional[subprocess.Popen] = None
        self.pid: Optional[int] = None
        
        # Ensure directories exist
        self.project_dir.mkdir(parents=True, exist_ok=True)
        
        # Validate JAR exists
        if not self.jar_path.exists():
            raise FileNotFoundError(f"BurpSuite JAR not found: {self.jar_path}")
    
    def start(
        self,
        port: int = 8080,
        project_name: str = "default",
        config_file: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Start BurpSuite in headless mode.
        
        Args:
            port: Proxy port
            project_name: Name for project file
            config_file: Optional configuration JSON path
            
        Returns:
            Dict with status, pid, and port
        """
        if self.process and self.process.poll() is None:
            return {
                "status": "already_running",
                "pid": self.pid,
                "proxy_port": port
            }
        
        project_file = self.project_dir / f"{project_name}.burp"
        
        cmd = [
            self.java_path,
            "-jar",
            f"-Xmx{self.heap_size}m",
            str(self.jar_path),
            f"--project-file={project_file}",
            "--headless"
        ]
        
        if config_file:
            cmd.append(f"--config-file={config_file}")
        
        # Add unpause for spider/scanner
        cmd.append("--unpause-spider-and-scanner")
        
        try:
            self.process = subprocess.Popen(
                cmd,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                preexec_fn=os.setsid  # Create new process group
            )
            
            self.pid = self.process.pid
            
            # Wait a bit to ensure it started
            time.sleep(2)
            
            if self.process.poll() is not None:
                stderr = self.process.stderr.read().decode() if self.process.stderr else ""
                raise RuntimeError(f"BurpSuite failed to start: {stderr}")
            
            return {
                "status": "started",
                "pid": self.pid,
                "proxy_port": port,
                "project_file": str(project_file)
            }
            
        except Exception as e:
            return {
                "status": "failed",
                "error": str(e)
            }
    
    def stop(self) -> Dict[str, str]:
        """
        Stop BurpSuite process.
        
        Returns:
            Dict with status
        """
        if not self.process:
            return {"status": "not_running"}
        
        try:
            # Try graceful shutdown first
            os.killpg(os.getpgid(self.process.pid), signal.SIGTERM)
            
            # Wait up to 10 seconds for graceful shutdown
            for _ in range(10):
                if self.process.poll() is not None:
                    break
                time.sleep(1)
            
            # Force kill if still running
            if self.process.poll() is None:
                os.killpg(os.getpgid(self.process.pid), signal.SIGKILL)
                self.process.wait()
            
            self.process = None
            self.pid = None
            
            return {"status": "stopped"}
            
        except Exception as e:
            return {
                "status": "error",
                "error": str(e)
            }
    
    def get_status(self) -> Dict[str, Any]:
        """
        Get current BurpSuite status.
        
        Returns:
            Dict with status information
        """
        if not self.process:
            return {"status": "stopped"}
        
        if self.process.poll() is None:
            return {
                "status": "running",
                "pid": self.pid
            }
        else:
            return {
                "status": "stopped",
                "return_code": self.process.returncode
            }
    
    def create_config(
        self,
        output_path: str,
        proxy_port: int = 8080,
        spider_threads: int = 10,
        scanner_threads: int = 10
    ) -> str:
        """
        Create BurpSuite configuration file.
        
        Args:
            output_path: Where to save config
            proxy_port: Proxy listener port
            spider_threads: Number of spider threads
            scanner_threads: Number of scanner threads
            
        Returns:
            Path to created config file
        """
        config = {
            "proxy": {
                "request_listeners": [
                    {
                        "certificate_mode": "per_host",
                        "listen_mode": "all_interfaces",
                        "listener_port": proxy_port,
                        "running": True,
                        "support_invisible_proxying": True
                    }
                ]
            },
            "scanner": {
                "active_scanning_engine": {
                    "number_of_threads": scanner_threads
                },
                "audit_optimization": {
                    "skip_ineffective_checks": True
                }
            },
            "spider": {
                "max_link_depth": 5,
                "number_of_threads": spider_threads
            }
        }
        
        with open(output_path, 'w') as f:
            json.dump(config, f, indent=2)
        
        return output_path


def main():
    """Example usage"""
    import argparse
    
    parser = argparse.ArgumentParser(description="BurpSuite Headless Wrapper")
    parser.add_argument("action", choices=["start", "stop", "status"])
    parser.add_argument("--jar", required=True, help="Path to BurpSuite JAR")
    parser.add_argument("--project-dir", default="./burpsuite", help="Project directory")
    parser.add_argument("--port", type=int, default=8080, help="Proxy port")
    parser.add_argument("--config", help="Config file path")
    
    args = parser.parse_args()
    
    burp = BurpSuiteHeadless(
        jar_path=args.jar,
        project_dir=args.project_dir
    )
    
    if args.action == "start":
        result = burp.start(port=args.port, config_file=args.config)
        print(json.dumps(result, indent=2))
    
    elif args.action == "stop":
        result = burp.stop()
        print(json.dumps(result, indent=2))
    
    elif args.action == "status":
        result = burp.get_status()
        print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
