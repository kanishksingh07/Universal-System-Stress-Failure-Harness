
import unittest
import sys
import os
import inspect

# Add parent dir to path to import generators
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from generators.mutators import PayloadGenerator

class TestNoExec(unittest.TestCase):
    def test_payloads_are_passive_data(self):
        """Verify all mutators return data, not code objects."""
        mutators = [
            PayloadGenerator.generate_long_string,
            PayloadGenerator.generate_unicode,
            PayloadGenerator.generate_nested_json,
            PayloadGenerator.generate_boundary_ints,
            PayloadGenerator.generate_regex_bomb,
            PayloadGenerator.generate_malformed_schema,
            PayloadGenerator.generate_payload_flood
        ]
        
        for func in mutators:
            payload = func()
            # If list (boundary ints), check elements
            if isinstance(payload, list):
                for item in payload:
                     self.assertFalse(callable(item), f"{func.__name__} returned executable code!")
            else:
                self.assertFalse(callable(payload), f"{func.__name__} returned executable code!")
                
    def test_codebase_no_exec(self):
        """Scan codebase for dangerous functions like eval/exec used on dynamic inputs."""
        # Simple static analysis
        risk_terms = ['eval(', 'exec(', 'subprocess.call', 'os.system']
        
        source_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
        
        for root, dirs, files in os.walk(source_dir):
            if ".git" in root or "__pycache__" in root or "venv" in root:
                continue
                
            for file in files:
                if file.endswith(".py") and file != "test_no_exec.py": # exclude self
                    path = os.path.join(root, file)
                    with open(path, 'r', encoding='utf-8') as f:
                        content = f.read()
                        for term in risk_terms:
                            if term in content:
                                # Allow known safe usages if strictly commented/controlled (none expected here)
                                # For now, strict failure
                                self.fail(f"Dangerous term '{term}' found in {file}. Manual audit required.")

if __name__ == '__main__':
    unittest.main()
