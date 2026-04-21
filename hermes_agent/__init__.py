"""Hermes Agent - A fork of NousResearch/hermes-agent.

An intelligent agent framework built on top of the Hermes model family,
providing tool use, function calling, and agentic loop capabilities.
"""

__version__ = "0.1.0"
__author__ = "Hermes Agent Contributors"
__license__ = "Apache-2.0"

from hermes_agent.agent import HermesAgent
from hermes_agent.config import AgentConfig

__all__ = [
    "HermesAgent",
    "AgentConfig",
    "__version__",
]
