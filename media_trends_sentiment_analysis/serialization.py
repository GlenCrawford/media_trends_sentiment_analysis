import torch

MODEL_STORAGE_PATH = 'models/' # Relative from project root directory.

def load_model(model):
  model.load_state_dict(torch.load(file_path_for_model(model)))

def save_model(model):
  torch.save(model.state_dict(), file_path_for_model(model))

def file_path_for_model(model):
  return MODEL_STORAGE_PATH + type(model).__name__ + '.pth'
