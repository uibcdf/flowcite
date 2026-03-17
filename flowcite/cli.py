from __future__ import annotations
import argparse
import sys
from pathlib import Path
from .core.collector import Collector
from .core.report import report

def main():
    parser = argparse.ArgumentParser(description=\"FlowCite CLI - Inspect saved citation sessions.\")
    parser.add_argument(\"session_file\", help=\"Path to a saved session JSON file (from enable_persistence)\")
    parser.add_argument("--format", "-f", default="text", 
                        choices=["text", "markdown", "bibtex", "csl-json", "provenance", "latex"],
                        help="Output format (default: text)")
    
    args = parser.parse_args()
    
    session_path = Path(args.session_file)
    if not session_path.exists():
        print(f\"Error: Session file not found: {args.session_file}\", file=sys.stderr)
        sys.exit(1)
        
    # Load session into the global Collector
    Collector.enable_persistence(session_path)
    
    # Generate report
    try:
        output = report(format=args.format)
        print(output)
    except Exception as e:
        print(f\"Error generating report: {e}\", file=sys.stderr)
        sys.exit(1)

if __name__ == \"__main__\":
    main()
