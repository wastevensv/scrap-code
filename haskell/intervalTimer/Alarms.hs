module Alarms where
import IVTimer

doNothing :: Time -> (String, Alarm)
doNothing t = ("",Alarm(0, doNothing))

repeatMsg :: String -> Time -> (Time -> (String, Alarm))
repeatMsg str i = \t -> (str, Alarm((t+i), repeatMsg str i))

message :: String -> (Time -> (String, Alarm))
message str = \t -> (str, Alarm(0, doNothing))

sample = [Alarm(2, repeatMsg "Two" 2), Alarm(3, repeatMsg "Three" 3), Alarm(5, message "Hello"), Alarm(10, message "Test"), Alarm(15, message "Loop")]
