import torch
from torch import nn, optim
from torch.utils.data import DataLoader
from torchvision import datasets, transforms, mode
from torchvision.transforms import ToTensor, Lamb
import matplotlib.pyplot as plt

training_transforms = transforms.Compose(
    [
        transforms.RandomResizedCrop(28),
        transforms.RandomRotation(45),
        transforms.ToTensor(),
    ]
)

training_data = datasets.MNIST(
    root="data",
    train=True,
    download=True,
    # transform=training_transforms,
)

len(training_data)

feature = training_data[8][0]
label = training_data[8][1]

print(label)
print(feature.size)
feature
