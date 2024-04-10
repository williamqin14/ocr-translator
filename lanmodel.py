# This Python file uses the following encoding: utf-8

# if __name__ == "__main__":
#     pass

import torch
import time
from transformers import MBartForConditionalGeneration, MBart50TokenizerFast

def aiQuery(text):
    start = time.time()
    model = MBartForConditionalGeneration.from_pretrained("facebook/mbart-large-50-many-to-many-mmt")
    tokenizer = MBart50TokenizerFast.from_pretrained("facebook/mbart-large-50-many-to-many-mmt")

    # translate Japanese to English
    tokenizer.src_lang = "ja_XX"
    encoded_ar = tokenizer(text, return_tensors="pt")
    generated_tokens = model.generate(
        **encoded_ar,
        forced_bos_token_id=tokenizer.lang_code_to_id["en_XX"]
    )
    output = tokenizer.batch_decode(generated_tokens, skip_special_tokens=True)

    end = time.time()

    print(output, (end-start), "s")
    return output[0]
