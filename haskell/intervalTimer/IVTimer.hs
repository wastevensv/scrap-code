module IVTimer where
type Time = Int
data Alarm = Alarm (Time, (Time -> (String, Alarm)))

execAlarm :: Alarm -> (String, Alarm)
execAlarm (Alarm (t, fn)) = fn t

retTime :: Alarm -> Time
retTime (Alarm (t, fn)) = t

curAlarms :: [Alarm] -> Time -> [Alarm]
curAlarms as t = filter (\a -> ((retTime a) == t)) as
