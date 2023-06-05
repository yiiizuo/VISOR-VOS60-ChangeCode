# VISOR-VOS60-ChangeCode

# train
bash train.sh

# eval
Download Weights: 

Put Weights to ./weights

python eval -g 0 -s val -y 22 -D /data/EPIC-KITCHENS/DAVIS/VISOR_2022 -p ./weights/best.pth -backbone resnet50

Docker Link: https://drive.google.com/file/d/1W7tNImbkjXKko81s1PAesYgTsM4rUiHv/view?usp=sharing