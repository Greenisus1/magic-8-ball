#!/usr/bin/env python3
"""Random classic-style 8-ball replies. No AI, translations, history or network."""
import argparse
import random

RESPONSES = (
    'It is certain', 'It is decidedly so', 'Without a doubt',
    'Yes definitely', 'You may rely on it', 'As I see it, yes',
    'Most likely', 'Outlook good', 'Yes', 'Signs point to yes',
    'Reply hazy, try again', 'Ask again later', 'Better not tell you now',
    'Cannot predict now', 'Concentrate and ask again',
    "Don't count on it", 'My reply is no', 'My sources say no',
    'Outlook not so good', 'Very doubtful',
)

def answer(question, choose=random.choice):
    if not isinstance(question, str) or not question.strip():
        raise ValueError('Ask a question first.')
    return choose(RESPONSES)

def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--question', help='one question; prints only the answer')
    args = parser.parse_args(argv)
    try:
        if args.question is not None:
            if not args.question.strip():
                parser.error('Ask a question first.')
            print(answer(args.question))
            return 0
        while True:
            question = input('Question (/quit to exit): ')
            if question.strip().lower() in ('/quit', '/exit'):
                return 0
            if question.strip():
                print(answer(question))
    except (EOFError, KeyboardInterrupt):
        return 0

if __name__ == '__main__':
    raise SystemExit(main())
