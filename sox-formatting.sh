for FILE in *.wav; do
    echo -e "Processing audio '\e[32m$FILE\e[0m'";
  	# NAME = $(echo -e '\e[32m$FILE\e[0m'| cut -d '.' -f 1);
   #  echo $NAME;
    sox "${FILE}" -c 1 -r 16000 "out_${FILE}";
    python -m transcribe.py "out_${FILE}";
    rm "out_${FILE}";
done;

