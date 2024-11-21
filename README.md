# preview

Review my commit.

## How to use

```bash
pip install preview
python -m preview
```

## Requirements

- Requires git and at least one commit.
- Requires OpenAI API key.
  - `OPENAI_API_KEY=<your-api-key>`

## Options

```bash
-m --mode | OpenAI Model (default: o1-mini)
-l --language | Review language (default: ENGLISH)
```

## How it works

Check your commit log and review it.

```bash
git show head -> llm review -> format review output
```

## Roadmap

- [x] Review head commit
- [ ] Review several commits
- [ ] Review branch

- [ ] Review with other LLM model providers
