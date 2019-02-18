

#step1: split img into dir by category using im2rec.py
python ${MXNET}/tools/im2rec.py --list --recursive --train-ratio 0.9 dog_data/dog ${img_root_dir}

#step2: generate recordIO files 
python ${MXNET}/tools/im2rec.py --resize 256 --quality 90 --num-thread 16 dog_data/dog ${img_root_dir}