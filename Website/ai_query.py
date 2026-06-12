import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), 'AiModel'))
from aipy_ai import ask

def main():
    print("AI Query Tool. Type 'exit' to quit.")
    print("Examples: 'reverse a string', 'sort a list', 'validate email'")
    while True:
        try:
            q = input("\nAsk AI: ").strip()
        except (EOFError, KeyboardInterrupt):
            break
        if not q:
            continue
        if q.lower() in ('exit', 'quit', '/exit', '/quit'):
            break
        print(ask(q))

if __name__ == "__main__":
    main()
