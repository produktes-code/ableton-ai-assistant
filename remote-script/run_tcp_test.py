import sys
from unittest.mock import MagicMock

sys.modules["ableton"] = MagicMock()
sys.modules["ableton.v3"] = MagicMock()
sys.modules["ableton.v3.control_surface"] = MagicMock()

import unittest  # noqa: E402

if __name__ == "__main__":
    unittest.main()
