source /home/prefix/default/setup_env.sh
CURRENTDATE=`date +"%Y-%m-%d-%T"`
python top_block.py -i 2.wav -o ${CURRENTDATE}
met_decoder -q -c ${CURRENTDATE}.s output_pic
