import torch
# import sys

# sys.setdefaultencoding('utf-8')
pthfile = r'‪D:\训练营\医疗\MIL-nature-medicine-2019-master\resnet34-333f7ec4.pth'
net = torch.load(pthfile)

print(net)

