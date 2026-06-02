# app/providers/gemini_provider.py

import google.generativeai as genai

class GeminiProvider:

    def classify(self, query):

        q = query.lower()

        if "flight" in q:
            return {
                "provider": "gemini",
                "agent": "travel",
                "confidence": 0.89,
                "reason": "travel intent"
            }

        return {
            "provider": "gemini",
            "agent": "general",
            "confidence": 0.60,
            "reason": "fallback"
        }