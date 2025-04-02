"""Test version management."""
import open_data_pvnet
from importlib.metadata import version

def test_version_consistency():
    """Test that package version matches the one in __init__.py."""
    package_version = version("open-data-pvnet")
    assert package_version == open_data_pvnet.__version__, (
        f"Version mismatch: package version ({package_version}) != "
        f"__init__ version ({open_data_pvnet.__version__})"
    )