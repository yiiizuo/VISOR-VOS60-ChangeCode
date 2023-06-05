python train_stm_baseline.py -Dvisor /data/EPIC-KITCHENS/DAVIS/VISOR_2022/ -total_iter 80001 -test_iter 40000 \
-batch 1 -backbone resnet50 -save ../train3_weights/ -name experiment1 -wandb_logs 0 \
-resume /root/code/train2_weights/experiment1_resnet50_400000_32_119999.pth