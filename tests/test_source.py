from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]


class App02SourceTests(unittest.TestCase):
    def test_api_response_and_health_endpoint_are_configured(self):
        config = (ROOT / "src/default.conf").read_text(encoding="utf-8")
        self.assertIn('"service":"app02-service"', config)
        self.assertIn("location = /healthz", config)
        self.assertIn("listen 8080", config)


if __name__ == "__main__":
    unittest.main()
