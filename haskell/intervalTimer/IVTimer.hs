module IVTimer where
type Time = Int
data Alarm = Alarm (Time, (Time -> String))

execAlarm :: Alarm -> String
execAlarm (Alarm (t, fn)) = fn t

retTime :: Alarm -> Time
retTime (Alarm (t, fn)) = t

curAlarms :: [Alarm] -> Time -> [Alarm]
curAlarms as t = filter (\a -> ((retTime a) == t)) as

sample = [Alarm (10, show),Alarm (15, show),Alarm (15, show), Alarm (5, show)]
