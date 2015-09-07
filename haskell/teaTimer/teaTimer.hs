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

chooseTea :: String -> Int
chooseTea strength
      | strength == "black"  = 15
      | strength == "green"  = 10
      | strength == "herbal" = 5
      | otherwise = 10

main = do
  putStrLn "How strong is your tea?"
  x <- getLine
  let t = chooseTea(x)
  countDown(t)
