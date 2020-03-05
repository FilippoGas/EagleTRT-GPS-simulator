#!/bin/bash

# Adding killing trap
function ctrl_c() {
        echo "killing processes"
        kill $GPS_ID
        kill $CAN_ID
}
trap ctrl_c SIGINT

# Starting canplayer
echo "starting can process"
bash ./can.sh &
CAN_ID=$! 

# Starting gps simulator
echo "starting gps process"
./simulator.out &
GPS_ID=$!

# Printing 
echo "CAN_ID" $CAN_ID
echo "GPS_ID" $GPS_ID

# Waiting for trap
wait $CAN_ID
wait $GPS_ID