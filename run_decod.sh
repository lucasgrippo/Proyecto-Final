source /home/prefix/default/setup_env.sh
CURRENTDATE=`date +"%Y-%m-%d-%T"`
python top_block.py -i 1.wav -o ${CURRENTDATE}
#met_decoder -q -c out_soft.s output_pic
