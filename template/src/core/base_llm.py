"""
Base LLM Interface
Defines the abstract interface that all LLM providers must implement.
"""

from abc import ABC, abstractmethod
from typing import Any, AsyncIterator, Dict, List, Optional
from dataclasses import dataclass


@dataclass
class Message:
    """Standardized message format"""
    role: str  # 'system', 'user', 'assistant'
    content: str


@dataclass
class LLMResponse:
    """Standardized response format from all LLM providers"""
    content: str
    model: str
    metadata: Optional[Dict[str, Any]] = None


class BaseLLM(ABC):
    """
    Abstract base class for all LLM providers.
    
    Implement this interface for each LLM provider you want to support.
    """
    
    def __init__(self, model_name: str, **kwargs):
        """
        Initialize the LLM client.
        
        Args:
            model_name: The model identifier
            **kwargs: Provider-specific configuration
        """
        self.model_name = model_name
        self.config = kwargs
        
    @abstractmethod
    def generate(
        self,
        messages: List[Message],
        **kwargs
    ) -> LLMResponse:
        """
        Synchronous generation method.
        
        Args:
            messages: List of conversation messages
            **kwargs: Additional provider-specific parameters
            
        Returns:
            LLMResponse: Standardized response object
        """
        pass
    
    @abstractmethod
    async def agenerate(
        self,
        messages: List[Message],
        **kwargs
    ) -> LLMResponse:
        """
        Asynchronous generation method.
        
        Args:
            messages: List of conversation messages
            **kwargs: Additional provider-specific parameters
            
        Returns:
            LLMResponse: Standardized response object
        """
        pass
    
    @abstractmethod
    async def stream(
        self,
        messages: List[Message],
        **kwargs
    ) -> AsyncIterator[str]:
        """
        Stream response tokens as they're generated.
        
        Args:
            messages: List of conversation messages
            **kwargs: Additional provider-specific parameters
            
        Yields:
            str: Individual tokens or chunks
        """
        pass
    
    def estimate_tokens(self, text: str) -> int:
        """
        Estimate the token count for a given text.
        
        Args:
            text: The text to estimate tokens for
            
        Returns:
            int: Approximate token count
        """
        # Simple estimation: ~4 chars per token
        return len(text) // 4
    
    def validate_messages(self, messages: List[Message]) -> None:
        """
        Validate message format before sending to provider.
        
        Args:
            messages: List of messages to validate
            
        Raises:
            ValueError: If messages are invalid
        """
        if not messages:
            raise ValueError("Messages list cannot be empty")
        
        if not all(isinstance(msg, Message) for msg in messages):
            raise ValueError("All messages must be Message instances")
    
    def __repr__(self) -> str:
        return (
            f"{self.__class__.__name__}("
            f"model={self.model_name}, "
            f"temperature={self.temperature}, "
            f"max_tokens={self.max_tokens})"
        )
