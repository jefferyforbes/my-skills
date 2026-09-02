#!/usr/bin/env python3
"""
AirLLM API Client & Standalone CLI Tester
"""

import argparse
import json
import sys
import requests


def query_api(base_url: str, prompt: str, max_tokens: int = 128, is_chat: bool = True):
    if is_chat:
        url = f"{base_url.rstrip('/')}/v1/chat/completions"
        payload = {
            "messages": [
                {"role": "system", "content": "You are a helpful AI assistant."},
                {"role": "user", "content": prompt}
            ],
            "max_tokens": max_tokens
        }
        res = requests.post(url, json=payload)
        res.raise_for_status()
        data = res.json()
        print("\n--- Assistant Response ---")
        print(data["choices"][0]["message"]["content"])
        print("--------------------------\n")
    else:
        url = f"{base_url.rstrip('/')}/v1/completions"
        payload = {
            "prompt": prompt,
            "max_tokens": max_tokens
        }
        res = requests.post(url, json=payload)
        res.raise_for_status()
        data = res.json()
        print("\n--- Completion Output ---")
        print(data["choices"][0]["text"])
        print("--------------------------\n")


def check_health(base_url: str):
    url = f"{base_url.rstrip('/')}/health"
    res = requests.get(url)
    print("Health Status:", json.dumps(res.json(), indent=2))


def main():
    parser = argparse.ArgumentParser(description="Query AirLLM API Server")
    parser.add_argument("--url", type=str, default="http://localhost:8000", help="AirLLM API base URL")
    parser.add_argument("--prompt", type=str, default="What are the three laws of robotics?", help="Prompt to send")
    parser.add_argument("--max-tokens", type=int, default=128, help="Max tokens to generate")
    parser.add_argument("--completion", action="store_true", help="Use raw completions endpoint instead of chat")
    parser.add_argument("--health", action="store_true", help="Check server health status")

    args = parser.parse_args()

    if args.health:
        check_health(args.url)
    else:
        query_api(args.url, args.prompt, args.max_tokens, is_chat=not args.completion)


if __name__ == "__main__":
    main()
