echo "\n\n\t Running iPerf for $1 seconds...\n\t\t Please wait for the Graphical Result\n\n"
iperf -c $1 -t $2 -i 1 | tee result.txt &
sleep $2
python plotIperf.py
