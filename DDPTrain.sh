python -m torch.distributed.run --nnodes=1 --nproc_per_node=2 --node_rank=0 --master_port=11111 train.py \
-Dvisor /data/EPIC-KITCHENS/DAVIS/VISOR_2022/ -total_iter 80000 -test_iter 40000 -batch 32 \
-backbone resnet50 -save ../train3_weights/ -name experiment1 -wandb_logs 0 \
-resume /root/code/train2_weights/experiment1_resnet50_400000_32_119999.pth