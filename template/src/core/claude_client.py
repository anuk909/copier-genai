"""
Claude Client Implementation Example

TODO: Implement your Claude client here.
Install: uv add anthropic

Example structure:
```python
import os
from anthropic import Anthropic
from .base_llm import BaseLLM, Message, LLMResponse

class ClaudeClient(BaseLLM):
    def __init__(self, model_name: str, **kwargs):
        super().__init__(model_name, **kwargs)
        self.client = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))
    
    def generate(self, messages, **kwargs):
        # Implement Claude API call
        pass
```
"""

from .base_llm import BaseLLM

# TODO: Implement your Claude client
