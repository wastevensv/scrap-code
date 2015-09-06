-- file: teaTimer.hs
-- Author: William A Stevens V
-- Written for Alex Kyte's packet challenge.
-- Purpose: Countdown the steeping time for various types of tea.

import Data.Char
import Data.Ord
import Control.Concurrent

countDown :: Int -> IO ()
countDown 0 = do putStr ['\r']
                 print 0
countDown t = do putStrLn . show $ t
                 threadDelay (1000 * 1000)
                 countDown(t-1)

chooseTea :: String -> IO()
chooseTea strength
      | strength == "black"  = countDown(15)
      | strength == "green"  = countDown(10)
      | strength == "herbal" = countDown(5)

main = do
  putStrLn "How strong is your tea?"
  x <- getLine
  chooseTea(x)
