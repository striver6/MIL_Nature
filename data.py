import torch


data = {
    "slides" : [r"D:\CAMELYON16\testing\images\1.svs",r"D:\CAMELYON16\testing\images\2.svs",
				r"D:\CAMELYON16\testing\images\3.svs",r"D:\CAMELYON16\testing\images\4.svs"
				],
    "grid":[
     [(74752, 117120),
	 (40576, 18432),
	 (1280, 19072)],
	[(77568, 158592),
	 (77312, 155776),
	 (21504, 216448),
	 (2304, 106112)],
     [(74752, 117120),
	 (40576, 18432),
	 (1280, 19072)],
	[(77568, 158592),
	 (77312, 155776),
	 (21504, 216448),
	 (2304, 106112)]
	],
	"targets" : [1,1,1,1],
	"mult" : 1,
	"level" : 1
}

torch.save(data,r"D:\Camp\train_lib\data.pt")
# torch.save(data,"sftp://root@172.16.4.226:12622/home/data/data.pt")
torch.save(data,"/home/data/data.pt")
# print("naiqa",torch.load(r"D:\Camp\train_lib\data.pt"))
# print("结束啊")