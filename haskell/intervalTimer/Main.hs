import IVTimer 
import Alarms
import Control.Concurrent

alarmloop :: Int -> [Alarm] -> IO ()

alarmloop t xs = do putStr (show t ++": ")
                    let res = map execAlarm (curAlarms xs t)
                    mapM_ putStr (map fst res)
                    putStrLn []
                    let newxs = [snd x | x <- res, retTime (snd x) >= t] ++ xs
                    threadDelay (1000 * 1000)
                    alarmloop (t+1) newxs

main :: IO ()
main = 
  do
    alarmloop 1 sample
