# Example of ReAct prompting

Note, in order to work, a local llama.cpp server needs to be running on port 8080 (refer to <https://github.com/J-sephB-lt-n/useful-code-snippets/blob/main/snippets/bash/llm/host_local_models_with_llama_cpp.sh> for instructions)

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python play_single_game_vanilla_prompt.py
python play_single_game_react_prompting.py --verbose
```
