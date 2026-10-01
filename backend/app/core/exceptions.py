class AgentFlowException(Exception):
    """Base exception for AgentFlow."""


class ConfigurationError(AgentFlowException):
    """Raised when application configuration is invalid."""


class ResourceNotFoundError(AgentFlowException):
    """Raised when a requested resource does not exist."""


class AuthenticationError(AgentFlowException):
    """Raised when authentication fails."""


class AuthorizationError(AgentFlowException):
    """Raised when a user is not authorized to access a resource."""