import torch


valdata = {
    "slides" : [r"D:\CAMELYON16\testing\images\5.svs"
				],
    "grid":[
     [(74752, 117120),
	 (40576, 18432),
	 (1280, 19072)]
	],
	"targets" : [1],
	"mult" : 1,
	"level" : 1
}

# torch.save(valdata,r"D:\训练营\医疗\MedicalData\val_lib\valdata.pt")
# print(torch.load(r"D:\训练营\医疗\MedicalData\val_lib\valdata.pt"))
# torch.save(valdata,r"D:\Camp\val_lib\valdata.pt")
torch.save(valdata,"/home/data/valdata.pt")
print(torch.load(r"D:\Camp\val_lib\valdata.pt"))


