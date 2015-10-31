import IVTimer 

main :: IO ()
main = 
  do
    let xs = sample
    t <- getLine
    mapM_ putStrLn (map execAlarm (curAlarms xs (read t)))
