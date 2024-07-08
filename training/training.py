"""Training."""
import numpy as np
import torch
import sys
sys.path.append('..\\..')
import Transformers.model.transformer.Transformer

text = open("""c:\\users\\adrie\\GraphDataScience\\Transformers\\Datasets\\tiny_shakespeare.txt""",
     'rb').read().decode(encoding='utf-8')
print('Length of text: {} characters'.format(len(text)))
print(text[:250])

# unique characters in the file
vocab = sorted(set(text))
print('{} unique characters'.format(len(vocab)))

# Lookup tables
char2idx = {u:i for i, u in enumerate(vocab)}
idx2char = np.array(vocab)

text_as_int = np.array([char2idx[c] for c in text])
print("char2idx")
print(char2idx)
print("idx2char")
print(idx2char)
print("text_as_int")
print(text_as_int)
print ('{} ---- characters mapped to int ---- > {}'.format(repr(text[:13]), text_as_int[:13]))

# Create training examples:
seq_length = 128
examples_per_epoch = len(text)//(seq_length)

int_text_tensor = torch.tensor(text_as_int)
chunks = torch.chunk(int_text_tensor, examples_per_epoch, 0)
print(int_text_tensor)

examples = [chunk[:-1] for chunk in chunks]
targets = [chunk[1:] for chunk in chunks]
print(examples[4])
print(targets[4])


model_parameters = {}
transformer = Transformer(model_parameters)