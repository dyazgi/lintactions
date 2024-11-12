import re

import yaml


def to_kebab_case(s):
    """Convert a string to kebab-case."""
    # Insert a hyphen before uppercase letters and convert to lowercase
    s = re.sub(r"(?<!^)(?=[A-Z])", "_", s).lower()
    # Replace underscores with hyphens
    s = s.replace("-", "_")
    return s


class DotDict(dict):
    """A dictionary that supports dot notation and converts all keys to kebab-case."""

    def __init__(self, dct=None):
        super().__init__()
        if dct is not None:
            for key, value in dct.items():
                kebab_key = to_kebab_case(key)
                res = None
                if isinstance(value, dict):
                    res = DotDict(value)
                elif isinstance(value, list):
                    res = [DotDict(item) if isinstance(item, dict) else item for item in value]
                self[kebab_key] = res

    def __getattr__(self, key):
        kebab_key = to_kebab_case(key)
        try:
            return self[kebab_key]
        except KeyError:
            raise AttributeError(f"'DotDict' object has no attribute '{kebab_key}'") from None

    def __setattr__(self, key, value):
        kebab_key = to_kebab_case(key)
        if isinstance(value, dict):
            value = DotDict(value)
        elif isinstance(value, list):
            value = [DotDict(item) if isinstance(item, dict) else item for item in value]
        self[kebab_key] = value

    def __delattr__(self, key):
        kebab_key = to_kebab_case(key)
        del self[kebab_key]

    def __getitem__(self, key):
        kebab_key = to_kebab_case(key)
        return super().__getitem__(kebab_key)

    def __setitem__(self, key, value):
        kebab_key = to_kebab_case(key)
        if isinstance(value, dict):
            value = DotDict(value)
        elif isinstance(value, list):
            value = [DotDict(item) if isinstance(item, dict) else item for item in value]
        super().__setitem__(kebab_key, value)

    def __delitem__(self, key):
        kebab_key = to_kebab_case(key)
        super().__delitem__(kebab_key)


class ConfigManager:
    def __init__(self, filepath=None):
        self.config = DotDict()
        self.filepath = filepath
        if filepath:
            self.load(filepath)

    def load(self, filepath):
        """Load configuration from a YAML file."""
        with open(filepath, "r") as file:
            data = yaml.safe_load(file)
            self.config = DotDict(data)
        self.filepath = filepath

    def save(self, filepath=None):
        """Save configuration to a YAML file."""
        if filepath is None:
            if self.filepath is None:
                raise ValueError("No file path specified for saving the configuration.")
            filepath = self.filepath
        # Convert DotDict to a regular dict before saving
        with open(filepath, "w") as file:
            yaml.dump(self._to_dict(self.config), file)

    def get(self, key, default=None):
        """Get a configuration value."""
        return self.config.get(to_kebab_case(key), default)

    def set(self, key, value):
        """Set a configuration value."""
        self.config[to_kebab_case(key)] = value

    def _to_dict(self, obj):
        """Recursively convert a DotDict to a regular dict."""
        if isinstance(obj, DotDict):
            return {k: self._to_dict(v) for k, v in obj.items()}
        if isinstance(obj, list):
            return [self._to_dict(v) if isinstance(v, DotDict) else v for v in obj]
        return obj


if __name__ == "__main__":
    # Initialize ConfigManager and load configurations
    config = ConfigManager("config.yaml")

    # Access configuration values using dot notation
    db_host = config.config.database.host  # Accesses 'databaseHost' as 'database-host'
    db_port = config.config.database.port  # Accesses 'database_port' as 'database-port'
    username = config.config.credentials.username  # Accesses 'UserName' as 'username'

    print(f"Connecting to {db_host}:{db_port} as {username}")

    # Modify a configuration value
    config.config.database_port = 5432

    # Add a new configuration value
    config.config.credentials.api_key = "new_api_key"

    # Save the updated configurations back to the file
    config.save()
