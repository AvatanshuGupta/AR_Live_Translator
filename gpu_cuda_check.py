import torch

#Testing gpu and cuda

print("CUDA Available:", torch.cuda.is_available())
print("Torch Version:", torch.__version__)
if torch.cuda.is_available():
    print("GPU Name:", torch.cuda.get_device_name(0))
