#!/usr/bin/env python3
import json
import logging
import os
import sys
from pathlib import Path

LOG = Path(__file__).resolve().parent.parent / "skill.log"
logging.basicConfig(
    filename=LOG,
    level=logging.INFO,
    format="%(asctime)s [pid=%(process)d] %(message)s",
)

logger = logging.getLogger(__name__)

def main():
    logger.info("invoked argv=%r cwd=%s", sys.argv, os.getcwd())
    location = sys.argv[1] if len(sys.argv) > 1 else None
    if not location:
        logger.error("missing location arg")
        print(json.dumps({"error": "location argument required"}))
        sys.exit(1)

    logger.info("resolved location=%s", location)
    print(json.dumps({"location": location, "weather": "sunny"}))

if __name__ == "__main__":
    main()