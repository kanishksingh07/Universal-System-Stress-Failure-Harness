
import unittest
import sys
import os
import yaml

# Add parent dir to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

class TestResourceSafety(unittest.TestCase):
    def setUp(self):
        self.config_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'config', 'mutation-config.yaml'))
        with open(self.config_path, 'r') as f:
            self.config = yaml.safe_load(f)

    def test_timeout_defined(self):
        """Ensure timeout is strictly defined and reasonable."""
        target = self.config.get('target_system', {})
        timeout = target.get('timeout_seconds')
        self.assertIsNotNone(timeout, "CRITICAL: No timeout defined in config!")
        self.assertLess(timeout, 60, "Timeout > 60s risks holding resources too long.")
        self.assertGreater(timeout, 0, "Timeout must be positive.")

    def test_concurrency_limit(self):
        """Ensure concurrency is within safe limits."""
        settings = self.config.get('test_settings', {})
        concurrency = settings.get('concurrency')
        self.assertIsNotNone(concurrency, "CRITICAL: No concurrency limit defined!")
        self.assertLess(concurrency, 50, "Concurrency > 50 risks DoS'ing the host.")
        
    def test_total_volume_limit(self):
        """Ensure total requests are bounded."""
        settings = self.config.get('test_settings', {})
        total = settings.get('total_requests')
        self.assertLess(total, 100000, "Total requests > 100k risk local resource exhaustion without pagination.")

if __name__ == '__main__':
    unittest.main()
