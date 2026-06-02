# app/providers/openai_provider.py

import os
import json

from openai import OpenAI


VALID_AGENTS = {
    "home",
    "office",
    "doctor",
    "travel",
    "general"
}


class OpenAIProvider:

    def __init__(self):

        self.client = OpenAI(
            api_key=os.getenv(
                "OPENAI_API_KEY"
            )
        )

    def classify(
        self,
        query
    ):

        prompt = f"""
You are an intent classifier.

Available agents:

home
office
doctor
travel
general

User Query:
{query}

Return JSON only:

{{
    "agent":"",
    "confidence":0.0,
    "reason":""
}}
"""

        try:

            response = (
                self.client.chat.completions.create(
                    model="gpt-4o-mini",
                    messages=[
                        {
                            "role": "user",
                            "content": prompt
                        }
                    ],
                    temperature=0,
                    max_tokens=80
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

            result = json.loads(
                content
            )

            agent = (
                result.get(
                    "agent",
                    "general"
                )
                .lower()
                .strip()
            )

            if agent not in VALID_AGENTS:

                agent = "general"

            return {

                "provider":
                    "openai",

                "agent":
                    agent,

                "confidence":
                    float(
                        result.get(
                            "confidence",
                            0.5
                        )
                    ),

                "reason":
                    result.get(
                        "reason",
                        ""
                    )
            }

        except Exception as e:

            print(
                f"OpenAI Error: {e}"
            )

            return {

                "provider":
                    "openai",

                "agent":
                    "general",

                "confidence":
                    0.50,

                "reason":
                    "fallback"
            }