#!/bin/bash
cd basic_agent
adk api_server --host=0.0.0.0 --port=${PORT:-8080} --allow_origins="*"
