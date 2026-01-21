import random
import sys

class PayloadGenerator:
    @staticmethod
    def generate_long_string(length=50000):
        """Day 2: Long strings to test buffer limits [cite: 27]"""
        return "A" * length

    @staticmethod
    def generate_unicode():
        """Day 2: Unicode/Emojis to test encoding [cite: 29]"""
        return "Testing ⚠️ 🐛 👩‍💻 " + "\uFFFF" * 100

    @staticmethod
    def generate_nested_json(depth=50):
        """Day 2: Deeply nested JSON [cite: 28]"""
        data = {"final": "value"}
        for _ in range(depth):
            data = {"level": data}
        return data

    @staticmethod
    def generate_boundary_ints():
        """Day 2: Boundary values (MAX_INT, 0, -1) [cite: 31]"""
        return [0, -1, 2147483647, -2147483648, sys.maxsize]

    @staticmethod
    def generate_random_entropy(size=1024):
        """Day 2: Random entropy/garbage data [cite: 30]"""
        return "".join(chr(random.randint(0, 255)) for _ in range(size))
    
    @staticmethod
    def generate_regex_bomb():
        """
        Day 5: Regex Abuse.
        This pattern forces some regex engines into 'Catastrophic Backtracking',
        locking up the CPU (DoS attack).
        """
        return "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa!"

    @staticmethod
    def generate_malformed_schema():
        """
        Day 5: Malformed Schemas.
        Valid JSON, but breaks the business logic structure.
        """
        return {
            "user_id": -1, 
            "email": ["this", "should", "be", "a", "string"], 
            "role": "admin' OR '1'='1"  # SQL Injection hint
        }
    
    @staticmethod
    def generate_payload_flood(size=1024*1024):
        """
        Day 5: Payload Flooding.
        Send a massive 1MB+ JSON body to exhaust memory.
        """
        return {"garbage": "A" * size}