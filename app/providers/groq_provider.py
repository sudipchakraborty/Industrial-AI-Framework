# app/providers/groq_provider.py

import os
import json
import re

from groq import Groq


VALID_AGENTS = {
    "home",
    "office",
    "doctor",
    "travel",
    "general"
}


class GroqProvider:

    def __init__(self):

        self.client = Groq(
            api_key=os.getenv(
                "GROQ_API_KEY"
            )
        )

    def classify(
        self,
        query
    ):

        prompt = f"""
Classify the query into exactly ONE agent.

Agents:

home
office
doctor
travel
general

Query:
{query}

Return ONLY JSON.

Example:

{{"agent":"general","confidence":0.85}}
"""

        try:

            response = (
                self.client.chat.completions.create(
                    model="llama-3.3-70b-versatile",
                    messages=[
                        {
                            "role": "user",
                            "content": prompt
                        }
                    ],
                    temperature=0,
                    max_tokens=50
                )
            )

            content = (
                response
                .choices[0]
                .message
                .content
                .strip()
            )

            if content.startswith("```"):

                content = (
                    content
                    .replace("```json", "")
                    .replace("```", "")
                    .strip()
                )

            try:

                result = json.loads(
                    content
                )

            except Exception:

                match = re.search(
                    r"\{.*\}",
                    content,
                    re.DOTALL
                )

                if not match:

                    raise ValueError(
                        "No JSON found"
                    )

                result = json.loads(
                    match.group()
                )

            agent = (
                str(
                    result.get(
                        "agent",
                        "general"
                    )
                )
                .lower()
                .strip()
            )

            if agent not in VALID_AGENTS:

                agent = "general"

            confidence = float(
                result.get(
                    "confidence",
                    0.5
                )
            )

            confidence = max(
                0.0,
                min(
                    confidence,
                    1.0
                )
            )

            return {

                "provider":
                    "groq",

                "agent":
                    agent,

                "confidence":
                    confidence,

                "reason":
                    ""
            }

        except Exception as e:

            print(
                f"[GroqProvider Error] {e}"
            )

            return {

                "provider":
                    "groq",

                "agent":
                    "general",

                "confidence":
                    0.50,

                "reason":
                    "fallback"
            }