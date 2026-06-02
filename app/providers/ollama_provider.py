# app/providers/ollama_provider.py

import json
import time
import re

import ollama


VALID_AGENTS = {
    "home",
    "office",
    "doctor",
    "travel",
    "general"
}


class OllamaProvider:

    def classify(
        self,
        query
    ):

        start_time = time.time()

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

            response = ollama.chat(
                model="llama3:latest",
                messages=[
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                options={
                    "temperature": 0,
                    "num_predict": 20
                }
            )

            content = (
                response["message"]["content"]
                .strip()
            )

            # ---------------------------------
            # Remove markdown fences
            # ---------------------------------

            if content.startswith("```"):

                content = (
                    content
                    .replace("```json", "")
                    .replace("```", "")
                    .strip()
                )

            # ---------------------------------
            # Extract JSON safely
            # ---------------------------------

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
                    0.50
                )
            )

            confidence = max(
                0.0,
                min(
                    confidence,
                    1.0
                )
            )

            latency = round(
                time.time() - start_time,
                3
            )

            return {

                "provider":
                    "ollama",

                "agent":
                    agent,

                "confidence":
                    confidence,

                "reason":
                    "",

                "latency":
                    latency
            }

        except Exception as e:

            latency = round(
                time.time() - start_time,
                3
            )

            print(
                f"[OllamaProvider Error] {e}"
            )

            return {

                "provider":
                    "ollama",

                "agent":
                    "general",

                "confidence":
                    0.50,

                "reason":
                    "fallback",

                "latency":
                    latency
            }