import os
import openai
openai.api_key = "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"
openai.FineTune.create(
    training_file="Data_cli_prepared.jsonl")
