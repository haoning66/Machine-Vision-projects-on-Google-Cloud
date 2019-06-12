#!/usr/bin/env bash
export DATA_SET_ROOT='../A2D'
PYTHONPATH='./':$PYTHONPATH python eval/baseline_gen_det_result.py \
    --dataset A2D \
    --cfg model_cfgs/e2e_faster_rcnn_R-101-FPN_1x.yaml \
    --image_dir $DATA_SET_ROOT/pngs320H \
    --test_lst $DATA_SET_ROOT/list/val.txt \
    --root $DATA_SET_ROOT/pngs320H \
    --anno_root $DATA_SET_ROOT/Annotations/mat \
    --id_map_file $DATA_SET_ROOT/list/actor_id_action_id.txt \
    --det_result_pkl /home/shinshukuni/csc249_final_proj/csc_249_final_proj_a2d_det/det_results/temp.pkl \
    --segment_length 2 \
    --load_ckpt /home/shinshukuni/csc249_final_proj/csc_249_final_proj_a2d_det/train_output/e2e_faster_rcnn_R-101-FPN_1x/Apr22-19-54-12_pytorch1-vm_step/ckpt/model_step11869.pth
