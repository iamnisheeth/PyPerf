# PyPerf

This is a simple GUI report generator for Iperf tool.

Prerequisites :
1. User should have Iperf already set up ( client + Server )


How to run:
1. Clone the git repo to your local machine
2. Move to project directory /PyPerf
3. Execute this to give +x to runIperf.sh script
4. Start the Iperf Server ( $iperf -s)
5. On the client, run the script below by specifying the IP address and duration of Iperf run
   e.g. Running the below command   
            $ ./runIperf 127.0.0.1 5
        will execute the test against localhost for 5 seconds and will throw a graph at the end.
